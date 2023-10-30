#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Tuple
import sympy as sym
from math import pi

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
from matching import LOOP_LEVEL_MATCHING
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
        return "Missing"

    return max(
        (m for m in measurements if m.process == process), key=lambda x: x.value,
    )


def print_process_limits(measurements: List[Measurement]):
    output = {}
    inv_gev_per_year = 7.625e30
    value_in_inv_gev = lambda x: inv_gev_per_year * x
    for process in PROCESSES:
        meas = most_stringent_limit(measurements=measurements, process=process)
        if isinstance(meas, str):
            output[process] = meas
            continue
        gamma, cite = 1.0 / value_in_inv_gev(meas.value), meas.ref
        output[process] = (gamma, cite)

    return output


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


def derive_best_general_limits(
    operator_to_quantum_numbers=D6_LEFT_OPERATOR_SYMMETRIES,
    quantum_numbers_to_processes=ALLOWED_PROCESSES,
    decay_rates=None,  # Expecting list
):
    measurements = parse_limits("limits.yml")
    best_limits = {}
    for left_operator, quantum_numbers in operator_to_quantum_numbers.items():
        processes = quantum_numbers_to_processes[quantum_numbers]
        for process in processes:
            # Get baryon and meson
            baryon, meson_lepton = process.split("->")
            meson = meson_lepton[:-2]
            matrix_elem = get_matrix_element(left_operator, baryon, meson)

            lifetime_limit = most_stringent_limit(
                measurements=measurements, process=process
            )
            for smeft_op_expr in TREE_LEVEL_MATCHING[left_operator]:
                smeft_op_expr = smeft_op_expr.subs({V: CKM})

                gamma = dim_6_decay_rate(
                    operator=smeft_op_expr,
                    matrix_element=matrix_elem,
                    baryon=baryon,
                    meson=meson,
                )
                gamma = gamma.subs({VEV: VEV_VAL})

                inv_gev_per_year = 7.625e30
                value_in_inv_gev = lambda x: inv_gev_per_year * x
                gamma_limit = 1.0 / value_in_inv_gev(lifetime_limit.value)
                lambda_limits = sym.solve(gamma_limit - gamma, LAMBDA)

                # TODO Do something better here than just assuming the last one is positive
                lambda_limit = lambda_limits[-1]
                assert len(lambda_limit.free_symbols) == 1
                smeft_op = list(lambda_limit.free_symbols)[0]

                # Update decay rates for later use through side effect
                smeft_label, smeft_flavour = process_smeft_label(str(smeft_op))
                if decay_rates is not None:
                    # Read with pd.DataFrame.from_records(data)
                    decay_rates.append(
                        {
                            "smeft_op": smeft_op,
                            "smeft_label": smeft_label,
                            "smeft_flavour": smeft_flavour,
                            "process": PROCESS_TO_LATEX[process],
                            "gamma": gamma,
                            "gamma_coeff_1": gamma.subs({smeft_op: 1}),
                            "left_op": left_operator[0],
                            "left_flavour": "".join(str(i) for i in left_operator[1]),
                            "lambda_limit": lambda_limit,
                            "lambda_limit_coeff_1": lambda_limit.subs({smeft_op: 1}),
                        }
                    )

                # Keep only the best limit on each operator
                is_better = True
                if smeft_op in best_limits:
                    # Set coeffs to 1 and check which limit is best
                    is_better = best_limits[smeft_op][0].subs(
                        {smeft_op: 1}
                    ) < lambda_limit.subs({smeft_op: 1})

                if is_better:
                    best_limits[smeft_op] = (
                        lambda_limit,
                        process,
                        left_operator,
                        gamma,
                        smeft_label,
                        smeft_flavour,
                    )

    return best_limits


def derive_general_limits(
    operator_to_quantum_numbers={**D6_LEFT_OPERATOR_SYMMETRIES, **D7_LEFT_OPERATOR_SYMMETRIES},
    quantum_numbers_to_processes=ALLOWED_PROCESSES,
    decay_rates=None,  # Expecting list
):
    """Copy of the previous function but return all limits, not just the best ones."""
    measurements = parse_limits("limits.yml")
    best_limits = {}
    for left_operator, quantum_numbers in operator_to_quantum_numbers.items():
        processes = quantum_numbers_to_processes[quantum_numbers]

        # Specify mass-dimension of the left operator
        if left_operator in D7_LEFT_OPERATOR_SYMMETRIES:
            dimension = 7
        else:
            dimension = 6

        for process in processes:
            # Get baryon and meson
            baryon, meson_lepton = process.split("->")
            meson = meson_lepton[:-2]

            if dimension == 6:
                matrix_elem = get_matrix_element(left_operator, baryon, meson)

            lifetime_limit = most_stringent_limit(
                measurements=measurements, process=process
            )
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

                # TODO Do something better here than just assuming the last one is positive
                lambda_limit = lambda_limits[-1]
                assert len(lambda_limit.free_symbols) == 1
                smeft_op = list(lambda_limit.free_symbols)[0]

                # Update decay rates for later use through side effect
                smeft_label, smeft_flavour = process_smeft_label(str(smeft_op))
                if decay_rates is not None:
                    # Read with pd.DataFrame.from_records(data)
                    decay_rates.append(
                        {
                            "smeft_op": smeft_op,
                            "smeft_label": smeft_label,
                            "smeft_flavour": smeft_flavour,
                            "process": PROCESS_TO_LATEX[process],
                            "gamma": gamma,
                            "left_dimension": dimension,
                            "gamma_coeff_1": gamma.subs({smeft_op: 1}),
                            "left_op": left_operator[0],
                            "left_flavour": "".join(str(i) for i in left_operator[1]),
                            "lambda_limit": lambda_limit,
                            "lambda_limit_coeff_1": lambda_limit.subs({smeft_op: 1}),
                            "lifetime_limit": lifetime_limit.value,
                            "lifetime_limit_ref": lifetime_limit.name,
                        }
                    )

                if smeft_op not in best_limits:
                    best_limits[smeft_op] = []

                best_limits[smeft_op].append(
                    (
                        lambda_limit,
                        process,
                        left_operator,
                        gamma,
                        smeft_label,
                        smeft_flavour,
                    )
                )

    return best_limits


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


# GENERAL_LIMITS = derive_general_limits()


def _derive_loop_limits_helper(
    term, out, general_limits, fieldstring_label, fieldstring_coeff_exprs
):
    # term here is a coeff, it could be negative, so fix that too
    if isinstance(term, sym.core.mul.Mul):
        term *= -1

    if term in general_limits:
        for combo in general_limits[term]:
            limit, process, left_coeff, gamma, smeft_label, smeft_flavour = combo
            for fieldstring_coeff_expr in fieldstring_coeff_exprs:
                lambda_limit = limit.subs({term: fieldstring_coeff_expr})
                fieldstring_coeff = list(fieldstring_coeff_expr.free_symbols)[0]
                fieldstring_label, fieldstring_flavour = process_smeft_label(
                    str(fieldstring_coeff)
                )
                out.append(
                    {
                        "fieldstring_label": fieldstring_label[:-1],
                        "fieldstring_flavour": fieldstring_flavour,
                        "smeft_op": term,
                        "smeft_label": smeft_label,
                        "smeft_flavour": smeft_flavour,
                        "lambda_limit": lambda_limit,
                        "process": PROCESS_TO_LATEX[process],
                        "lambda_limit_coeff_1": lambda_limit.subs(
                            {fieldstring_coeff: 1}
                        ),
                        "left_op": left_coeff[0],
                        "left_flavour": "".join(str(i) for i in left_coeff[1]),
                        "gamma": gamma,
                        "gamma_fieldstring_coeff": gamma.subs(
                            {term: fieldstring_coeff_expr}
                        ),
                        "gamma_fieldstring_coeff_1": gamma.subs(
                            {term: fieldstring_coeff_expr}
                        ).subs({fieldstring_coeff: 1}),
                    }
                )


def derive_loop_limits(matching_dict=LOOP_LEVEL_MATCHING, general_limits=None):
    if general_limits is None:
        general_limits = derive_general_limits()

    out = []
    for fieldstring_label, matching_data in matching_dict.items():
        for smeft_coeff_expr, fieldstring_coeff_exprs in matching_data.items():
            if isinstance(smeft_coeff_expr, sym.core.add.Add):
                terms = smeft_coeff_expr.args
                for term in terms:
                    _derive_loop_limits_helper(
                        term=term,
                        out=out,
                        general_limits=general_limits,
                        fieldstring_label=fieldstring_label,
                        fieldstring_coeff_exprs=fieldstring_coeff_exprs,
                    )

            elif isinstance(smeft_coeff_expr, sym.core.symbol.Symbol):
                _derive_loop_limits_helper(
                    term=smeft_coeff_expr,
                    out=out,
                    general_limits=general_limits,
                    fieldstring_label=fieldstring_label,
                    fieldstring_coeff_exprs=fieldstring_coeff_exprs,
                )

            elif isinstance(smeft_coeff_expr, sym.core.mul.Mul):
                assert isinstance(-1 * smeft_coeff_expr, sym.core.symbol.Symbol)
                _derive_loop_limits_helper(
                    term=-1 * smeft_coeff_expr,
                    out=out,
                    general_limits=general_limits,
                    fieldstring_label=fieldstring_label,
                    fieldstring_coeff_exprs=fieldstring_coeff_exprs,
                )

            elif smeft_coeff_expr == 0:
                continue

            else:
                raise ValueError(
                    f"Unrecognised type {type(smeft_coeff_expr)} for {smeft_coeff_expr} in coefficient dispatch."
                )

    return out
