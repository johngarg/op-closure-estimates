#!/usr/bin/env python
# coding: utf-8

# In[1]:


from limits import get_loop_level_records, get_tree_level_records
import pandas as pd
import numpy as np


# ## Tree-level barplots

# In[ ]:


tree_level_records = get_tree_level_records()


# ## Loop-level barplots

# In[2]:


loop_level_records = get_loop_level_records()


# In[6]:


df = pd.DataFrame.from_records(loop_level_records)
df = df.drop_duplicates()

df.lambda_limit_coeff_1 = df.lambda_limit_coeff_1.astype(float)


# Perhaps the best thing to do is take different smeft operators rather than field-string operators, since the plot with the field-string operators looks completely red for the d=9 case.

# In[8]:


#best_limits_ = df[["fieldstring_label", "fieldstring_flavour", "smeft_label", "smeft_flavour", "lambda_limit_coeff_1", "process"]].sort_values("lambda_limit_coeff_1", ascending=False).groupby(by=["fieldstring_label", "smeft_label"], as_index=True).first()

best_limits_ = df[["fieldstring_label", "fieldstring_flavour", "smeft_label", "smeft_flavour", "lambda_limit_coeff_1", "process"]].groupby(by=["fieldstring_label", "smeft_label"], as_index=False).apply(lambda x: x.nlargest(1, "lambda_limit_coeff_1")).reset_index(drop=True)

# There are no cases where there are groups of unit length apparently
# best_limits.groupby("fieldstring_label").apply(lambda x: x if len(x) < 2 else None).empty

#best_limits_different_ops = best_limits_.reset_index(inplace=False).sort_values("lambda_limit_coeff_1", ascending=False).groupby("fieldstring_label").head(2)
best_limits_different_ops = best_limits_.groupby("fieldstring_label").apply(lambda x: x.nlargest(2, "lambda_limit_coeff_1"))

# Only operator 12 has one limit, add it in by hand!
test = df[["fieldstring_label", "fieldstring_flavour", "smeft_label", "smeft_flavour", "lambda_limit_coeff_1", "process"]].sort_values("lambda_limit_coeff_1", ascending=False)
new_row = test[(test.fieldstring_label == "12") & (test.smeft_flavour == "1121")].iloc[0].to_dict()
best_limits = pd.concat([best_limits_different_ops, pd.DataFrame([new_row])], ignore_index=True).sort_values("lambda_limit_coeff_1", ascending=False)


# In[11]:


first_best_limits = best_limits[~best_limits.duplicated(subset=["fieldstring_label"])]
second_best_limits = best_limits[best_limits.duplicated(subset=["fieldstring_label"])]

assert len(first_best_limits) == len(second_best_limits)


# In[12]:


rename_dict = {
    "lambda_limit_coeff_1": "Limit", 
    "fieldstring_label": "Operator", 
    "fieldstring_flavour": "Flavour", 
    "process": "Process"
}

first_best_limits = first_best_limits.rename(columns=rename_dict)
second_best_limits = second_best_limits.rename(columns=rename_dict)

first_best_limits_order = list(first_best_limits["Operator"])
second_best_limits["sorter"] = [first_best_limits_order.index(i) for i in second_best_limits["Operator"]]

second_best_limits = second_best_limits.sort_values("sorter")


# In[13]:


to_latex = {
    "qqql": "qqql",
    "duql": "duql",
    "duue": "duue",
    "qque": "qque",
    "l~dqqH~": "\\bar{l}dqq\\tilde{H}",
    "l~dudH~": "\\bar{l}dud\\tilde{H}",
    "e~dqqH~": "\\bar{e}dqq\\tilde{H}",
    "e~qddH~": "\\bar{e}qdq\\tilde{H}",
    "l~dddH": "\\bar{l}dddH",
    "luqqHHH": "luqqHHH",
    "eqqqHHH": "eqqqHHH",
    "ddqlHH": "ddqlHH",
    "l~qdDd": "\\bar{l}qddD",
    "e~dddD": "\\bar{e}dddD",
    "qqlqHHD": "lqqqHHD",
    "qqedHHD": "eqqdHH D",
    "udqlHHD": "udqlHHD",
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


# In[14]:


fb_d8_mask = first_best_limits.Operator.astype(int) < 25
fb_d9_mask = first_best_limits.Operator.astype(int) >= 25
sb_d8_mask = second_best_limits.Operator.astype(int) < 25
sb_d9_mask = second_best_limits.Operator.astype(int) >= 25


# In[15]:


import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.colors import LogNorm

cmap = sns.cubehelix_palette(
    n_colors=9, start=0, rot=-0.2, gamma=0.7, hue=0.8, light=0.9, dark=0.1, as_cmap=True
)

sns.set_theme(style="whitegrid")

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",  
})


# In[16]:


## Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

best = first_best_limits[fb_d8_mask]
second = second_best_limits[sb_d8_mask]

# Plot the total crashes
sns.set_color_codes("pastel")
sns_plot=sns.barplot(x="Limit", y="Operator", data=best, label="Best loop-level limit", color="b", axes=ax)

sns.set_color_codes("muted")
sns.barplot(x="Limit", y="Operator", data=second, color="r", axes=ax, label="Second best loop-level limit")

ax.set_xscale("log")

sns_plot.set_yticklabels([f"${op}$" for op in best.Operator])

lower_limit = 100
ax.set(xlim=(lower_limit, 10e+17), ylabel="")

ax.set_xlabel("Lower limit on scale [GeV]", fontsize=16)
sns.despine(left=True, bottom=True)



for i, (lim, flav, proc, smeft_label, smeft_flavour) in enumerate(zip(best.Limit, best.Flavour, best.Process, best.smeft_label, best.smeft_flavour)):
    ax.text(lim*2, i-0.02, "$"+proc+"$", fontsize=14)
    ax.text(lim*2, i+0.29, "$"+flav+"$", fontsize=12)
    string_ = "$[\\mathcal{O}_{" + to_latex[smeft_label] + "}]_{" + smeft_flavour + "}$"
    ax.text(lim*50, i+0.29, string_)
    
for i, (lim, flav, proc, smeft_label, smeft_flavour) in enumerate(zip(second.Limit, second.Flavour, second.Process, second.smeft_label, second.smeft_flavour)):
    ax.text(lower_limit*2, i-0.02, "$"+proc+"$", fontsize=14, color="white")
    ax.text(lower_limit*2, i+0.29, "$"+flav+"$", fontsize=12, color="white")
    string_ = "$[\\mathcal{O}_{" + to_latex[smeft_label] + "}]_{" + smeft_flavour + "}$"
    ax.text(lower_limit*50, i+0.29, string_, color="white")

#ax.bar_label(ax.containers[0], labels=[typeset_operator_label(i) for i in best_limits.Process], padding=3, fontsize=16)
#ax.bar_label(ax.containers[1], labels=[typeset_operator_label(i) for i in worst_limits.Process], fontsize=16, label_type='center')

ax.set_title('Loop-level limits on $d=8$ operators', fontsize=16)

ax.yaxis.set_tick_params(labelsize=16)
ax.xaxis.set_tick_params(labelsize=16)

#ax.get_legend().remove()

snsfig = sns_plot.get_figure()
snsfig.savefig('/Users/johngargalionis/Desktop/dim_8_loop_level_limits.pdf', bbox_inches="tight")


# In[11]:


## Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

best = first_best_limits[fb_d9_mask]
second = second_best_limits[sb_d9_mask]

# Plot the total crashes
sns.set_color_codes("pastel")
sns_plot=sns.barplot(x="Limit", y="Operator", data=best, label="Best loop-level limit", color="b", axes=ax)

sns.set_color_codes("muted")
sns.barplot(x="Limit", y="Operator", data=second, color="r", axes=ax, label="Second best loop-level limit")

ax.set_xscale("log")

sns_plot.set_yticklabels([f"${op}$" for op in best.Operator])

lower_limit = 1
ax.set(xlim=(lower_limit, 10e+12), ylabel="")

ax.set_xlabel("Lower limit on scale [GeV]", fontsize=16)
sns.despine(left=True, bottom=True)

for i, (lim, flav, proc, smeft_label, smeft_flavour) in enumerate(zip(best.Limit, best.Flavour, best.Process, best.smeft_label, best.smeft_flavour)):
    ax.text(lim*2, i-0.05, "$"+proc+"$", fontsize=13)
    ax.text(lim*2, i+0.24, "$"+flav+"$", fontsize=11)
    string_ = "$[\\mathcal{O}_{" + to_latex[smeft_label] + "}]_{" + smeft_flavour + "}$"
    ax.text(lim*50, i+0.24, string_)
    
for i, (lim, flav, proc, smeft_label, smeft_flavour) in enumerate(zip(second.Limit, second.Flavour, second.Process, second.smeft_label, second.smeft_flavour)):
    ax.text(lower_limit*2, i-0.05, "$"+proc+"$", fontsize=13, color="white")
    ax.text(lower_limit*2, i+0.24, "$"+flav+"$", fontsize=11, color="white")
    string_ = "$[\\mathcal{O}_{" + to_latex[smeft_label] + "}]_{" + smeft_flavour + "}$"
    ax.text(lower_limit*50, i+0.24, string_, color="white")

#ax.bar_label(ax.containers[0], labels=[typeset_operator_label(i) for i in best_limits.Process], padding=3, fontsize=16)
#ax.bar_label(ax.containers[1], labels=[typeset_operator_label(i) for i in worst_limits.Process], fontsize=16, label_type='center')

ax.set_title('Loop-level limits on $d=9$ operators', fontsize=16)

ax.yaxis.set_tick_params(labelsize=16)
ax.xaxis.set_tick_params(labelsize=16)

#ax.get_legend().remove()

snsfig = sns_plot.get_figure()
snsfig.savefig('/Users/johngargalionis/Desktop/dim_9_loop_level_limits.pdf', bbox_inches="tight")


# ## Old barplots

# In[ ]:


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


# In[13]:


# Here I want to check how close the p->e+K0 contribution is for duql,2111 since Arnau finds this to give a better limit

arnau = df.sort_values("lambda_limit_coeff_1", ascending=False)
arnau[(arnau.smeft_label == "duql")]

# 719580238945908.
# 758179010856717. 

758179010856717. / 719580238945908.


# In[5]:


arnau_limits = df.sort_values("lambda_limit_coeff_1", ascending=False).drop_duplicates(subset=["smeft_label", "smeft_flavour"], keep="first")
arnau_limits[['smeft_label', 'smeft_flavour', 'process', 'lambda_limit_coeff_1']].to_csv("~/Desktop/updated3_limits_for_arnau.csv")


# In[6]:


df = pd.DataFrame.from_records(decay_rates)
df = df.astype({'lambda_limit_coeff_1': 'float'})


# In[7]:


best_limits = df.sort_values("lambda_limit_coeff_1", ascending=False).drop_duplicates(subset="smeft_label", keep="first")
worst_limits = df.sort_values("lambda_limit_coeff_1", ascending=True).drop_duplicates(subset="smeft_label", keep="first")

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


# In[8]:


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


# In[9]:


df[df.smeft_label == "ddqlHH"]


# In[10]:


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
snsfig.savefig('/Users/johngargalionis/Desktop/tree-level-limits-4.pdf', bbox_inches="tight")


# In[11]:


def wrap_math(math: str) -> str:
    return r"$" + math + r"$"


# In[12]:


fsdf = pd.DataFrame.from_records(fieldstring_limits)
fsdf = fsdf.astype({'lambda_limit_coeff_1': 'float'})


# In[29]:


fsdf["fieldstring_label_int"] = fsdf["fieldstring_label"]
fsdf = fsdf.astype({'fieldstring_label_int': 'int'})


# In[16]:


fsdf["gamma_fieldstring_coeff_1_lam_100"] = [val.subs({LAMBDA: 100}) for val in fsdf.gamma_fieldstring_coeff_1]


# In[17]:


fsdf[fsdf["fieldstring_label"] == "20"].sort_values("gamma_fieldstring_coeff_1_lam_100", ascending=False)


# In[31]:


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


# In[38]:


best_d8 = fs_best_limits[fs_best_limits.fieldstring_label_int < 25]
best_d9 = fs_best_limits[fs_best_limits.fieldstring_label_int >= 25] 


# In[46]:


def plot_loop_level_barplot(fs_best_limits):
    sns.set_theme(style="whitegrid")

    ## Initialize the matplotlib figure
    f, ax = plt.subplots(figsize=(6, 17))

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

    ax.set_title('Limits on dimension-9 operators', fontsize=16)

    ax.yaxis.set_tick_params(labelsize=16)
    ax.xaxis.set_tick_params(labelsize=16)

    ax.legend(fontsize=16)
    ax.get_legend().remove()

    snsfig = sns_plot.get_figure()
    snsfig.savefig('/Users/johngargalionis/Desktop/loop-level-limits-d9.pdf', bbox_inches="tight")


# In[47]:


plot_loop_level_barplot(best_d9)


# In[ ]:




