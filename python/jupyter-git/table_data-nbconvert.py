#!/usr/bin/env python
# coding: utf-8

# # Data for tables in the paper

# Let's start with the latex matching expressions for the main table

# In[1]:


from limits import get_loop_level_records, get_tree_level_records
import pandas as pd


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
    header=["\#", "Operator", "$D$", r"$\Delta B$", r"$\Delta L$", "Matching", "$pqrs$", "$\Lambda > \#$", "Process"],
    na_rep="---",
    longtable=True,
    column_format="llcccllll",
    formatters={"latex": wrap_math, "DeltaB": wrap_math, "DeltaL": wrap_math, "fieldstring_label": wrap_math , "dimension": wrap_math, "process": wrap_math, "lambda_limit_coeff_1": tab_num},
    caption="The table displays our listing of the $|\Delta B| = 1$ operators. The matching expressions represent our estimate of the loop-level matching onto the LEFT in our SM-covariant formalism, discussed in the main text. Here, there is an implicit sum over all primed indices and $p,q,r,s$. The column labelled $pqrs$ represents the flavour of the SMEFT operator given in the matching expression that gives rise to the most stringent experimental limit. The implied limit on the scale underlying the operator is shown in the next column, and the process from which this limit is derived in the last. We separate those operators that generate proton decay only with loops from those that mediate it at tree level (operators 1--10).",
    label="tab:bviolating-operators",
    )
)


# In[1]:


import pandas as pd
from limits import derive_general_limits, derive_best_general_limits, derive_loop_limits, LAMBDA, print_general_limits


# In[2]:


decay_rates = []
# best_limits = derive_best_general_limits(decay_rates=decay_rates)
best_limits = derive_best_general_limits(decay_rates=decay_rates)

for decay_rate in decay_rates:
    decay_rate["process"] = "$" + decay_rate["process"] + "$"
    
# fieldstring_limits = derive_loop_limits(general_limits=best_limits)


# In[3]:


# 26/09/2023
print_general_limits(best_limits=best_limits)

