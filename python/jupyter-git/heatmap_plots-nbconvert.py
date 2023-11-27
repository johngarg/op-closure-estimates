#!/usr/bin/env python
# coding: utf-8

# In[1]:


from limits import get_loop_level_records, get_tree_level_records
import pandas as pd


# ## Tree-level heatmaps

# In[3]:


tree_level_records = get_tree_level_records()


# In[4]:


df = pd.DataFrame.from_records(tree_level_records)


# You need to scale the tree-level coefficients that you have with the factors from Arnau.

# In[5]:


arnau_growth_factors = [
    ("QQQL",1111,5.7,6),
    ("QQue",1111,3.1,6),
    ("duQL",1111,2.9,6),
    ("duue",1111,2.7,6),
    ("QQQL",2111,3.5,6),
    ("QQQL",1211,4.6,6),
    ("duQL",2111,3.0,6),
    ("duQL",1121,2.7,6),
    ("duue",2111,2.5,6),
    ("QQue",2111,3.1,6),
    ("ldud",1111,1.8,7),
    ("ldqq",1111,2.1,7),
    ("ldud",1211,1.6,7),
    ("ldud",1112,1.7,7),
    ("ldqq",1211,1.9,7),
    ("ldqq",1121,1.8,7),
    ("ldqq",1112,1.8,7),
    ("lddd",1112,1.7,7),
    ("eqdd",1121,1.7,7),
]

growth_factors_df = pd.DataFrame.from_records(arnau_growth_factors, columns=["smeft_label", "smeft_flavour", "growth_factor", "dim"])


# In[6]:


fix_labels_dict = {
    "ldud": "l~dudH~",
    "ldqq": "l~dqqH~",
    "lddd": "l~dddH",
    "eqdd": "e~qddH~",
}

def fix_label(label):
    maybe_result = fix_labels_dict.get(label)
    if maybe_result:
        return maybe_result
    
    label = label.lower()
    return label

growth_factors_df.smeft_label = growth_factors_df.smeft_label.map(lambda s: fix_label(s))
growth_factors_df.smeft_flavour = growth_factors_df.smeft_flavour.astype(int)
df.smeft_flavour = df.smeft_flavour.astype(int)


# In[7]:


growth_factors_df


# In[8]:


df_with_growth_factors = pd.merge(df, growth_factors_df, on=["smeft_label", "smeft_flavour"], suffixes=("_john", "_arnau"))


# In[9]:


# Keep only the dimension 6 and 7 smeft operators
df_with_growth_factors[df_with_growth_factors["dim_arnau"] >= 6]


# Now we want to scale each coefficient by the growth factor in the `lambda_limit`, but this needs to be accessed through the `smeft_op` with `sympy`.

# In[25]:


max_lambda_dict


# In[10]:


import sympy
import numpy as np
from tables import LAMBDA

# First scale the lambda limit
d6 = df_with_growth_factors["dim_arnau"] == 6
d7 = df_with_growth_factors["dim_arnau"] == 7

df_with_growth_factors.loc[d6, "scaled_lambda_limit_coeff_1"] = df_with_growth_factors[d6].lambda_limit_coeff_1 * np.sqrt(df_with_growth_factors[d6].growth_factor)
df_with_growth_factors.loc[d7, "scaled_lambda_limit_coeff_1"] = df_with_growth_factors[d7].lambda_limit_coeff_1 * np.cbrt(df_with_growth_factors[d7].growth_factor)

# For each operator, get the max (scaled) lambda limit
max_lambda_dict = df_with_growth_factors[["smeft_label", "smeft_flavour", "scaled_lambda_limit_coeff_1"]].groupby(["smeft_label", "smeft_flavour"]).max().to_dict()
max_lambda_dict = max_lambda_dict["scaled_lambda_limit_coeff_1"]

# Set `LAMBDA` to this value in `gamma_coeff_1` and then normalise to the rate associated with the experimental limit
def calc_bound_saturation(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x

    gamma = row.gamma.subs({row.smeft_op: row.growth_factor, LAMBDA: max_lambda_dict[(row.smeft_label, row.smeft_flavour)]})
    gamma_limit = 1.0 / value_in_inv_gev(row.lifetime_limit)

    ratio = gamma / gamma_limit
    return ratio

df_with_growth_factors["bound_saturation"] = df_with_growth_factors.apply(calc_bound_saturation, axis=1)
df_with_growth_factors["operator"] = df_with_growth_factors.apply(lambda row: row.smeft_label + "_" + str(row.smeft_flavour), axis=1)
df_with_growth_factors


# In[11]:


ordering = [
    "qqql",
    "qque",
    "duql",
    "duue",
    "l~dddH",
    "l~dqqH~",
    "l~dudH~",
]

def ordering_func(x: pd.Index) -> pd.Index:
    if isinstance(x[0], np.int64):
        return x
    return pd.Index([ordering.index(i) for i in x])

heatmap_df = pd.pivot_table(
    df_with_growth_factors,
    values='bound_saturation',
    index=['smeft_label', 'smeft_flavour'],
    columns=['process'], 
    aggfunc="max", 
    fill_value=0,
    ).sort_index(key=ordering_func)

np.array(heatmap_df, dtype=float)


# In[22]:


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

    return wrap_math("C_{" + replacement + "}" + rf"^{{{flavour}}}")

def plot_fingerprints(df: pd.DataFrame, savefig: bool = False) -> None:
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
        annot=True,
        #annot_kws={"size": 8},
        xticklabels=[pretty_process(proc) for proc in df.keys()],
        yticklabels=[pretty_label(label, flavour) for label, flavour in df.index],
        # cbar_kws={'label': 'Bound Saturation'}
    )

    # print(ax.texts) 
    # for t in ax.texts:
    #     t.set_text(t.get_text())
    
    # axes_subplot.set(title="")

    
    for label in ax.get_xticklabels():
        label.set_rotation(75)
        label.set_ha("right")

    for label in ax.get_yticklabels():
        label.set_rotation(15)
        label.set_ha("right")
        
        
    ax.yaxis.set_tick_params(labelsize=16)
    ax.xaxis.set_tick_params(labelsize=16)

    # ax.collections[0].colorbar.set_label("Bound Saturation")
    ax.figure.axes[-1].set_ylabel('Bound Saturation', size=15)
    
    ax.tick_params(axis="x")
    ax.tick_params(axis="y")

    if savefig: 
        snsfig = axes_subplot.get_figure()
        snsfig.savefig('/Users/johngargalionis/Desktop/correlations.pdf', bbox_inches="tight")
    
    return axes_subplot


# In[24]:


plot_fingerprints(heatmap_df, savefig=True)


# ## Loop-level heatmap

# In[ ]:


loop_level_records = get_loop_level_records()


# In[ ]:


df = pd.DataFrame.from_records(loop_level_records)


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




