#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List
import sympy as sym

from tables import (
    D6_LEFT_OPERATOR_SYMMETRIES,
    D7_LEFT_OPERATOR_SYMMETRIES,
    PROCESSES,
    HALF,
)


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


def derive_general_limits():
    for left_operator in LEFT_OPERATOR_SYMMETRIES:
        pass


V = sym.MatrixSymbol("V", 3, 3)
V_matrix = sym.Matrix(
    [[0.973, 0.2245, 0.008], [0.22, 0.987, 0.04], [0.008, 0.0388, 1.013]]
)
# C = sym.symarray("C", (3, 3, 3, 3))
i, j, k, l, m = sym.symbols("i j k l m")
C = sym.tensor.Array(C)

sum_ = sym.summation(V[0, j] * V[0, k] * C[0, j, k, 0], (j, 0, 2), (k, 0, 2))

## TODO Each of the coefficients here should be constrained separately
print(sum_.subs({V: V_matrix}))
