#!/usr/bin/env python
# coding: utf-8

# In[1]:


from limits import get_loop_level_records, get_tree_level_records
import pandas as pd
import numpy as np


# ## Tree-level heatmaps

# In[ ]:


tree_level_records = get_tree_level_records()


# In[ ]:


df = pd.DataFrame.from_records(tree_level_records)


# You need to scale the tree-level coefficients that you have with the factors from Arnau.

# In[4]:


data = df[["smeft_label", "smeft_flavour", "lambda_limit_coeff_1"]].groupby(["smeft_label", "smeft_flavour"], as_index=False).max().to_dict(orient="list")

max_lambda_dict = {}
for smeft_label, smeft_flavour, value in zip(*data.values()):
    if (smeft_label, smeft_flavour) in max_lambda_dict:
        print("Problem...")

    max_lambda_dict[(smeft_label, smeft_flavour)] = value


# In[5]:


import sympy
import numpy as np
from tables import LAMBDA

# Set `LAMBDA` to this value in `gamma_coeff_1` and then normalise to the rate associated with the experimental limit
def calc_bound_saturation(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x

    gamma = row.gamma.subs({row.smeft_op: 1.0, LAMBDA: max_lambda_dict[(row.smeft_label, str(row.smeft_flavour))]})
    gamma_limit = 1.0 / value_in_inv_gev(row.lifetime_limit)

    ratio = gamma / gamma_limit
    return ratio

df["bound_saturation"] = df.apply(calc_bound_saturation, axis=1)


# In[81]:


higher_dimensional_labels = {
    "ddqlHH",
    "eqqqHHH",
    "luqqHHH", 
    "qqedHHD",
    "qqlqHHD",
    "udqlHHD",
    # These aren't higher dimensional, but still suppressed
    # "l~qdDd",
    # "e~dddD",
}

reduced_df = df[(~df['smeft_label'].isin(higher_dimensional_labels)) & (~df['smeft_flavour'].astype(str).str.contains('3'))]


# In[82]:


ordering = [
    "qqql",
    "qque",
    "duue",
    "duql",
    "l~dddH",
    "l~dqqH~",
    "e~qddH~",
    "l~dudH~",
    "l~qdDd",
    "e~dddD",
    "ddqlHH",
    "eqqqHHH",
    "luqqHHH",
    "qqedHHD",
    "qqlqHHD",
    "udqlHHD",
]

# Convert smeft_flavour to int
df.smeft_flavour = df.smeft_flavour.astype(int)

def ordering_func(x: pd.Index) -> pd.Index:
    if isinstance(x[0], np.int64):
        return x
    return pd.Index([ordering.index(i) for i in x])

dim_7_heatmap_df = pd.pivot_table(
    df[(~df['smeft_label'].isin(higher_dimensional_labels)) & (~df['smeft_flavour'].astype(str).str.contains('3'))],
    values='bound_saturation',
    index=['smeft_label', 'smeft_flavour'],
    columns=['process'], 
    aggfunc="max", 
    fill_value=0,
    ).sort_index(key=ordering_func)

dim_9_heatmap_df = pd.pivot_table(
    df[(df['smeft_label'].isin(higher_dimensional_labels)) & (~df['smeft_flavour'].astype(str).str.contains('3'))],
    values='bound_saturation',
    index=['smeft_label', 'smeft_flavour'],
    columns=['process'], 
    aggfunc="max", 
    fill_value=0,
    ).sort_index(key=ordering_func)

np.array(dim_7_heatmap_df, dtype=float)


# In[83]:


dim_7_data = np.array(dim_7_heatmap_df, dtype=float)
dim_9_data = np.array(dim_9_heatmap_df, dtype=float)

def latex_format(value):
    if 0 < abs(value) < 9e-3:
        base, exp = "{:.0e}".format(value).replace('e-0', 'e-').split("e")
        return fr"${base} \cdot 10^{{{exp}}}$"
    else:
        return fr"$ {value:.2f} $"
    
dim_7_formatted_labels = np.vectorize(latex_format)(dim_7_data).astype(str)
dim_9_formatted_labels = np.vectorize(latex_format)(dim_9_data).astype(str)


# In[94]:


import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LogNorm

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",  
})

def wrap_math(expr: str) -> str:
    return rf"${expr}$"

def pretty_process(proc: str) -> str:
    return wrap_math(proc)

def pretty_label(label: str, flavour: int) -> str:
    smeft_label_dict = {
        "l~dqqH~": r"\bar{l}dqq\tilde{H}",
        "e~qddH~": r"\bar{e}qdd\tilde{H}",
        "l~dudH~": r"\bar{l}dud\tilde{H}",
        "l~dddH": r"\bar{l}dddH",
        "e~dddD": r"\bar{e}dddD",
        "l~qdDd": r"\bar{l}qdDd",
    }

    replacement = smeft_label_dict.get(label)
    if replacement is None:
        replacement = label

    return wrap_math("[\\mathcal{O}_{" + replacement + "}]" + rf"_{{{flavour}}}")

def plot_fingerprints(df: pd.DataFrame, labels: list[str], savefig: bool = False, filename: str = "correlations.pdf") -> None:
    """Function acting on the dataframe (with an explicit value of Λ set) to make
    plot.

    """
    f, ax = plt.subplots(figsize=(9, 11))

    cmap = sns.cubehelix_palette(
        n_colors=9, start=0, rot=-0.2, gamma=0.7, hue=0.8, light=0.9, dark=0.1, as_cmap=True
    )

    ax.set_xlabel("Processes")
    ax.set_ylabel("Operators")
    
    axes_subplot = sns.heatmap(
        np.array(df, dtype=float),
        center=0,
        linewidths=0.5,
        cmap=cmap,
        norm=LogNorm(),
        ax=ax,
        #annot=True,
        annot=labels,
        fmt="",
        #annot_kws={"size": 8},
        xticklabels=[pretty_process(proc) for proc in df.keys()],
        yticklabels=[pretty_label(label, flavour) for label, flavour in df.index],
        # cbar_kws={'label': 'Bound Saturation'}
    )
    
    for label in ax.get_xticklabels():
        label.set_rotation(75)
        label.set_ha("center")

    for label in ax.get_yticklabels():
        label.set_rotation(15)
        label.set_ha("right")
        
    ax.yaxis.set_tick_params(labelsize=15)
    ax.xaxis.set_tick_params(labelsize=15)

    # ax.collections[0].colorbar.set_label("Bound Saturation")
    ax.figure.axes[-1].set_ylabel('Bound Saturation', size=15)
    ax.figure.axes[-1].tick_params(labelsize=14)
    
    ax.tick_params(axis="x")
    ax.tick_params(axis="y")

    if savefig: 
        snsfig = axes_subplot.get_figure()
        snsfig.savefig(f'/Users/johngargalionis/Desktop/{filename}', bbox_inches="tight")
    
    return axes_subplot


# In[95]:


plot_fingerprints(dim_7_heatmap_df, labels=dim_7_formatted_labels, savefig=True, filename="dim_7_tree_level_correlations.pdf")


# In[96]:


plot_fingerprints(dim_9_heatmap_df, labels=dim_9_formatted_labels, savefig=True, filename="dim_9_tree_level_correlations.pdf")


# ## Loop-level heatmap

# In[2]:


loop_level_records = get_loop_level_records()


# In[3]:


df = pd.DataFrame.from_records(loop_level_records)
df = df.drop_duplicates()
df.lambda_limit_coeff_1 = df.lambda_limit_coeff_1.astype(float)
# df = df.sort_values(["lambda_limit_coeff_1", "fieldstring_label", "fieldstring_flavour"])

print(df.size)


# In[117]:


from limits import VEV
from constants import VEV_VAL
from collections import defaultdict

df[["smeft_label", "smeft_flavour", "fieldstring_label", "fieldstring_flavour", "smeft_op", "smeft_op_expr"]]

def smeft_coeff(row):
    subs_dict = defaultdict(lambda: 0)
    subs_dict[VEV] = 1
    subs_dict[LAMBDA] = 1
    subs_dict[row.smeft_op] = 1
    return float(abs(row.smeft_op_expr.subs(subs_dict).evalf()))

df["abs_smeft_coeff"] = df.apply(smeft_coeff, axis=1)
# df['abs_smeft_coeff'] = pd.to_numeric(df['abs_smeft_coeff'], errors='coerce')

heatmap_df = pd.pivot_table(
    df[df.fieldstring_label=="49"],
    values='abs_smeft_coeff',
    index=['fieldstring_label', 'fieldstring_flavour'],
    columns=['smeft_label', 'smeft_flavour'], 
    aggfunc=lambda x: max(x), 
    fill_value=0,
)

heatmap_df


#test = df.groupby(by=["fieldstring_label", "fieldstring_flavour", "process"], as_index=False).agg({"smeft_op_expr": "sum"})


# In[118]:


sns.heatmap(heatmap_df, annot=False, norm='log', cmap='Blues')

##

# Customize x-axis labels
#x_labels = [f"${label[0]}_{{{label[1]}}}$" for label in heatmap_df.columns.get_level_values(1)]
#plt.xticks(range(len(heatmap_df.columns.get_level_values(1))), x_labels)

# Customize y-axis labels
#y_labels = [f"${label[0]}_{{{label[1]}}}$" for label in heatmap_df.index]
#plt.yticks(range(len(heatmap_df.index)), y_labels)


# In[12]:


# Construct `best` dataframe containing flavour structures listed in the table that contain the contributions that give the best limits
df_1 = df.groupby("fieldstring_label", as_index=False).apply(lambda x: x.nlargest(1, "lambda_limit_coeff_1"))
merged = pd.merge(df, df_1, on=["fieldstring_label", "fieldstring_flavour"], how="right")
best = merged.groupby(by=["fieldstring_label", "process_y"], as_index=False).agg({"gamma_fieldstring_coeff_1_y": "sum", "lifetime_limit_y": "first", "fieldstring_flavour": "first"})
best["process"] = best["process_y"]
best["gamma_fieldstring_coeff_1"] = best["gamma_fieldstring_coeff_1_y"]
best["lifetime_limit"] = best["lifetime_limit_y"]
best = best[["fieldstring_label", "fieldstring_flavour", "process", "gamma_fieldstring_coeff_1", "lifetime_limit"]]


# In[32]:


result_dfs = []

# Best limit flavour structures
conditions = [
    (11, "1113"), (12, "1131"), (13, "1311"), (14, "1123"),
    (15, "1113"), (16, "1131"), (17, "1111"), (18, "1111"),
    (19, "1113"), (20, "1113"), (21, "1112"), (22, "1111"),
    (23, "1111"), (24, "1111"), (25, "111111"), (26, "1211"),
    (27, "111122"), (28, "133111"), (29, "113321"), (30, "133111"),
    (31, "111112"), (32, "111121"), (33, "122111"), (34, "1211"),
    (35, "133121"), (36, "1121"), (37, "1113"), (38, "1112"),
    (39, "131123"), (40, "113131"), (41, "133112"), (42, "111331"),
    (43, "1121"), (44, "1131"), (45, "1111"), (46, "1111"),
    (47, "1121"), (48, "1111"), (49, "331121"), (50, "131311"),
]

for label, flavour in conditions:
    condition = (df.fieldstring_label == label) & (df.fieldstring_flavour == flavour)
    result_df = df[condition].groupby(by=["fieldstring_label", "process"], as_index=False).agg({
        "gamma_fieldstring_coeff_1": "sum",
        "lifetime_limit": "first",
        "fieldstring_flavour": "first"
    })
    result_dfs.append(result_df)

best = pd.concat(result_dfs)


# In[33]:


from tables import LAMBDA

def calc_exp_ratio(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x

    gamma = row.gamma_fieldstring_coeff_1.subs({LAMBDA: 1.})
    gamma_limit = 1.0 / value_in_inv_gev(row.lifetime_limit)

    ratio = gamma / gamma_limit
    return ratio


df.fieldstring_label = df.fieldstring_label.astype(int)

# Democratic
democratic = df.groupby(by=["fieldstring_label", "process"], as_index=False).agg({"gamma_fieldstring_coeff_1": "sum", "lifetime_limit": "first"})
democratic["exp_ratio"] = democratic.apply(calc_exp_ratio, axis=1)
max_ratio_dict = democratic[["fieldstring_label", "exp_ratio"]].groupby(by="fieldstring_label").max().to_dict()["exp_ratio"]


# Best limits
best["exp_ratio"] = best.apply(calc_exp_ratio, axis=1)
max_ratio_dict_best = best[["fieldstring_label", "exp_ratio"]].groupby(by="fieldstring_label").max().to_dict()["exp_ratio"]

def calc_bound_saturation_michael(row):
    return row.exp_ratio / max_ratio_dict[row.fieldstring_label]

def calc_bound_saturation_michael_best(row):
    return row.exp_ratio / max_ratio_dict_best[row.fieldstring_label]

democratic["bound_saturation"] = democratic.apply(calc_bound_saturation_michael, axis=1)
best["bound_saturation"] = best.apply(calc_bound_saturation_michael_best, axis=1)



heatmap_df = pd.pivot_table(
    best[best.bound_saturation > 9.999e-6],
    values='bound_saturation',
    index=['fieldstring_label', "fieldstring_flavour"],
    columns=['process'], 
    aggfunc=lambda x: float(max(x)), 
    fill_value=0,
)

heatmap_df


# In[5]:


test = df.groupby(by=["fieldstring_label", "fieldstring_flavour", "process"], as_index=False).agg({"gamma_fieldstring_coeff_1": "sum", "lifetime_limit": "first"})


# In[6]:


from tables import LAMBDA

def calc_exp_ratio(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x

    gamma = row.gamma_fieldstring_coeff_1.subs({LAMBDA: 1.})
    gamma_limit = 1.0 / value_in_inv_gev(row.lifetime_limit)

    ratio = gamma / gamma_limit
    return ratio


# In[ ]:


test["exp_ratio"] = test.apply(calc_exp_ratio, axis=1)
test


# In[7]:


max_ratio_dict = test[["fieldstring_label", "fieldstring_flavour", "exp_ratio"]].groupby(by=["fieldstring_label", "fieldstring_flavour"]).max().to_dict()["exp_ratio"]

def calc_bound_saturation_michael(row):
    return row.exp_ratio / max_ratio_dict[(row.fieldstring_label, row.fieldstring_flavour)]

test["bound_saturation"] = test.apply(calc_bound_saturation_michael, axis=1)
test.fieldstring_label = test.fieldstring_label.astype(int)


# In[8]:


heatmap_df = pd.pivot_table(
    test[(test.fieldstring_label == 49) & (test.bound_saturation > 9.999e-6)],
    values='bound_saturation',
    index=['fieldstring_label', 'fieldstring_flavour'],
    columns=['process'], 
    aggfunc="max", 
    fill_value=0,
)

heatmap_df


# In[9]:


from tables import LAMBDA

# For each operator, get the max (scaled) lambda limit
max_lambda_dict = df[["fieldstring_label", "fieldstring_flavour", "lambda_limit_coeff_1"]].groupby(["fieldstring_label", "fieldstring_flavour"]).max().to_dict()
max_lambda_dict = max_lambda_dict["lambda_limit_coeff_1"]

# Set `LAMBDA` to this value in `gamma_coeff_1` and then normalise to the rate associated with the experimental limit
def calc_bound_saturation(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x

    gamma = row.gamma_fieldstring_coeff_1.subs({LAMBDA: max_lambda_dict[(row.fieldstring_label, row.fieldstring_flavour)]})
    gamma_limit = 1.0 / value_in_inv_gev(row.lifetime_limit)

    ratio = gamma / gamma_limit
    return ratio

df["bound_saturation"] = df.apply(calc_bound_saturation, axis=1)

# Pick out dimension here
df.fieldstring_label = df.fieldstring_label.astype(int)
d8_mask = (df.fieldstring_label > 10) & (df.fieldstring_label < 25)
d9_mask = df.fieldstring_label > 24
#df = df[d8_mask]

# Isolate dominant contribution to each operator
#df_bound_sat = df[["fieldstring_label", "fieldstring_flavour", "process", "bound_saturation"]].groupby(["fieldstring_label", "fieldstring_flavour", "process"], as_index=False).max()
#df_bound_sat = df[["fieldstring_label", "fieldstring_flavour", "smeft_label", "smeft_flavour", "process", "bound_saturation"]].drop_duplicates(["fieldstring_label", "smeft_label", "smeft_flavour", "process"], inplace=False).groupby(["fieldstring_label", "fieldstring_flavour", "process"], as_index=False).max()

# df_bound_sat = df[["fieldstring_label", "fieldstring_flavour", "smeft_label", "smeft_flavour", "process", "bound_saturation"]].groupby(["fieldstring_label", "fieldstring_flavour", "process"], as_index=False).max()


# In[14]:


df_bound_sat = df.groupby(["fieldstring_label", "smeft_label", "smeft_flavour", "process"], as_index=True).apply(lambda x: x)


# In[62]:


test = df[["fieldstring_label", "fieldstring_flavour", "smeft_label", "smeft_flavour", "process", "bound_saturation"]].drop_duplicates(["fieldstring_label", "smeft_label", "smeft_flavour", "process"])

test[(test.fieldstring_label == 16) & (test.fieldstring_flavour == "1113")]


# In[51]:


test[(test.fieldstring_label == 17) & (test.smeft_flavour == "1311")]


# In[5]:


grouped_df = df_bound_sat.groupby(["fieldstring_label", "fieldstring_flavour"])
filtered_df = grouped_df.filter(lambda x: len(x) > 1)
shortened_df_bound_sat = filtered_df.reset_index(inplace=False).groupby(["fieldstring_label", "fieldstring_flavour", "process"], as_index=False).max()


# In[65]:


df[d9_mask].drop_duplicates(["fieldstring_label", "smeft_op", "process"])


# In[110]:


heatmap_df = pd.pivot_table(
    df[(df.fieldstring_label > 46) & (df.fieldstring_label < 470) & (df.bound_saturation > 9.999e-6)],
    values='bound_saturation',
    index=['fieldstring_label', 'fieldstring_flavour'],
    columns=['process'], 
    aggfunc="max", 
    fill_value=0,
)

heatmap_df


# In[34]:


def latex_format(value):
    if abs(value) == 0:
        return fr"${value:.0f}$"

    if abs(value) > 0.9:
        return "$10^{0}$" 

    base, exp = "{:.0e}".format(value).replace('e-0', 'e-').split("e")
    if int(exp) < -5:
        return "$0$"

    if float(base) < 5:
        return fr"$10^{{{exp}}}$"
    elif float(base) >= 5:
        return fr"$10^{{{int(exp)+1}}}$"
    else:
        raise ValueError

data = np.array(heatmap_df, dtype=float)
formatted_labels = np.vectorize(latex_format)(data).astype(str)

def replace_unity(x):
    return x.replace("$10^{0}$", "$1$")

replace_vectorized = np.vectorize(replace_unity)
formatted_labels = replace_vectorized(formatted_labels)


# In[37]:


import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LogNorm
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",  
})

def wrap_math(expr: str) -> str:
    return rf"${expr}$"

def pretty_process(proc: str) -> str:
    return wrap_math(proc)

def pretty_label(label: str, flavour: int) -> str:
    return wrap_math(rf"{label}_{{{flavour}}}")

def pretty_label_no_flavour(label: str) -> str:
    return wrap_math(rf"{label}")

def plot_fingerprints(df: pd.DataFrame, savefig: bool = False, formatted_labels=formatted_labels) -> None:
    """Function acting on the dataframe (with an explicit value of Λ set) to make
    plot.

    """
    f, ax = plt.subplots(figsize=(9, 11))

    cmap = sns.cubehelix_palette(
        n_colors=9, start=0, rot=-0.2, gamma=0.7, hue=0.8, light=0.9, dark=0.1, as_cmap=True
    )

    ax.set_xlabel("Processes")
    ax.set_ylabel("Operators")

    data = np.array(df, dtype=float)
    #data[data < 9.999e-6] = 0

    axes_subplot = sns.heatmap(
        data,
        center=0,
        linewidths=0.5,
        cmap=cmap,
        norm=LogNorm(),
        ax=ax,
        annot=formatted_labels,
        fmt="",
        xticklabels=[pretty_process(proc) for proc in df.keys()],
        yticklabels=[pretty_label(label, flavour) for label, flavour in df.index],
        # yticklabels=[pretty_label_no_flavour(label) for label in df.index],
        # cbar_kws={'label': 'Bound Saturation', 'shrink': 1.00, 'aspect': 30}
    )

    for label in ax.get_xticklabels():
        label.set_rotation(75)
        label.set_ha("center")

    for label in ax.get_yticklabels():
        label.set_rotation(15)
        label.set_ha("right")
        
        
    ax.yaxis.set_tick_params(labelsize=15)
    ax.xaxis.set_tick_params(labelsize=15)

    # ax.collections[0].colorbar.set_label("Bound Saturation")
    ax.figure.axes[-1].set_ylabel('Bound Saturation', size=15)
    
    ax.tick_params(axis="x")
    ax.tick_params(axis="y")

    if savefig: 
        snsfig = axes_subplot.get_figure()
        #snsfig.savefig('/Users/johngargalionis/Desktop/dim_8_loop_level_correlations_18_20.pdf', bbox_inches="tight")
        snsfig.savefig('/Users/johngargalionis/Desktop/best_limit_correlations.pdf', bbox_inches="tight")
    
    return axes_subplot


# In[38]:


plot_fingerprints(heatmap_df, savefig=True)


# ## Old heatmap

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from collections import defaultdict

from matplotlib.colors import LogNorm

plt.style.use("/Users/johngargalionis/Dropbox/research/bviolation/ProtonDecayCalc/python/nord.mplstyle")
cmap = sns.cubehelix_palette(
    n_colors=9, start=0, rot=-0.2, gamma=0.7, hue=0.8, light=0.9, dark=0.1, as_cmap=True
)

sns.set_theme(style="whitegrid")

from limits import derive_general_limits, derive_loop_limits

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",  
})


# In[2]:


from tables import LAMBDA


# In[3]:


fieldstring_limits = derive_loop_limits()


# In[4]:


for fl in fieldstring_limits:
    fl["process"] = "$" + fl["process"] + "$"


# In[5]:


op_dict = defaultdict(dict)
for fl in fieldstring_limits:
    if fl["fieldstring_flavour"] == "2111":
        op_dict[fl["fieldstring_label"]+","+"2111"][fl["process"]] = fl["gamma_fieldstring_coeff_1"]
    if fl["fieldstring_flavour"] == "1211":
        op_dict[fl["fieldstring_label"]+","+"1211"][fl["process"]] = fl["gamma_fieldstring_coeff_1"]
    if fl["fieldstring_flavour"] == "1121":
        op_dict[fl["fieldstring_label"]+","+"1121"][fl["process"]] = fl["gamma_fieldstring_coeff_1"]
    if fl["fieldstring_flavour"] == "1112":
        op_dict[fl["fieldstring_label"]+","+"1112"][fl["process"]] = fl["gamma_fieldstring_coeff_1"]


# In[6]:


def make_dataframe(op_dict, lambda_: float) -> pd.DataFrame:
    """Sets the value of Λ to a float in GeV and returns a Pandas DataFrame
    object.

    """
    index = op_dict.keys()
    data = [
        {
            proc: float(expr.subs(LAMBDA, lambda_))
            for proc, expr in fingerprint.items()
        }
        for fingerprint in op_dict.values()
    ]

    df = pd.DataFrame(data, index=index)

    return df

