#!/usr/bin/env python
# coding: utf-8

# In[1]:


from limits import get_loop_level_records, get_tree_level_records
import pandas as pd


# # UV particles results table

# In[2]:


loop_level_records = get_loop_level_records()


# In[132]:


df = pd.DataFrame.from_records(loop_level_records)
df["fieldstring_label"] = df["fieldstring_label"].astype(int)

def is_muon_mode(row):
    return int(row.smeft_flavour[lepton_index(row)]) == 2

def lepton_index(row):
    try:
        return row.smeft_label.index("l")
    except:
        return row.smeft_label.index("e")
    
df["is_muon"] = df.apply(is_muon_mode, axis=1)

# Keep only future results on non-muon modes from Hyper-K
df = df[(df.is_future) & (~df.is_muon) & (df.lifetime_limit_ref.str.startswith("Hyper-K"))]

df.head()


# In[133]:


operators_from_arnau = {
"scalars": {
 "\\omega_{1}": ["1 p(qr)s", "2 p(qr)s", "3", "4"],
 "\\zeta": ["1 p[qr]s"],
 "\\omega_{4}": ["3 p[qr]s"],
 "\\Xi_{1}": ["30 (pq)r[st]u", "31 (pq)rs[tu]"],
 "\\mathcal{S}_{1}": ["28 [pq]rstu", "30 [pq]r[st]u", "31 [pq]rs[tu]"],
 "\\mathcal{S}_{2}": ["25 [pq]rs[tu]"],
 "\\Pi_{1}": ["5 pq[rs]", "8", "10"],
 "\\Pi_{7}": ["9 pq[rs]", "10 pq[rs]"],
 "\\mathcal{S}": ["18", "22", "23", "24"],
 "\\varphi": ["28", "29 pqrs[tu]", "30", "32", "35", "36", "40", "41", "42", "45", "46", "47 pq[rs]", "49 pqrs[tu]", "50"],
 "\\omega_{2}": ["5 pq[rs]", "9 pq[rs]", "10 pq[rs]"],
 "\\Xi": ["18", "22 p(qr)s", "24"],
 "\\Theta_{1}": ["45 p(qr)s"],
 "\\Theta_{3}": ["26", "37 p[qr]s"],
 "\\Omega_{1}": ["29 p[qr]s[tu]", "33 pqrs[tu]", "40 pq[rs]tu", "41", "42", "50"],
 "\\Omega_{2}": ["27 p[qr](st)u", "29 pqrs(tu)", "32 pqe(st)u", "33 pqrs(tu)", "39 pqrs(tu)", "41 pqrs(tu)", "42 pqrs(tu)", "50 pqrs(tu)"],
 "\\Upsilon": ["40 pq(rs)tu", "42 p(qr)stu"],
 "\\Phi": ["29", "32", "39", "40", "41", "42", "50"],
 }
}


# ## Construct new dataframe

# You want to check whether the flavours you have are allowed by whatever antisymmetry is present in the operator

# In[134]:


def bracket_indices(s: str) -> tuple[bool, tuple[tuple[int, int], ...]]:
    """Returns a tuple (bool, ((index, index), ...)) showing whether 
       any indices are antisymmetric and the indices of those indices
       
    """
    indices = []
    bracket_count = 0
    for i in range(len(s)):
        if s[i] in {"(", ")"}:
            bracket_count += 1
        if s[i] == '[':
            bracket_count += 1
            start = i - bracket_count + 1
        elif s[i] == ']':
            bracket_count += 1
            end = i - bracket_count
            indices.append((start, end))
    return (len(indices) > 0, tuple(indices))

# Testing the function
assert(bracket_indices("pqrs[tu]")) == (True, ((4, 5),))
assert(bracket_indices("pqrs")) == (False, ())
assert(bracket_indices("[pq]rs[tu]")) == (True, ((0, 1), (4, 5)))
assert(bracket_indices("(pq)rstu")) == (False, ())
assert(bracket_indices("(pq)r[st]u")) == (True, ((3, 4),))
assert(bracket_indices("[pq]rs[tu]")) == (True, ((0, 1), (4, 5)))


