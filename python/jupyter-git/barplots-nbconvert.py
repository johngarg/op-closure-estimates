#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.colors import LogNorm

#plt.style.use("/Users/johngargalionis/Dropbox/research/bviolation/ProtonDecayCalc/python/nord.mplstyle")
cmap = sns.cubehelix_palette(
    n_colors=9, start=0, rot=-0.2, gamma=0.7, hue=0.8, light=0.9, dark=0.1, as_cmap=True
)

sns.set_theme(style="whitegrid")

from limits import derive_general_limits, derive_loop_limits, LAMBDA

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",  
})


# In[2]:


decay_rates = []
best_limits = derive_general_limits(decay_rates=decay_rates)

for decay_rate in decay_rates:
    decay_rate["process"] = "$" + decay_rate["process"] + "$"
    
fieldstring_limits = derive_loop_limits(general_limits=best_limits)


# In[3]:


df = pd.DataFrame.from_records(decay_rates)


# In[4]:


df.sort_values("lambda_limit_coeff_1", ascending=False)


# In[5]:


arnau_limits = df.sort_values("lambda_limit_coeff_1", ascending=False).drop_duplicates(subset=["smeft_label", "smeft_flavour"], keep="first")
arnau_limits[['smeft_label', 'smeft_flavour', 'process', 'lambda_limit_coeff_1']].to_csv("~/Desktop/limits_for_arnau.csv")


# In[5]:


df = pd.DataFrame.from_records(decay_rates)
df = df.astype({'lambda_limit_coeff_1': 'float'})


# In[6]:


best_limits = df.sort_values("lambda_limit_coeff_1", ascending=False).drop_duplicates(subset="smeft_label", keep="first")
worst_limits = df.sort_values("lambda_limit_coeff_1").drop_duplicates(subset="smeft_label", keep="first")

rename_dict = {
    "lambda_limit_coeff_1": "Limit", 
    "smeft_label": "Operator", 
    "smeft_flavour": "Flavour", 
    "process": "Process"
}

best_limits = best_limits.rename(columns=rename_dict)
worst_limits = worst_limits.rename(columns=rename_dict)

best_limits_order = list(best_limits["Operator"])
worst_limits["sorter"] = [best_limits_order.index(i) for i in worst_limits["Operator"]]

worst_limits = worst_limits.sort_values("sorter")


# In[19]:


to_latex = {
    "qqql": "q^3l",
    "duql": "duql",
    "duue": "du^2e",
    "qque": "q^2ue",
    "l~dqqH~": "\\bar{l}dq^2\\tilde{H}",
    "l~dudH~": "\\bar{l}dud\\tilde{H}",
    "e~dqqH~": "\\bar{e}dq^2\\tilde{H}",
    "e~qddH~": "\\bar{e}qd^2\\tilde{H}",
    "l~dddH": "\\bar{l}d^3H",
    "luqqHHH": "luq^2H^3",
    "eqqqHHH": "eq^3H^3",
    "ddqlHH": "d^2qlH^2",
    
    "l~qdDd": "\\bar{l}qd^2 D",
    "e~dddD": "\\bar{e}d^3 D",
    "qqlqHHD": "lq^3 H^2 D",
    "qqedHHD": "eq^2dH^2 D",
}

PROCESS_TO_LATEX = {
    "p->K0e+": r"p \to K^{0} e^{+}",
    "p->K0mu+": r"p \to K^{0} \mu^{+}",
    "p->pi0e+": r"p \to \pi^{0} e^{+}",
    "p->pi+nu": r"p \to \pi^{+} \nu",
    "p->eta0e+": r"p \to \eta^{0} e^{+}",
    "p->K+nu": r"p \to K^{+} \nu",
    "n->pi0nu": r"n \to \pi^{0} \nu",
    "n->pi+e-": r"n \to \pi^{+} e^{-}",
    "n->pi-e+": r"n \to \pi^{-} e^{+}",
    "n->eta0nu": r"n \to \eta^{0} \nu",
    "n->K+e-": r"n \to K^{+} e^{-}",
    "n->K0nu": r"n \to K^{0} \nu",
}


def typeset_operator_label(label: str) -> str:
    return "$" + label + "$"


# In[31]:


worst_limits


# In[24]:


worst_limits[worst_limits.Operator == "qqedHHD"]


# In[25]:


best_limits[best_limits.Operator == "qqedHHD"]


# In[76]:


sns.set_theme(style="whitegrid")

## Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# Plot the total crashes
sns.set_color_codes("pastel")
sns_plot=sns.barplot(x="Limit", y="Operator", data=best_limits, label="Best tree-level limit", color="b", axes=ax)

sns.set_color_codes("muted")
sns.barplot(x="Limit", y="Operator", data=worst_limits, color="r", axes=ax, label="Worst tree-level limit")

ax.set_xscale("log")

sns_plot.set_yticklabels([f"${to_latex[op]}$" for op in best_limits.Operator])
#sns_plot.set_xticklabels(["", "", "$10^3$", "$10^7$", "$10^{11}$", "$10^{15}$", "", ""])

lower_limit = 100
ax.set(xlim=(lower_limit, 10e+15), ylabel="")

ax.set_xlabel("Lower limit on scale [GeV]", fontsize=18)
sns.despine(left=True, bottom=True)



for i, (lim, flav, proc) in enumerate(zip(best_limits.Limit, best_limits.Flavour, best_limits.Process)):
    ax.text(lim*2, i, "$"+proc+"$", fontsize=14)
    ax.text(lim*2, i+0.35, "$"+flav+"$", fontsize=12)
    
for i, (lim, flav, proc) in enumerate(zip(worst_limits.Limit, worst_limits.Flavour, worst_limits.Process)):
    ax.text(lower_limit*2, i, "$"+proc+"$", fontsize=14, color="white")
    ax.text(lower_limit*2, i+0.35, "$"+flav+"$", fontsize=12, color="white")

#ax.bar_label(ax.containers[0], labels=[typeset_operator_label(i) for i in best_limits.Process], padding=3, fontsize=16)
#ax.bar_label(ax.containers[1], labels=[typeset_operator_label(i) for i in worst_limits.Process], fontsize=16, label_type='center')

ax.set_title('Tree-level limits on SMEFT operators', fontsize=16)

ax.yaxis.set_tick_params(labelsize=16)
ax.xaxis.set_tick_params(labelsize=16)

#ax.get_legend().remove()

snsfig = sns_plot.get_figure()
snsfig.savefig('/Users/johngargalionis/Desktop/tree-level-limits-2.pdf', bbox_inches="tight")


# In[10]:


def wrap_math(math: str) -> str:
    return r"$" + math + r"$"


# In[11]:


fsdf = pd.DataFrame.from_records(fieldstring_limits)
fsdf = fsdf.astype({'lambda_limit_coeff_1': 'float'})


# In[12]:


fsdf["gamma_fieldstring_coeff_1_lam_100"] = [val.subs({LAMBDA: 100}) for val in fsdf.gamma_fieldstring_coeff_1]


# In[13]:


fsdf[fsdf["fieldstring_label"] == "20"].sort_values("gamma_fieldstring_coeff_1_lam_100", ascending=False)


# In[14]:


fs_best_limits = fsdf.sort_values("lambda_limit_coeff_1", ascending=False).drop_duplicates(subset="fieldstring_label", keep="first")
fs_worst_limits = fsdf.sort_values("lambda_limit_coeff_1").drop_duplicates(subset="fieldstring_label", keep="first")

rename_dict = {
    "lambda_limit_coeff_1": "Limit", 
    "fieldstring_label": "Operator", 
    "fieldstring_flavour": "Flavour", 
    "process": "Process"
}

fs_best_limits = fs_best_limits.rename(columns=rename_dict)
fs_worst_limits = fs_worst_limits.rename(columns=rename_dict)

fs_best_limits_order = list(fs_best_limits["Operator"])
fs_worst_limits["sorter"] = [fs_best_limits_order.index(i) for i in fs_worst_limits["Operator"]]

fs_worst_limits = fs_worst_limits.sort_values("sorter")


# In[15]:


sns.set_theme(style="whitegrid")

## Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# Plot the total crashes
sns.set_color_codes("pastel")
sns_plot=sns.barplot(x="Limit", y="Operator", data=fs_best_limits, label="Best tree-level limit", color="b", axes=ax)

#sns.set_color_codes("muted")
#sns.barplot(x="Limit", y="Operator", data=fs_worst_limits, color="r", axes=ax, label="Worst tree-level limit")

ax.set_xscale("log")

sns_plot.set_yticklabels([f"${op}$" for op in fs_best_limits.Operator])

#for i in ax.containers:
#    ax.bar_label(i,)


# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(10e+0, 10e+17), ylabel="")

ax.set_xlabel("Lower limit on scale [GeV]", fontsize=18)
sns.despine(left=True, bottom=True)

#for con in ax.containers:
#       ax.bar_label(con,)


for i, (lim, flav) in enumerate(zip(fs_best_limits.Limit, fs_best_limits.Flavour)):
    ax.text(lim*2, i+0.35, "$"+flav+"$", fontsize=12)
    
#for i, (lim, flav) in enumerate(zip(fs_worst_limits.Limit, fs_worst_limits.Flavour)):
#    ax.text(lim/40, i+0.35, "$"+flav+"$", fontsize=12)

ax.bar_label(ax.containers[0], labels=[typeset_operator_label(i) for i in fs_best_limits.Process], padding=3, fontsize=16)
#ax.bar_label(ax.containers[1], labels=[typeset_operator_label(i) for i in worst_limits.Flavour], padding=3, fontsize=16)

ax.set_title('Limits on $\\Delta B = \\Delta L = -1$ dimension-8 operators', fontsize=16)

ax.yaxis.set_tick_params(labelsize=16)
ax.xaxis.set_tick_params(labelsize=16)

ax.legend(fontsize=16)
ax.get_legend().remove()

snsfig = sns_plot.get_figure()
snsfig.savefig('/Users/johngargalionis/Desktop/loop-level-limits.pdf', bbox_inches="tight")


# In[ ]:



