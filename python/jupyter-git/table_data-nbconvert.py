#!/usr/bin/env python
# coding: utf-8

# # Data for tables in the paper

# In[ ]:


from limits import get_loop_level_records, get_tree_level_records
import pandas as pd


# ## Field string table

# Let's start with the latex matching expressions for the main table

# In[2]:


loop_level_records = get_loop_level_records()


# In[3]:


df = pd.DataFrame.from_records(loop_level_records)
df["fieldstring_label"] = df["fieldstring_label"].astype(int)
df.head()


# In[8]:


fieldstring_df = pd.read_csv("fieldstring_table_noflavour.csv")

# Go from B, L to \Delta B and \Delta L
fieldstring_df["fieldstring_label"] = fieldstring_df["fieldstring_label"].astype(int)
fieldstring_df["DeltaB"] = -fieldstring_df["B"]
fieldstring_df["DeltaL"] = -fieldstring_df["L"]

fieldstring_df[["fieldstring_label", "operator", "DeltaB", "DeltaL"]].head()


# In[9]:


raw_size = df.size

# overwrite dataframe to remove duplicates
df = df.drop_duplicates(keep="first")

without_duplicates = df.size
raw_size - without_duplicates


# In[14]:


wrap_math = lambda x: "$" + str(x) + "$"
tab_num = lambda x: "\\tabnum{" + str(x) + "}"
fieldstring_table_info = df[["fieldstring_label",  "fieldstring_flavour",  "latex", "smeft_label", "smeft_flavour", "lambda_limit_coeff_1", "process"]].sort_values(by=["fieldstring_label", "lambda_limit_coeff_1"], ascending=[True, False]).groupby(by="fieldstring_label", as_index=False).first()

print(fieldstring_df.merge(fieldstring_table_info, how="left", on="fieldstring_label").to_latex(
    index=False,
    columns=["fieldstring_label", "operator", "dimension", "DeltaB", "DeltaL", "latex", "smeft_flavour", "lambda_limit_coeff_1", "process"],
    header=["\#", "Operator", "$D$", r"$\Delta B$", r"$\Delta L$", "Matching", "$pqrs$", "$\Lambda~[\mathrm{GeV}]$", "Process"],
    na_rep="---",
    longtable=True,
    column_format="llcccllll",
    formatters={"latex": wrap_math, "DeltaB": wrap_math, "DeltaL": wrap_math, "fieldstring_label": wrap_math , "dimension": wrap_math, "process": wrap_math, "lambda_limit_coeff_1": tab_num},
    caption="The table displays our listing of the $|\Delta B| = 1$ operators. The matching expressions represent our estimate of the loop-level matching onto the LEFT in our SM-covariant formalism, discussed in the main text. Here, there is an implicit sum over all primed indices and $p,q,r,s$. The column labelled $pqrs$ represents the flavour of the SMEFT operator given in the matching expression that gives rise to the most stringent experimental limit. The implied limit on the scale underlying the operator is shown in the next column, and the process from which this limit is derived in the last. We separate those operators that generate proton decay only with loops from those that mediate it at tree level (operators 1--10).",
    label="tab:bviolating-operators",
    )
)


# ## Tree-level limits table

# In[17]:


tree_level_records = get_tree_level_records()


# In[18]:


df = pd.DataFrame.from_records(tree_level_records)


# In[87]:


test = {"a": 1, "b": 2}

test.get("c")


# In[99]:


import sympy

best_tree_level_limits = df.sort_values("lambda_limit_coeff_1", ascending=False).drop_duplicates(subset=["smeft_label", "smeft_flavour"], keep="first")

def typeset_left_op(label: str, flavour: str):
    sup, sub = label.split("_")
    return f"[C^{{{sup}}}_{{{sub}}}]_{{{flavour}}}"

def fmt_lambda_limit(limit, smeft_label: str, smeft_flavour: str):
    number, coeff_expr = limit.args
    coeff_expr_latex = sympy.latex(coeff_expr)
    coeff_expr_latex = coeff_expr_latex.replace("K_", "C_")

    # Replace the smeft labels to latex
    smeft_label_dict = {
        "l~dqqH~": r"\\bar{l}dqq\\tilde{H}",
        "e~qddH~": r"\\bar{e}qdd\\tilde{H}",
        "l~dudH~": r"\\bar{l}dud\\tilde{H}",
        "l~dddH": r"\\bar{l}dddH",
        "e~dddD": r"\\bar{e}dddD",
        "l~qdDd": r"\\bar{l}qdDd",

    }
    replacement = smeft_label_dict.get(smeft_label)

    clean_coeff_expr_latex = re.sub(pattern=r'(C_\{[^\}]+\})', repl=f"C^{{{replacement if replacement is not None else smeft_label}}}_{{{smeft_flavour}}}", string=coeff_expr_latex)
    tab_num = f"\\tabnumT{{{float(number)}}}"
    return tab_num + " \\cdot " + clean_coeff_expr_latex

best_tree_level_limits['left_coefficient'] = df.apply(lambda row: typeset_left_op(row["left_op"], row["left_flavour"]), axis=1)
best_tree_level_limits['lambda_limit_latex'] = df.apply(lambda row: fmt_lambda_limit(row["lambda_limit"], row["smeft_label"], row["smeft_flavour"]), axis=1)

cols = ['lambda_limit_latex', 'process', 'left_coefficient']

print(
    best_tree_level_limits.sort_values(by=["lambda_limit_coeff_1", "smeft_label", "smeft_flavour"], ascending=[False, False, True])[cols].to_latex(
        index=False,
        columns=cols,
        header=["Lower limit [GeV]", "Process", "LEFT coefficient"],
        na_rep="---",
        longtable=True,
        formatters={k: wrap_math for k in cols},
        caption="The table shows the lower limits on the UV scale $\Lambda$ underlying each SMEFT operator defined in section~\\ref{sec:smeft-left-tree-level-matching} in terms of the operator coefficient. These limits are derived by matching the SMEFT operator onto the LEFT operator shown at tree level and comparing the specific process shown to its current experimental bound.",
        label="tab:tree-level-limits",
    )
)