df=make_dataframe(op_dict=op_dict, lambda_=1e10)


# In[7]:


df


# In[12]:


# Different  workflow
df = pd.DataFrame.from_records(fieldstring_limits)
df = df.astype({'lambda_limit_coeff_1': 'float'})


# In[13]:


# Different workflow
df["gamma_fieldstring_coeff_1_lambda_1e15"] = [float(expr.subs({LAMBDA: 1e15})) for expr in df["gamma_fieldstring_coeff_1"]]


# In[8]:


from typing import Tuple

def plot_fingerprints(
    df: pd.DataFrame, figsize: Tuple[float, float], save_path=None, title=None, **kwargs
):
    """Function acting on the dataframe (with an explicit value of Λ set) to make
    plot.

    If `save_path` is not `None`, attempts to save the figure to the path,
    otherwise returns the figure.

    The `save_path` variable should look like
    "/Users/johngargalionis/Desktop/test", importantly without the file
    extension!

    """

    fig, ax = plt.subplots(figsize=figsize)

    ax.set_xlabel("Processes")
    ax.set_ylabel("Operators")

    # annot = df.copy()
    # annot_labels = np.empty_like(df, dtype=str)
    # annot_mask = arr > 1e-3
    # for k in annot.keys():
    #     annot[annot[k] < 1e-3] = 0

    axes_subplot = sns.heatmap(
        np.array(df),
        # center=0,
        linewidths=0.5,
        cmap=cmap,
        # norm=LogNorm(),
        annot=True,
        annot_kws={"size": 8},
        ax=ax,
        xticklabels=[s for s in df.keys()],
        yticklabels=[s for s in df.index],
        **kwargs,
    )

    if title is not None:
        axes_subplot.set(title=title)

    for label in ax.get_xticklabels():
        label.set_rotation(75)
        label.set_ha("right")

    for label in ax.get_yticklabels():
        label.set_rotation(15)
        label.set_ha("right")

    ax.tick_params(axis="x")
    ax.tick_params(axis="y")

    # ax.axvline(2, color="white", lw=5)

    for t in ax.texts:
        if float(t.get_text()) >= 1e-3:
            t.set_text(t.get_text())  # Set the text
        else:
            t.set_text("")

    if save_path:
        # Save and remove excess whitespace
        for format_ in IMG_FORMATS:
            fig.savefig(save_path + "." + format_, format=format_, bbox_inches="tight")
        return None

    return axes_subplot


def plot_lambdas(
    df: pd.DataFrame, figsize: Tuple[float, float], save_path=None, **kwargs
):
    """Function acting on the dataframe (with an explicit value of Λ set) to make
    plot.

    If `save_path` is not `None`, attempts to save the figure to the path,
    otherwise returns the figure.

    The `save_path` variable should look like
    "/Users/johngargalionis/Desktop/test", importantly without the file
    extension!

    """

    fig, ax = plt.subplots(figsize=figsize)

    ax.set_xlabel("Processes")
    ax.set_ylabel("Operators")

    axes_subplot = sns.heatmap(
        np.array(df),
        center=0,
        linewidths=0.5,
        cmap=cmap,
        norm=LogNorm(),
        ax=ax,
        xticklabels=[wrap_math(TO_LATEX[s]) for s in df.keys()],
        yticklabels=[wrap_math(s) for s in df.index],
        **kwargs,
    )

    for label in ax.get_xticklabels():
        label.set_rotation(75)
        label.set_ha("right")

    for label in ax.get_yticklabels():
        label.set_rotation(15)
        label.set_ha("right")

    ax.tick_params(axis="x")
    ax.tick_params(axis="y")

    if save_path:
        # Save and remove excess whitespace
        for format_ in IMG_FORMATS:
            fig.savefig(save_path + "." + format_, format=format_, bbox_inches="tight")
        return None

    return axes_subplot


# In[11]:


def plot_fingerprints(df: pd.DataFrame) -> None:
    """Function acting on the dataframe (with an explicit value of Λ set) to make
    plot.

    """
    f, ax = plt.subplots(figsize=(9, 11))


    ax.set_xlabel("Processes")
    ax.set_ylabel("Operators")
    
    axes_subplot = sns.heatmap(
        np.array(df),
        center=0,
        linewidths=0.5,
        cmap=cmap,
        norm=LogNorm(),
        ax=ax,
        annot=True,
        annot_kws={"size": 8},
        xticklabels=df.keys(),
        yticklabels=[f"${s.split(',')[0]}_{{{s.split(',')[1]}}}$" for s in df.index],
    )
    
    for t in ax.texts:
        if float(t.get_text()) >= 1e-3:
            t.set_text(t.get_text())  # Set the text
        else:
            text = t.get_text()
            number, exponent = text.split("e-")
            t.set_text(f"${'-'+exponent}$")

    
    # axes_subplot.set(title="")

    
    for label in ax.get_xticklabels():
        label.set_rotation(75)
        label.set_ha("right")

    for label in ax.get_yticklabels():
        label.set_rotation(15)
        label.set_ha("right")
        
        
    ax.yaxis.set_tick_params(labelsize=16)
    ax.xaxis.set_tick_params(labelsize=16)
        
    
    ax.tick_params(axis="x")
    ax.tick_params(axis="y")
    
    snsfig = axes_subplot.get_figure()
    snsfig.savefig('/Users/johngargalionis/Desktop/single-second-gen-fingerprints.pdf', bbox_inches="tight")
    
    return axes_subplot


# In[12]:


plot_fingerprints(df)


# In[ ]:




