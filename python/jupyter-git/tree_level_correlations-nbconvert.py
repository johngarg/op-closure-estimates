#!/usr/bin/env python
# coding: utf-8

# In[1]:


from limits import get_loop_level_records, get_tree_level_records
import pandas as pd


# In[2]:


from rates import * 


# ## Tree-level correlations

# In[3]:


tree_level_records = get_tree_level_records()


# In[4]:


df = pd.DataFrame.from_records(tree_level_records)


# Here you want to implement the decay rates using the expressions from Arnau

# In[5]:


coeffs = defaultdict(lambda: 0)
coeffs[("S^LR_ddd", "1211")] = 1
# gamma_BL2_neK(coeffs=coeffs, lam=1000.)

lam = 10
0.254328 * (lam)**(-4) * (Abs(((-0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs[('S^LR_ddd', '1211')])) )**(2)


# In[6]:


from collections import defaultdict
import sympy
import numpy as np

from tables import LAMBDA
from limits import VEV
from constants import VEV_VAL

rates_func_dict = {
    "n \\to K^{+} e^{-}": {2: gamma_BL2_neK},
    "n \\to K^{0} \\nu": {0: gamma_BL0_nnuK, 2: gamma_BL2_nnuK},
    "n \\to \\eta^{0} \\nu": {0: gamma_BL0_nnueta, 2: gamma_BL2_nnueta},
    "n \\to \\pi^{-} e^{+}": {0: gamma_BL0_nepi},
    "n \\to \\pi^{0} \\nu": {0: gamma_BL0_nnupi, 2: gamma_BL2_nnupi},
    "p \\to K^{+} \\nu": {0: gamma_BL0_pnuK, 2: gamma_BL2_pnuK},
    "p \\to K^{0} e^{+}": {0: gamma_BL0_peK},
    "p \\to \\eta^{0} e^{+}": {0: gamma_BL0_peeta},
    "p \\to \\pi^{+} \\nu": {0: gamma_BL0_pnupi, 2: gamma_BL2_pnupi},
    "p \\to \\pi^{0} e^{+}": {0: gamma_BL0_pepi},
}

def BminusL(operator: str):
    if operator in {"S,LL_udd", "S,LL_duu", "S,LR_duu", "S,RL_duu", "S,RL_dud", "S,RL_ddu", "S,RR_duu"}:
        return 0
    return 2


def calc_indirect_decay_rate(row):
    if row.process not in rates_func_dict:
        return 0.0

    rate_func = rates_func_dict[row.process][BminusL(row.left_op)]
    coeffs = defaultdict(lambda: 0)
    coeffs[(row.left_op, row.left_flavour)] = row.smeft_op_expr.subs({VEV: VEV_VAL})
    # Symbolic rate to solve for lambda
    rate = rate_func(coeffs=coeffs, lam=LAMBDA)
    return rate

def calc_indirect_limit(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x
    gamma_limit = 1.0 / value_in_inv_gev(row.lifetime_limit)

    rate = calc_indirect_decay_rate(row)
    if rate == 0:
        return np.nan
    lambda_limit = sympy.solve(gamma_limit - rate, LAMBDA)
    return lambda_limit[-1]

def calc_indirect_limit_coeff_1(row):
    limit = calc_indirect_limit(row)
    if isinstance(limit, float):
        return limit
    return limit.subs({row.smeft_op: 1.0})


# In[7]:


df["gamma_indirect"] = df.apply(calc_indirect_decay_rate, axis=1)
df["lambda_limit_indirect"] = df.apply(calc_indirect_limit, axis=1)
df["lambda_limit_coeff_1_indirect"] = df.apply(calc_indirect_limit_coeff_1, axis=1)


# You need to scale the tree-level coefficients that you have with the factors from Arnau.

# In[8]:


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


# In[9]:


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


# In[10]:


growth_factors_df


# In[11]:


growth_factors_df.loc[4,"smeft_flavour"] = 1121
growth_factors_df.loc[9,"smeft_flavour"] = 1211
growth_factors_df.loc[18,"smeft_flavour"] = 1112


# In[12]:


df_with_growth_factors = pd.merge(df, growth_factors_df, on=["smeft_label", "smeft_flavour"], suffixes=("_john", "_arnau"))


# In[13]:


df[(df.smeft_label == "qque") & (df.smeft_flavour == 1211)]


# In[14]:


# Keep only the dimension 6 and 7 smeft operators
df_with_growth_factors[df_with_growth_factors["dim_arnau"] >= 6]


# In[15]:


df_with_growth_factors[df_with_growth_factors.smeft_label == "l~dqqH~"]


# Now we want to scale each coefficient by the growth factor in the `lambda_limit`, but this needs to be accessed through the `smeft_op` with `sympy`.

# In[16]:


# First scale the lambda limit
d6 = df_with_growth_factors["dim_arnau"] == 6
d7 = df_with_growth_factors["dim_arnau"] == 7

df_with_growth_factors.loc[d6, "scaled_lambda_limit_coeff_1_indirect"] = df_with_growth_factors[d6].lambda_limit_coeff_1_indirect * np.sqrt(df_with_growth_factors[d6].growth_factor)
df_with_growth_factors.loc[d7, "scaled_lambda_limit_coeff_1_indirect"] = df_with_growth_factors[d7].lambda_limit_coeff_1_indirect * np.cbrt(df_with_growth_factors[d7].growth_factor)

# For each operator, get the max (scaled) lambda limit
max_lambda_dict = df_with_growth_factors[["smeft_label", "smeft_flavour", "scaled_lambda_limit_coeff_1_indirect"]].groupby(["smeft_label", "smeft_flavour"]).max().to_dict()
max_lambda_dict = max_lambda_dict["scaled_lambda_limit_coeff_1_indirect"]


# In[17]:


max_lambda_dict


# In[70]:


# Set `LAMBDA` to this value in `gamma_coeff_1` and then normalise to the rate associated with the experimental limit
def calc_bound_saturation(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x

    gamma = row.gamma_indirect.subs({row.smeft_op: row.growth_factor, LAMBDA: max_lambda_dict[(row.smeft_label, row.smeft_flavour)]})
    gamma_limit = 1.0 / value_in_inv_gev(row.lifetime_limit)

    ratio = gamma / gamma_limit
    return ratio

def calc_exp_ratio(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x

    gamma = row.gamma_indirect.subs({row.smeft_op: row.growth_factor, LAMBDA: 1.})
    gamma_limit = 1.0 / value_in_inv_gev(row.lifetime_limit)

    ratio = gamma / gamma_limit
    return ratio

df_with_growth_factors["bound_saturation"] = df_with_growth_factors.apply(calc_bound_saturation, axis=1)
df_with_growth_factors["operator"] = df_with_growth_factors.apply(lambda row: row.smeft_label + "_" + str(row.smeft_flavour), axis=1)
df_with_growth_factors


# In[83]:


df_with_growth_factors["exp_ratio"] = df_with_growth_factors.apply(calc_exp_ratio, axis=1)
max_ratio_dict = df_with_growth_factors[["smeft_label", "smeft_flavour", "exp_ratio"]].groupby(by=["smeft_label", "smeft_flavour"]).max().to_dict()["exp_ratio"]

def calc_bound_saturation_michael(row):
    return row.exp_ratio / max_ratio_dict[(row.smeft_label, row.smeft_flavour)]

df_with_growth_factors["bound_saturation_michael"] = df_with_growth_factors.apply(calc_bound_saturation_michael, axis=1)

df_with_growth_factors[["smeft_label", "smeft_flavour", "bound_saturation", "bound_saturation_michael"]]


# In[22]:


ordering = [
    "qqql",
    "qque",
    "duql",
    "duue",
    "l~dddH",
    "l~dqqH~",
    "l~dudH~",
    "e~qddH~",
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


# In[30]:


heatmap_df


# In[94]:


data = np.array(heatmap_df, dtype=float)

def latex_format(value):
    if 0 < abs(value) < 9e-3:
        base, exp = "{:.0e}".format(value).replace('e-0', 'e-').split("e")
        return fr"${base} \cdot 10^{{{exp}}}$"
    else:
        return fr"$ {value:.2f} $"
    
formatted_labels = np.vectorize(latex_format)(data).astype(str)
formatted_labels


# In[95]:


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

    return wrap_math("\\mathcal{O}_{" + replacement + rf",{{{flavour}}}" + "}")

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
        #annot=True,
        annot=formatted_labels,
        fmt="",
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
    ax.figure.axes[-1].tick_params(labelsize=14)
    
    ax.tick_params(axis="x")
    ax.tick_params(axis="y")

    if savefig: 
        snsfig = axes_subplot.get_figure()
        snsfig.savefig('/Users/johngargalionis/Desktop/correlations.pdf', bbox_inches="tight")
    
    return axes_subplot


# In[96]:


plot_fingerprints(heatmap_df, savefig=True)


# In[ ]:




