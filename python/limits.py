#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Tuple, Dict
import sympy as sym
from math import pi
import numpy as np

from itertools import product

from collections import defaultdict

from tables import (
    D6_LEFT_OPERATOR_SYMMETRIES,
    D7_LEFT_OPERATOR_SYMMETRIES,
    ALLOWED_PROCESSES,
    HALF,
    V,
    LAMBDA,
    VEV,
    LATTICE_VALUES,
    CANONICAL_MATRIX_ELEMENTS,
    MATRIX_ELEMENTS,
    TREE_LEVEL_MATCHING,
)
from matching import LOOP_LEVEL_MATCHING, LATEX_EXPRS
from constants import CKM, MASSES, VEV_VAL


@dataclass
class Measurement:
    """Class for future or past measurements."""

    name: str
    expt: str
    ref: str
    url: str
    process: str
    value: float
    cl: float  # confidence level
    is_future: bool = False
    ineq: str = ">"  # one of "<" or ">"

MISSING = Measurement(*(["Missing"]*7))

PROCESS_TO_LATEX = {
    "p->K0e+": r"p \to K^{0} e^{+}",
    "p->K0mu+": r"p \to K^{0} \mu^{+}",
    "p->pi0e+": r"p \to \pi^{0} e^{+}",
    "p->pi0mu+": r"p \to \pi^{0} \mu^{+}",
    "p->pi+nu": r"p \to \pi^{+} \nu",
    "p->eta0e+": r"p \to \eta^{0} e^{+}",
    "p->eta0mu+": r"p \to \eta^{0} \mu^{+}",
    "p->K+nu": r"p \to K^{+} \nu",
    "n->pi0nu": r"n \to \pi^{0} \nu",
    "n->pi+e-": r"n \to \pi^{+} e^{-}",
    "n->pi+mu-": r"n \to \pi^{+} \mu^{-}",
    "n->pi-e+": r"n \to \pi^{-} e^{+}",
    "n->pi-mu+": r"n \to \pi^{-} \mu^{+}",
    "n->eta0nu": r"n \to \eta^{0} \nu",
    "n->K+e-": r"n \to K^{+} e^{-}",
    "n->K+mu-": r"n \to K^{+} \mu^{-}",
    "n->K0nu": r"n \to K^{0} \nu",
}


def parse_limits(yaml_path: str, is_future: bool = False) -> List[Measurement]:
    """Parse yaml data file of limits into a list of `Measurement` objects.

    """
    import yaml

    measurements = []
    with open(yaml_path, "r") as stream:
        data = yaml.safe_load(stream)
        for name, results in data.items():
            inputs = {
                "name": name,
                "expt": results["experiment"],
                "ref": results["inspire"],
                "url": results["url"],
                "is_future": is_future,
            }
            for process, value in results["values"].items():
                ineq_and_val, cl = value.split(" @ ")
                cl = float(cl[:2]) / 100
                ineq, val = ineq_and_val.split(" ")
                val = float(val)
                inputs["process"] = process
                inputs["cl"] = cl
                inputs["ineq"] = ineq
                inputs["value"] = val
                measurements.append(Measurement(**inputs))

    return measurements


def most_stringent_limit(measurements: List[Measurement], process: str) -> Measurement:
    if process not in [m.process for m in measurements]:
        return MISSING

    return max(
        (m for m in measurements if m.process == process), key=lambda x: x.value,
    )


def get_matrix_element(
    left_operator: Tuple[str, Tuple[int, int, int, int]], baryon: str, meson: str
) -> float:
    """Extracts the underlying hadronic matrix element from the data in
    tables.py

    """
    spinors = MATRIX_ELEMENTS[left_operator]
    num_factor, canon_mat_elem = CANONICAL_MATRIX_ELEMENTS[(meson, spinors, baryon)]
    return num_factor * LATTICE_VALUES[canon_mat_elem]


def dim_6_decay_rate(
    operator, matrix_element: float, baryon: str, meson: str, masses=MASSES,
):
    prefactor = 1 / (32 * pi)
    kinematics = masses[baryon] * (1 - masses[meson] ** 2 / masses[baryon] ** 2) ** 2
    return (
        prefactor * kinematics * sym.Abs(matrix_element * operator / LAMBDA ** 2) ** 2
    )


def dim_7_decay_rate(operator, baryon: str, meson: str, masses=MASSES):
    pion_decay_constant = 0.1302
    lambda_qcd = 0.2
    prefactor = 1 / (32 * pi * pion_decay_constant ** 2)
    kinematics = masses[baryon] * (1 - masses[meson] ** 2 / masses[baryon] ** 2) ** 2
    return (
        prefactor
        * kinematics
        * sym.Abs(operator * lambda_qcd ** 4 / LAMBDA ** 3) ** 2
    )


def process_smeft_label(label: str):
    label_parts = label.split("_")
    if len(label_parts) == 6:
        _, lbl, p, q, r, s = label_parts
        return (lbl, f"{int(p)+1}{int(q)+1}{int(r)+1}{int(s)+1}")
    # Six indices here, unpack accordingly
    _, lbl, p, q, r, s, t, u = label_parts
    return (lbl, f"{int(p)+1}{int(q)+1}{int(r)+1}{int(s)+1}{int(t)+1}{int(u)+1}")

def extract_particles(s: str):
    # Split the string at "->" to separate the baryon from the rest
    baryon, rest = s.split("->")

    # Find the index of the first occurrence of "0", "+", or "-" in the rest of the string
    # This will mark the end of the meson
    meson_end_index = min([rest.find(char) for char in "0+-" if rest.find(char) != -1]) + 1

    # Extract the meson using the found index; everything up to that index is the meson
    meson = rest[:meson_end_index]

    # The lepton is everything after the meson
    lepton = rest[meson_end_index:]

    return baryon, meson, lepton

def get_tree_level_records_by_dict(
    operator_to_quantum_numbers={**D6_LEFT_OPERATOR_SYMMETRIES, **D7_LEFT_OPERATOR_SYMMETRIES},
    quantum_numbers_to_processes=ALLOWED_PROCESSES,
) -> Dict[str, list]:
    """Returns records organised into a dictionary by the `smeft_op` key."""

    results_dict = defaultdict(list)
    measurements = parse_limits("limits.yml")
    sensitivities = parse_limits("future.yml", is_future=True)
    for left_operator, quantum_numbers in operator_to_quantum_numbers.items():
        processes = quantum_numbers_to_processes[quantum_numbers]

        # Specify mass-dimension of the left operator
        if left_operator in D7_LEFT_OPERATOR_SYMMETRIES:
            dimension = 7
        else:
            dimension = 6

        for process in processes:
            # Get baryon and meson
            baryon, meson, lepton = extract_particles(process)

            matrix_elem = np.nan
            if dimension == 6:
                matrix_elem = get_matrix_element(left_operator, baryon, meson)

            # lifetime_limit = most_stringent_limit(
            #     measurements=measurements, process=process
            # )

            relevant_measurements = [most_stringent_limit(measurements=measurements, process=process), *[m for m in sensitivities if m.process == process]]
            for lifetime_limit in relevant_measurements:
                if lifetime_limit.name == "Missing":
                    continue
                for smeft_op_expr in TREE_LEVEL_MATCHING[left_operator]:
                    smeft_op_expr = smeft_op_expr.subs({V: CKM})

                    if dimension == 6:
                        gamma = dim_6_decay_rate(
                            operator=smeft_op_expr,
                            matrix_element=matrix_elem,
                            baryon=baryon,
                            meson=meson,
                        )
                    elif dimension == 7:
                        gamma = dim_7_decay_rate(
                            operator=smeft_op_expr,
                            baryon=baryon,
                            meson=meson,
                        )
                    else:
                        raise ValueError("Dimension of left operator incorrect: {dimension}.")


                    gamma = gamma.subs({VEV: VEV_VAL})

                    inv_gev_per_year = 7.625e30
                    value_in_inv_gev = lambda x: inv_gev_per_year * x
                    gamma_limit = 1.0 / value_in_inv_gev(lifetime_limit.value)
                    lambda_limits = sym.solve(gamma_limit - gamma, LAMBDA)

                    # Currently just assuming the last one is positive
                    lambda_limit = lambda_limits[-1]
                    assert len(lambda_limit.free_symbols) == 1
                    smeft_op = list(lambda_limit.free_symbols)[0]

                    smeft_label, smeft_flavour = process_smeft_label(str(smeft_op))
                    record = {
                        "smeft_op": smeft_op,
                        "smeft_label": smeft_label,
                        "smeft_flavour": smeft_flavour,
                        "smeft_op_expr": smeft_op_expr,
                        "process": PROCESS_TO_LATEX[process],
                        "gamma": gamma,
                        "left_dimension": dimension,
                        "gamma_coeff_1": gamma.subs({smeft_op: 1}),
                        "left_op": left_operator[0],
                        "left_flavour": "".join(str(i) for i in left_operator[1]),
                        "lambda_limit": lambda_limit,
                        "lambda_limit_coeff_1": lambda_limit.subs({smeft_op: 1}),
                        "lifetime_limit": lifetime_limit.value,
                        "lifetime_limit_ref": lifetime_limit.ref,
                        "is_future": lifetime_limit.is_future,
                        "dim": dimension, ## TODO Mark for deprication (same as left_dimension)
                        "matrix_elem": matrix_elem,
                    }

                    results_dict[smeft_op].append(record)

    return results_dict

def get_tree_level_records(*args, **kwargs) -> List[dict]:
    """A convenient wrapper around `get_tree_level_records_by_dict` to use to
    construct a dataframe.

    Read with `pd.DataFrame.from_records(data)`

    """
    def flatten(matrix: List[List[dict]]) -> List[dict]:
        return [item for row in matrix for item in row]

    results_dict = get_tree_level_records_by_dict(*args, **kwargs)

    return flatten(list(results_dict.values()))



def typeset_operator_label(label: str) -> str:
    return r"$" + PROCESS_TO_LATEX[label] + "$"


def typeset_left_operator(key: Tuple[str, Tuple[int, int, int, int]]):
    label, flavour = key
    p, q, r, s = flavour
    sup, sub = key[0].split("_")
    return f"$[C_{{{sub}}}^{{{sup}}}]_{{{p}{q}{r}{s}}}$"


def print_general_limits(best_limits):
    for k, v in best_limits.items():
        latex_expr = sym.latex(v[0]).replace("K", "C")
        latex_expr = latex_expr.replace("qqql", "qqql,")
        latex_expr = latex_expr.replace("duql", "duql,")
        latex_expr = latex_expr.replace("qque", "qque,")
        latex_expr = latex_expr.replace("duue", "duue,")
        latex_expr = latex_expr.replace("ddqlHH", "ddqlHH,")
        latex_expr = latex_expr.replace("eqqqHHH", "eqqqHHH,")
        latex_expr = latex_expr.replace("l~dqqH~", "\\bar{l}dqq\\tilde{H},")
        latex_expr = latex_expr.replace("e~qddH~", "\\bar{e}qdd\\tilde{H},")
        latex_expr = latex_expr.replace("l~dudH~", "\\bar{l}dud\\tilde{H},")
        latex_expr = latex_expr.replace("l~dddH", "\\bar{l}dddH,")
        latex_expr = latex_expr.replace("luqqHHH", "luqqHHH,")
        latex_expr = latex_expr.replace(" \\cdot 10^{15}", "e15")
        latex_expr = latex_expr.replace("\\left|", "")
        latex_expr = latex_expr.replace("\\right|", "")

        number, expr = latex_expr.split(" \sqrt")
        latex_expr = f"\\tabnum{{{number}}} \\sqrt{expr}"

        # Replace all zero indexing
        index_perms = [" ".join(x) for x in product("012", "012", "012", "012")][::-1]

        add_one_index_perms = [
            " ".join(str(int(i) + 1) for i in x.split()) for x in index_perms
        ]

        for perm1, perm2 in zip(index_perms, add_one_index_perms):
            latex_expr = latex_expr.replace(perm1, perm2)

        print(
            f"${latex_expr}$ & {typeset_operator_label(v[1])} & {typeset_left_operator(v[2])} \\\\"
        )


def _derive_loop_limits_helper(
        term, out, tree_level_records_dict, fieldstring_label, fieldstring_coeff_exprs, latex
):
    # term here is a coeff, it could be negative, so fix that too
    if isinstance(term, sym.core.mul.Mul):
        term *= -1

    if term in tree_level_records_dict:
        for record in tree_level_records_dict[term]:
            tree_level_info = record
            gamma = record["gamma"]
            limit = record["lambda_limit"]
            for fieldstring_coeff_expr in fieldstring_coeff_exprs:
                lambda_limit = limit.subs({term: fieldstring_coeff_expr})
                fieldstring_coeff = list(fieldstring_coeff_expr.free_symbols)[0]
                fieldstring_label, fieldstring_flavour = process_smeft_label(
                    str(fieldstring_coeff)
                )

                loop_level_info = {
                    "fieldstring_label": fieldstring_label[:-1],
                    "fieldstring_flavour": fieldstring_flavour,
                    "smeft_op": term,
                    "latex": latex,
                    "lambda_limit": lambda_limit,
                    "lambda_limit_coeff_1": lambda_limit.subs(
                        {fieldstring_coeff: 1}
                    ),
                    "gamma_fieldstring_coeff": gamma.subs(
                        {term: fieldstring_coeff_expr}
                    ),
                    "gamma_fieldstring_coeff_1": gamma.subs(
                        {term: fieldstring_coeff_expr}
                    ).subs({fieldstring_coeff: 1}),
                }

                out.append({**tree_level_info, **loop_level_info})


def get_loop_level_records(matching_dict=LOOP_LEVEL_MATCHING, tree_level_records_dict=None):
    if tree_level_records_dict is None:
        tree_level_records_dict = get_tree_level_records_by_dict()

    out = [] # The loop-level records
    for fieldstring_label, matching_data in matching_dict.items():
        # matching_data is a dictionary mapping symbolic SMEFT coefficients to
        # tuples of tuples of sympy expressions involving symbolic coefficients
        # of field strings
        for smeft_coeff_expr, fieldstring_coeff_exprs_tuple in matching_data.items():
            # fieldstring_coeff_exprs_tuple is a tuple of tuples. The inner layer of
            # tuple represents the sum over indices, the second represents
            # distinct contributions that don't just come about from summation.
            # These will have different latex representations
            latex_exprs = LATEX_EXPRS[fieldstring_label][smeft_coeff_expr]
            assert len(latex_exprs) == len(fieldstring_coeff_exprs_tuple)

            for latex_str, fieldstring_coeff_exprs in zip(latex_exprs, fieldstring_coeff_exprs_tuple):
                if isinstance(smeft_coeff_expr, sym.core.add.Add):
                    terms = smeft_coeff_expr.args
                    for term in terms:
                        _derive_loop_limits_helper(
                            term=term,
                            out=out,
                            tree_level_records_dict=tree_level_records_dict,
                            fieldstring_label=fieldstring_label,
                            fieldstring_coeff_exprs=fieldstring_coeff_exprs,
                            latex=latex_str,
                        )

                elif isinstance(smeft_coeff_expr, sym.core.symbol.Symbol):
                    _derive_loop_limits_helper(
                        term=smeft_coeff_expr,
                        out=out,
                        tree_level_records_dict=tree_level_records_dict,
                        fieldstring_label=fieldstring_label,
                        fieldstring_coeff_exprs=fieldstring_coeff_exprs,
                        latex=latex_str,
                    )

                elif isinstance(smeft_coeff_expr, sym.core.mul.Mul):
                    assert isinstance(-1 * smeft_coeff_expr, sym.core.symbol.Symbol)
                    _derive_loop_limits_helper(
                        term=-1 * smeft_coeff_expr,
                        out=out,
                        tree_level_records_dict=tree_level_records_dict,
                        fieldstring_label=fieldstring_label,
                        fieldstring_coeff_exprs=fieldstring_coeff_exprs,
                        latex=latex_str,
                    )

                elif smeft_coeff_expr == 0:
                    continue

                else:
                    raise ValueError(
                        f"Unrecognised type {type(smeft_coeff_expr)} for {smeft_coeff_expr} in coefficient dispatch."
                    )
    return out
