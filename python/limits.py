#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Tuple
import sympy as sym
from math import pi

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
    kinematics = masses[meson] * (1 - masses[meson] ** 2 / masses[baryon] ** 2) ** 2
    return (
        prefactor * kinematics * sym.Abs(matrix_element * operator / LAMBDA ** 2) ** 2
    )


def derive_general_limits(
    operator_dimension=6,
    operator_to_quantum_numbers=D6_LEFT_OPERATOR_SYMMETRIES,
    quantum_numbers_to_processes=ALLOWED_PROCESSES,
):
    measurements = parse_limits("limits.yml")
    for left_operator, quantum_numbers in operator_to_quantum_numbers.items():
        processes = quantum_numbers_to_processes[quantum_numbers]
        for process in processes:
            # Get baryon and meson
            baryon, meson_lepton = process.split("->")
            meson = meson_lepton[:-2]
            matrix_elem = get_matrix_element(left_operator, baryon, meson)

            ## TODO Check this with a few examples with Mathematica to make sure you haven't made a mistake
            # print(left_operator, process, get_matrix_element(left_operator, process))

            limit = most_stringent_limit(measurements=measurements, process=process)
            for smeft_op_expr in TREE_LEVEL_MATCHING[left_operator]:
                smeft_op_expr = smeft_op_expr.subs({V: CKM})
                # print(left_operator, process, smeft_op_expr)
                gamma = dim_6_decay_rate(
                    operator=smeft_op_expr,
                    matrix_element=matrix_elem,
                    baryon=baryon,
                    meson=meson,
                )
                gamma = gamma.subs({VEV: VEV_VAL})
                lambda_limit = sym.solve(limit.value - gamma, LAMBDA)
                print(lambda_limit[-1])


# print(sum_.subs({V: V_matrix}))