# In[135]:


class operator:
    def __init__(self, data: str):
        self.label, flavour_indices = data.split(" ")
        _, self.antisymmetric_indices = bracket_indices(flavour_indices)

assert bool(operator("1 p[qr]s").antisymmetric_indices)
assert not bool(operator("1 pqrs").antisymmetric_indices)


# In[300]:


import pandas as pd
import numpy as np

particle_operator_mapping = {
    # scalars
 "\\omega_{1}": ["1 p(qr)s", "2 p(qr)s", "3", "4"],
 "\\zeta": ["1 p[qr]s"],
 "\\omega_{4}": ["3 p[qr]s"],
 "\\Xi_{1}": ["30 (pq)r[st]u", "31 (pq)rs[tu]"],
 "\\mathcal{S}_{1}": ["28 [pq]rstu", "30 [pq]r[st]u", "31 [pq]rs[tu]"],
 "\\mathcal{S}_{2}": ["25 [pq]rs[tu]"],
 "\\Pi_{1}": ["5 pq[rs]", "8", "10"],
 "\\Pi_{7}": ["9 pq[rs]", "10 pq[rs]"],
 "\\mathcal{S}": ["18", "22", "23", "24"],
 "\\varphi": ["28", "29 pqrs[tu]", "30", "32", "35", "36", "40", "41", "42", "45", "46", "47 pq[rs]", "49 pqrs[tu]", "50"],
 "\\omega_{2}": ["5 pq[rs]", "9 pq[rs]", "10 pq[rs]"],
 "\\Xi": ["18", "22 p(qr)s", "24"],
 "\\Theta_{1}": ["45 p(qr)s"],
 "\\Theta_{3}": ["26", "37 p[qr]s"],
 "\\Omega_{1}": ["29 p[qr]s[tu]", "33 pqrs[tu]", "40 pq[rs]tu", "41", "42", "50"],
 "\\Omega_{2}": ["27 p[qr](st)u", "29 pqrs(tu)", "32 pqe(st)u", "33 pqrs(tu)", "39 pqrs(tu)", "41 pqrs(tu)", "42 pqrs(tu)", "50 pqrs(tu)"],
 "\\Upsilon": ["40 pq(rs)tu", "42 p(qr)stu"],
 "\\Phi": ["29", "32", "39", "40", "41", "42", "50"],
    
    # vectors
 "N": ["8 p(qr)s", "10"],
 "\\Sigma": ["8 p[qr]s"],
 "\\Sigma_{1}": ["14 pq[rs]", "18", "19 p[qr]s", "22", "24"],
 "\\Delta_{1}": ["9 pq[rs]"],
 "E": ["5"],
 "\\Delta_{2}": ["14 pq[rs]", "17 pq[rs]", "22", "23"],
 "U": ["11", "20 pq(rs)", "21"],
 "D": ["8", "9 pq[rs]"],
 "Q_{1}": ["5", "10"],
 "Q_{5}": ["8", "9", "10"],
 "Q_{7}": ["12 pq[rs]", "21", "22", "23", "24"],
 "T_{1}": ["8"],
 "T_{2}": ["11", "15", "16", "18", "20", "22", "24"],

    # vectors
 "\\mathcal{U}_{2}": ["8", "9"],
 "\\mathcal{X}": ["8"],
 "\\mathcal{L}_{3}": ["35", "49"],
 "\\mathcal{Q}_{5}": ["2", "4"],
 "\\mathcal{Q}_{1}": ["4"],
 "\\mathcal{U}_{5}": ["33"],
 "\\mathcal{Y}_{1}": ["29", "32", "39", "40", "42", "50"],
 "\\mathcal{Y}_{5}": ["50"],
 "\\mathcal{B}_{1}": ["29", "33", "40", "50"],
 "\\mathcal{W}_{1}": ["34", "38", "44"],
 "\\mathcal{G}_{1}": ["29", "33", "40", "50"],
 "\\mathcal{H}": ["11", "12", "13", "17", "19", "20", "21", "42"],
 "\\mathcal{B}": ["25", "27", "31", "32", "33", "35", "39", "42", "43", "48", "49", "50"],
 "\\mathcal{W}": ["31", "42", "43"],
 "\\mathcal{G}": ["27", "32", "33", "39", "42", "50"], 

}

def bracket_indices(s: str) -> tuple[bool, tuple[tuple[int, int], ...]]:
    """Returns a tuple (bool, ((index, index), ...)) showing whether 
       any indices are antisymmetric and the indices of those indices."""
    indices = []
    bracket_count = 0
    for i in range(len(s)):
        if s[i] in {"(", ")"}:
            bracket_count += 1
        if s[i] == '[':
            bracket_count += 1
            start = i - bracket_count + 1
        elif s[i] == ']':
            bracket_count += 1
            end = i - bracket_count
            indices.append((start, end))
    return (len(indices) > 0, tuple(indices))

def make_particle_dataframe(df, particle_operator_mapping) -> pd.DataFrame:
    df_list = []
    
    for particle, operators in particle_operator_mapping.items():
        for op in operators:
            op_label = ''.join(filter(str.isdigit, op))
            
            try:
                antisymmetric, antisymmetric_indices = bracket_indices(op.split(" ")[1])
            except:
                antisymmetric, antisymmetric_indices = False, tuple()
                
            antisymmetric_indices_str = "".join(str(x) for y in antisymmetric_indices for x in y)
            
            temp_df = df[df['fieldstring_label'] == int(op_label)].copy()
            if temp_df.empty:
                print(f"dataframe empty for {particle}!")
            temp_df['particle'] = particle
            temp_df['antisymmetric'] = antisymmetric
            temp_df['antisymmetric_indices'] = antisymmetric_indices_str
            
            # Filter based on antisymmetric indices
            if antisymmetric:
                def filter_flavours(row):
                    for i, j in antisymmetric_indices:
                        if row['fieldstring_flavour'][i] == row['fieldstring_flavour'][j]:
                            return False
                    return True
                
                temp_df = temp_df[temp_df.apply(filter_flavours, axis=1)]
            
            df_list.append(temp_df)
    
    new_df = pd.concat(df_list, ignore_index=True)
    return new_df


# In[301]:


particle_df = make_particle_dataframe(df=df, particle_operator_mapping=particle_operator_mapping)


# Keep in mind that the dataframe is empty for 6 fields since these give tree-level nucleon decays

# In[302]:


len(particle_operator_mapping) - 18 ## This is the number of rows we want at the end!


# In[303]:


particle_df


# ## Add future bound saturation information

# In[304]:


particle_df.keys()


# In[305]:


import sympy
from scipy.optimize import root, brentq

from tables import LAMBDA

def calc_exp_ratio(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x

    gamma = row.gamma_fieldstring_coeff_1.subs({LAMBDA: 1.})
    gamma_limit = 1.0 / value_in_inv_gev(row.lifetime_limit)

    ratio = gamma / gamma_limit
    return ratio

def calc_bviolation_scale_sympy(row):
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x

    gamma = row.gamma_fieldstring_coeff_1
    gamma_measurement = 1.0 / value_in_inv_gev(row.lifetime_limit)

    lambda_limit = sympy.solve(gamma_measurement - gamma, LAMBDA)

    return lambda_limit[-1]


# In[306]:


# Ratio to experimental limit
particle_df["exp_ratio"] = particle_df.apply(calc_exp_ratio, axis=1)


# In[307]:


particle_df.head()


# In[308]:


max_ratio_dict = particle_df[["particle", "fieldstring_label", "fieldstring_flavour", "exp_ratio"]].groupby(by=["particle"]).max().to_dict()["exp_ratio"]

def calc_bound_saturation(row):
    return row.exp_ratio / max_ratio_dict[row.particle]

particle_df["bound_saturation"] = particle_df.apply(calc_bound_saturation, axis=1)



# In[309]:


particle_df.keys()


# In[310]:


reduced_particle_df = particle_df[particle_df.bound_saturation > 0.1].drop_duplicates(
    subset=["smeft_label", "process", "left_dimension", "gamma_coeff_1", "left_op", "lifetime_limit", 
             "lifetime_limit_ref", "dim", "matrix_elem", "fieldstring_label", "gamma_fieldstring_coeff_1", 
             "particle", "exp_ratio", "bound_saturation"]
)

reduced_particle_df = reduced_particle_df[reduced_particle_df["bound_saturation"] > 0.9]
reduced_particle_df


# And the number of rows checks out

# In[311]:


reduced_particle_df["bviolation_scale"] = reduced_particle_df.apply(calc_bviolation_scale_sympy, axis=1)

reduced_particle_df


# ## Latex table

# Functions from other notebook

# In[312]:


import re

def remove_initial_sums(latex_expression):
    # Use regular expression to match and remove all initial sum expressions
    pattern_initial_sums = re.compile(r'\\sum_{([^}]*)}')

    # Find all matches of the pattern
    matches = pattern_initial_sums.findall(latex_expression)

    if matches:
        # Remove all initial sum expressions from the LaTeX string
        cleaned_expression = latex_expression
        for match in matches:
            cleaned_expression = cleaned_expression.replace(f"\\sum_{{{match}}}", "", 1)

        return cleaned_expression
    else:
        # Return the original expression if no initial sum expression is found
        return latex_expression

def process_latex(expr):
    expr = remove_initial_sums(expr)

    pattern_mathcal_O = re.compile(r'\\mathcal{O}\^{([^}]*)}_{([^}]*)}')
    pattern_mathcal_C = re.compile(r'\\mathcal{C}_{([^}]*)}\^{([^}]*)}')
    pattern_mathcal_barC = re.compile(r'\\bar{\\mathcal{C}}_{([^}]*)}\^{([^}]+)}')
    pattern_mathcal_barO = re.compile(r'\\mathcal{O}\^{((?:\\bar{[^}]+}|\\tilde{[^}]+}|[^}])+)}_{([^}]*)}')


    match_O = pattern_mathcal_O.search(expr)
    match_C = pattern_mathcal_C.search(expr)
    match_barC = pattern_mathcal_barC.search(expr)
    match_barO = pattern_mathcal_barO.search(expr)

    if match_O and match_C:
        subscripts_O = match_O.group(1)
        superscripts_O = match_O.group(2)
        subscripts_C = match_C.group(1)
        superscripts_C = match_C.group(2)

        math, _ = expr.split("\\mathcal{C}")
        transformed_expr = f"$C_{{{subscripts_O}}}^{{{superscripts_O}}} = {math} C_{{{subscripts_C}}}^{{{superscripts_C}}}$"
    elif match_barO and match_barC:
        subscripts_O = match_barO.group(1)
        superscripts_O = match_barO.group(2)
        subscripts_C = match_barC.group(1)
        superscripts_C = match_barC.group(2)

        math, _ = expr.split("\\bar{\\mathcal{C}}")
        transformed_expr = f"$C_{{{subscripts_O}}}^{{{superscripts_O}}} = {math} \\bar{{C}}_{{{subscripts_C}}}^{{{superscripts_C}}}$"
    else:
        return expr

    return transformed_expr


# In[313]:


reduced_particle_df['transformed_latex'] = reduced_particle_df['latex'].apply(process_latex)


# In[314]:


reduced_particle_df.transformed_latex


# In[315]:


def wrap_math(s):
    return "$" + s + "$"


# In[317]:


print(
reduced_particle_df[["particle", "transformed_latex", "fieldstring_flavour", "process", "bviolation_scale"]].to_latex(
    index=False,
    columns=["particle", "transformed_latex", "fieldstring_flavour", "process", "bviolation_scale"],
    header=["Particle", "Matching", "Flavour", "Process", "Scale [GeV]"],
    na_rep="---",
    column_format="lllll",
    formatters={"particle": wrap_math, "fieldstring_flavour": wrap_math, "process": wrap_math, "bviolation_scale": lambda x: f"\\tabnum{{{x}}}"},
    caption="This is the caption",
    label="tab:bviolation-table",
)
)


# In[ ]:





# In[ ]:




