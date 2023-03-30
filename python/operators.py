#!/usr/bin/env python3
#!/usr/bin/env python3

"""Script to write latex table of operators appearing the paper."""

import os
from collections import defaultdict
from sympy.abc import X
from string import ascii_lowercase
from typing import Dict, List, Tuple
import subprocess

import neutrinomass.tensormethod.sm as sm
from neutrinomass.tensormethod.parse_hs import FIELD_LOOKUP, parse
from neutrinomass.tensormethod.contract import invariants
from neutrinomass.completions.core import EffectiveOperator

PRINT_WL = False # False for LaTeX table
PRINT_RULE = True

from hs import (
    H6_ΔB1_ΔL1,
    H7_ΔBn1_ΔL1,
    H8_ΔB1_ΔL1,
    H9_ΔB2_ΔL0,
    H9_ΔBn1_ΔL1,
    H9_ΔB1_ΔL3,
    D,
)


def to_wl(op, label: str, matching_rule=False) -> None:
    """Prints a representation of the operator in Wolfram-language code.

    E.g.

    "2"  -> Prod[G["2"][r,s,t,u]
           , Conj[eb[r]], Q[s,a,i], Q[t,b,j], Conj[ub[u,c]]
           , Eps[i,j], Eps[a,b,c]

    """
    # Set up a standard order for the fields
    field_ordering = ["L", "e", "Q", "u", "d", "H", "B", "W", "G"]
    for field in op.indexed_fields:
        f, fc = field, field.conj
        if hasattr(f, "label") and not f.label in field_ordering:
            field_ordering.append(f.label.replace("~", ""))
            field_ordering.append(fc.label.replace("~", ""))

    style = {
        "g": list(ascii_lowercase[17:]),
    }

    try:
        # extract first non D in field name e.g. H for DDH
        # (currently only taking first char of field name)
        first_non_deriv = lambda f: str(f).split("D")[-1][0]
        order_func = lambda f: field_ordering.index(first_non_deriv(f))
        sorted_fields = sorted(op.indexed_fields, key=order_func)
    except:
        # if exotic field present in operator, won't be present in
        # `field_ordering` above. Just sort the fields lexicographically in that case
        # Still extract first non D in field name e.g. H for DDH
        first_non_deriv = lambda f: str(f).split("D")[-1]
        sorted_fields = sorted(op.indexed_fields, key=first_non_deriv)

    # Get indices for each field
    index_info: List[List[str]] = []
    # Get label and conj status for each field. True means conjed.
    label_info: List[Tuple[str, bool]] = []
    # Keep track of generation indices for operator coefficient too
    generation_indices = []
    index_dict = {}
    for i, field in enumerate(sorted_fields):
        index_info.append([])

        if field.is_conj:
            label_info.append((field.label[:-1], True))
        else:
            label_info.append((field.label, False))

        for index in field.indices:
            type_ = str(index)[0]
            if type_ == "-":
                type_ = str(index)[1]
            if type_ in {"u", "d", "i", "c"}:
                continue
            new_index = style[type_].pop(0)
            index_dict[index] = new_index
            # Generation need to be reordered (from last to first)
            if type_ == "g":
                index_info[i].insert(0, new_index)
                generation_indices.append(new_index)
            else:
                index_info[i].append(new_index)

    # Construct operator coeff
    coeff_indices = ",".join(generation_indices)
    coeff = f'Wt[G["{label}"][{coeff_indices}]]'

    # Construct fields
    field_strings = []
    conj_field_strings = []
    for (f, is_conj), indices in zip(label_info, index_info):
        indices_str = ",".join(indices)
        guts = f"{f}[{indices_str}]"
        guts = guts.replace("D", "Deriv, ")
        if is_conj:
            field_strings.append(f"Conj[{guts}]")
            conj_field_strings.append(guts)
        else:
            field_strings.append(guts)
            conj_field_strings.append(f"Conj[{guts}]")

    if matching_rule:
        matching_vals_guts = ", ".join(f'"{idx}" -> {idx}' for idx in generation_indices)

        # Replace indices on LHS with Mathematica patterns. This approach is
        # specialised to one index in the fields!
        gen_indices_replacements = [(f"[{i}]", f"[{i}_]") for i in generation_indices]
        rule_field_strings = field_strings
        rule_conj_field_strings = conj_field_strings
        for i, j in gen_indices_replacements:
            rule_field_strings = [s.replace(i, j) for s in rule_field_strings]
            rule_conj_field_strings = [s.replace(i, j) for s in rule_conj_field_strings]

        print(f"(* Op {label} *)")
        print(
            f'Op['
            + ", ".join(rule_field_strings)
            + ", rst___Wt"
            + f'] :> Op[Op["{label}"][{coeff_indices}], MatchingValues[{matching_vals_guts}]'
            + "],"
        )
        print(
            f'Op['
            + ", ".join(rule_field_strings)
            + ", Deriv, Deriv"
            + ", rst___Wt"
            + f'] :> Op[Op["{label}"][{coeff_indices}], MatchingValues[{matching_vals_guts}]'
            + "],"
        )
        # Conjugates
        print(
            f'Op['
            + ", ".join(rule_conj_field_strings)
            + ", rst___Wt"
            + f'] :> Op[Conj[Op["{label}"][{coeff_indices}]], MatchingValues[{matching_vals_guts}]'
            + "],"
        )
        print(
            f'Op['
            + ", ".join(rule_conj_field_strings)
            + ", Deriv, Deriv"
            + ", rst___Wt"
            + f'] :> Op[Conj[Op["{label}"][{coeff_indices}]], MatchingValues[{matching_vals_guts}]'
            + "],"
        )
        return

    print(
        f'"{label}" -> Op['
        + ", ".join([coeff, *field_strings])
        + "],"
    )
    return

operators = defaultdict(list)
counter = 0
operator_series = [
    H6_ΔB1_ΔL1,
    H7_ΔBn1_ΔL1,
    H8_ΔB1_ΔL1,
    # H9_ΔB2_ΔL0,
    H9_ΔBn1_ΔL1,
    # H9_ΔB1_ΔL3,
]
terms_labels = [
    (6, 1, 1),
    (7, -1, 1),
    (8, 1, 1),
    # (9, 2, 0),
    (9, -1, 1),
    # (9, 1, 3)
]

symmetries = {
    "2": [("S", 2, 3)],
    "5": [("A", 3, 4)],
    "6": [("S", 3, 4)],
    "7": [("S", 2, 4)],
    "9": [("A", 3, 4)],
    "14": [("A", 3, 4)],
    "15": [("A", 2, 3)],
    "16": [("A", 3, 4)],
    "25": [("A", 5, 6), ("S", 1, 2)],
    "26": [("A", 3, 4)],
    "27": [("A", 4, 5), ("S", 2, 3)], # not sure about this one
    "35": [("A", 5, 6)],
    "36": [("A", 3, 4)],
    "37": [("A", 2, 3)],
    "47": [("A", 3, 4)],
    "48": [("S", 3, 4)],
    }

def flavour_indices_and_symmetries(op, symmetries):
    op_latex = op.latex(ignore=["u", "d", "c", "i"])
    n_fields = len(op.fields)
    fields = op_latex.split()[:n_fields]
    flavour_indices = ["p", "q", "r", "s", "t", "u", "v", "w"]
    new_fields = []
    for flav, field in enumerate(fields):
        L, R = "", ""
        if op_label in symmetries:
            for symmetry in symmetries[op_label]:
                sym_type, idx1, idx2, = symmetry
                if idx1 - 1 == flav:
                    L = r"\{" if sym_type == "S" else "["
                elif idx2 - 1 == flav:
                    R = r"\}" if sym_type == "S" else "]"

        # Don't add flavour indices to the Higgs
        if "H" in field:
            new_fields.append(field)
        else:
            new_fields.append(field + "_{" + L + flavour_indices[flav] + R + "}")

    # Remove parens from deriv terms
    new_fields = [f.replace("(", "").replace(")", "") for f in new_fields]

    # Replace tilde with dagger
    new_fields = [f.replace("\\tilde", "\\dagf") for f in new_fields]

    new_op_latex = " ".join(new_fields + op_latex.split()[n_fields:])

    # Move deriv to the front
    if "D" in new_op_latex:
        new_op_latex = "D" + new_op_latex.replace("D", "")

    return new_op_latex


table_1, table_2 = [], []
seen = set()
for terms_label, terms in zip(terms_labels, operator_series):
    # remove derivatives just for now
    # no_deriv_terms = terms.xreplace({D: 0})
    for fields in parse(terms):

        # Skip set of fields if derivative is contracted in a (0, 1) or (1, 0)
        skip = False
        for f in fields:
            if "D" in f.label and f.lorentz_irrep not in {(2, 1), (1, 2)}:
                skip = True

        if skip:
            continue

        invs = invariants(*fields)

        # Sometimes the derivative contraction doesn't work, skip these
        if not invs:
            continue

        # Make sure you don't double up on field content
        rep = []
        for f in fields:
            if "D" in f.label:
                rep.append("D")
                rep.append(f.label_with_dagger[1:])
            else:
                rep.append(f.label_with_dagger)

        rep.sort()
        if tuple(rep) in seen:
            continue

        seen.add(tuple(rep))

        counter += 1
        operators[counter] += invs

        dim, deltab, deltal = terms_label

        # Impose this for now to remove multiple applications of the derivative
        invs = invs[:1]
        for a, op in zip(ascii_lowercase, invs):

            # Operator label with SU(2) structure if present
            op_label = f"{counter}{a}" if len(invs) > 1 else str(counter)

            if PRINT_WL:
                to_wl(op, op_label, matching_rule=PRINT_RULE)
            else:
                # Add in flavour indices
                new_op_latex = flavour_indices_and_symmetries(op, symmetries)

                print(
                    f"\t${op_label}$ & ${new_op_latex}$ & ${dim}$ & ${deltab}$ & ${deltal}$ \\\\"
                )
