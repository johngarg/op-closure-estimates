#!/usr/bin/env python
# coding: utf-8

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




