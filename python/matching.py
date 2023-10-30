#!/usr/bin/env python3

import sympy as sym
from sympy import conjugate as conj
from math import pi
import itertools
from collections import defaultdict

from tables import C, G
from constants import CKM, VEV_VAL

X = {}  # C_11, C_12, ...

LOOP_LEVEL_MATCHING = {}
# Fill all dimension-8 operators
for i in range(11, 25):
    LOOP_LEVEL_MATCHING[str(i) + ","] = defaultdict(tuple)
    X[str(i) + ","] = sym.tensor.Array(sym.symarray(f"C_{i},", (3, 3, 3, 3)))

# Some dimension-9 operators have six flavour indices
six_indices = [25, 27, 28, 29, 30, 31, 32, 33, 35, 39, 40, 41, 42, 49, 50]
for i in six_indices:
    LOOP_LEVEL_MATCHING[str(i) + ","] = defaultdict(tuple)
    X[str(i) + ","] = sym.tensor.Array(sym.symarray(f"C_{i},", (3, 3, 3, 3, 3, 3)))

for i in range(25, 51):
    # The remainder of the dimension-9 operators have four indices
    if i in six_indices:
        continue
    LOOP_LEVEL_MATCHING[str(i) + ","] = defaultdict(tuple)
    X[str(i) + ","] = sym.tensor.Array(sym.symarray(f"C_{i},", (3, 3, 3, 3)))

loop = 1 / (16 * pi**2)
# RUNNING MASSES AT m_t taken from 2009.04851 (see also 0712.1419)
yd = [2.56e-3 / VEV_VAL, 50.90e-3 / VEV_VAL, 2.702 / VEV_VAL]
yu = [1.18e-3 / VEV_VAL, 0.594 / VEV_VAL, 161.98 / VEV_VAL]
ye = [0.48583e-6 / VEV_VAL, 102.347e-3 / VEV_VAL, 1.73850 / VEV_VAL]


# TODO 5, 8, 9, 10, 34, 38, 44 are implicitely conjugated! This needs to be
# dealt with in the LaTeX export
for p, q, r, s in list(itertools.product(*[[0, 1, 2]] * 4)):
    LOOP_LEVEL_MATCHING["11,"][G["duql"][p, q, r, s]] += (
        loop * yu[q] * X["11,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["11,"][G["duql"][p, q, r, s]] += (
        loop * yu[q] * X["11,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["11,"][G["qqql"][p, q, r, s]] += (
        loop * conj(CKM[r, 0]) * yd[0] * X["11,"][s, p, q, 0],
        loop * conj(CKM[r, 1]) * yd[1] * X["11,"][s, p, q, 1],
        loop * conj(CKM[r, 2]) * yd[2] * X["11,"][s, p, q, 2],
    )

    LOOP_LEVEL_MATCHING["12,"][G["duql"][p, q, r, s]] += (
        loop * conj(CKM[r, 0]) * yd[0] * X["12,"][s, q, 0, p],
        loop * conj(CKM[r, 1]) * yd[1] * X["12,"][s, q, 1, p],
        loop * conj(CKM[r, 2]) * yd[2] * X["12,"][s, q, 2, p],
    )

    LOOP_LEVEL_MATCHING["12,"][G["duql"][p, q, r, s]] += (
        loop * conj(CKM[r, 0]) * yd[0] * X["12,"][s, q, p, 0],
        loop * conj(CKM[r, 1]) * yd[1] * X["12,"][s, q, p, 1],
        loop * conj(CKM[r, 2]) * yd[2] * X["12,"][s, q, p, 2],
    )

    LOOP_LEVEL_MATCHING["13,"][G["duql"][p, q, r, s]] += (
        loop * yu[r] * X["13,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["13,"][G["duql"][p, q, r, s]] += (
        loop * yu[r] * X["13,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["13,"][G["duue"][p, q, r, s]] += (
        loop * ye[s] * X["13,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["14,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * yu[q] * yu[r] * X["14,"][s, p, q, r],
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["14,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["14,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["14,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[0] * X["14,"][s, r, 0, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[1] * X["14,"][s, r, 1, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[2] * X["14,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["14,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[s] * X["14,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["14,"][s, 0, q, r],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["14,"][s, 1, q, r],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["14,"][s, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[0] * X["14,"][s, r, q, 0],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[1] * X["14,"][s, r, q, 1],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[2] * X["14,"][s, r, q, 2],
    )

    LOOP_LEVEL_MATCHING["14,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[s] * X["14,"][q, r, p, s],
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["14,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["14,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["14,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["14,"][s, 0, q, r],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["14,"][s, 1, q, r],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["14,"][s, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["14,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["14,"][s, 0, q, r],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["14,"][s, 1, q, r],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["14,"][s, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["14,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[s] * X["14,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["14,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[s] * X["14,"][q, r, p, s],
    )

    LOOP_LEVEL_MATCHING["14,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["14,"][s, 0, q, r],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["14,"][s, 1, q, r],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["14,"][s, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["15,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * yu[q] * yu[r] * X["15,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[p] * X["15,"][q, r, p, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[p] * X["15,"][q, r, p, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[p] * X["15,"][q, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["15,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * ye[s] * yu[q] * X["15,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["15,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * yu[q] * yu[r] * X["15,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[p] * X["15,"][q, r, p, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[p] * X["15,"][q, r, p, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[p] * X["15,"][q, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["15,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * ye[s] * yu[q] * X["15,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[p] * X["15,"][q, r, p, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[p] * X["15,"][q, r, p, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[p] * X["15,"][q, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[p] * X["15,"][q, r, p, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[p] * X["15,"][q, r, p, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[p] * X["15,"][q, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[p, 0]) * yd[0] * yu[p] * X["15,"][q, r, s, 0],
        (loop) ** (2) * conj(CKM[p, 1]) * yd[1] * yu[p] * X["15,"][q, r, s, 1],
        (loop) ** (2) * conj(CKM[p, 2]) * yd[2] * yu[p] * X["15,"][q, r, s, 2],
    )

    LOOP_LEVEL_MATCHING["15,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * ye[s] * X["15,"][s, p, q, 0],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * ye[s] * X["15,"][s, p, q, 1],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * ye[s] * X["15,"][s, p, q, 2],
    )

    LOOP_LEVEL_MATCHING["15,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * ye[s] * yu[q] * X["15,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["15,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * ye[s] * yu[q] * X["15,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["15,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * ye[s] * X["15,"][s, p, q, 0],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * ye[s] * X["15,"][s, p, q, 1],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * ye[s] * X["15,"][s, p, q, 2],
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["16,"][s, q, 0, p],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["16,"][s, q, 1, p],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["16,"][s, q, 2, p],
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["16,"][s, q, p, 0],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["16,"][s, q, p, 1],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["16,"][s, q, p, 2],
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["16,"][s, q, 0, p],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["16,"][s, q, 1, p],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["16,"][s, q, 2, p],
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[q, 0]) * yd[0] * yu[q] * X["16,"][s, r, 0, p],
        (loop) ** (2) * conj(CKM[q, 1]) * yd[1] * yu[q] * X["16,"][s, r, 1, p],
        (loop) ** (2) * conj(CKM[q, 2]) * yd[2] * yu[q] * X["16,"][s, r, 2, p],
    )

    LOOP_LEVEL_MATCHING["16,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[q, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["16,"][s, p, 0, 0],
        (loop) ** (2)
        * conj(CKM[q, 0])
        * conj(CKM[r, 1])
        * yd[0]
        * yd[1]
        * X["16,"][s, p, 0, 1],
        (loop) ** (2)
        * conj(CKM[q, 0])
        * conj(CKM[r, 2])
        * yd[0]
        * yd[2]
        * X["16,"][s, p, 0, 2],
        (loop) ** (2)
        * conj(CKM[q, 1])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[1]
        * X["16,"][s, p, 1, 0],
        (loop) ** (2)
        * conj(CKM[q, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["16,"][s, p, 1, 1],
        (loop) ** (2)
        * conj(CKM[q, 1])
        * conj(CKM[r, 2])
        * yd[1]
        * yd[2]
        * X["16,"][s, p, 1, 2],
        (loop) ** (2)
        * conj(CKM[q, 2])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[2]
        * X["16,"][s, p, 2, 0],
        (loop) ** (2)
        * conj(CKM[q, 2])
        * conj(CKM[r, 1])
        * yd[1]
        * yd[2]
        * X["16,"][s, p, 2, 1],
        (loop) ** (2)
        * conj(CKM[q, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["16,"][s, p, 2, 2],
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["16,"][s, q, p, 0],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["16,"][s, q, p, 1],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["16,"][s, q, p, 2],
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[q, 0]) * yd[0] * yu[q] * X["16,"][s, r, p, 0],
        (loop) ** (2) * conj(CKM[q, 1]) * yd[1] * yu[q] * X["16,"][s, r, p, 1],
        (loop) ** (2) * conj(CKM[q, 2]) * yd[2] * yu[q] * X["16,"][s, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["16,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[q, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["16,"][s, p, 0, 0],
        (loop) ** (2)
        * conj(CKM[q, 1])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[1]
        * X["16,"][s, p, 0, 1],
        (loop) ** (2)
        * conj(CKM[q, 2])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[2]
        * X["16,"][s, p, 0, 2],
        (loop) ** (2)
        * conj(CKM[q, 0])
        * conj(CKM[r, 1])
        * yd[0]
        * yd[1]
        * X["16,"][s, p, 1, 0],
        (loop) ** (2)
        * conj(CKM[q, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["16,"][s, p, 1, 1],
        (loop) ** (2)
        * conj(CKM[q, 2])
        * conj(CKM[r, 1])
        * yd[1]
        * yd[2]
        * X["16,"][s, p, 1, 2],
        (loop) ** (2)
        * conj(CKM[q, 0])
        * conj(CKM[r, 2])
        * yd[0]
        * yd[2]
        * X["16,"][s, p, 2, 0],
        (loop) ** (2)
        * conj(CKM[q, 1])
        * conj(CKM[r, 2])
        * yd[1]
        * yd[2]
        * X["16,"][s, p, 2, 1],
        (loop) ** (2)
        * conj(CKM[q, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["16,"][s, p, 2, 2],
    )

    LOOP_LEVEL_MATCHING["17,"][G["qque"][p, q, r, s]] += (
        loop * yu[s] * X["17,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["17,"][G["qque"][p, q, r, s]] += (
        loop * yu[s] * X["17,"][q, r, p, s],
    )

    LOOP_LEVEL_MATCHING["17,"][G["duue"][p, q, r, s]] += (
        loop * conj(CKM[0, p]) * yd[p] * X["17,"][s, 0, q, r],
        loop * conj(CKM[1, p]) * yd[p] * X["17,"][s, 1, q, r],
        loop * conj(CKM[2, p]) * yd[p] * X["17,"][s, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * (yu[r]) ** (2) * X["18,"][s, p, q, r],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * (yu[r]) ** (2) * X["18,"][s, p, q, r],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * (yu[r]) ** (2) * X["18,"][s, p, q, r],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["18,"][s, 0, p, q],
        (loop) ** (2)
        * conj(CKM[0, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["18,"][s, 0, p, q],
        (loop) ** (2)
        * conj(CKM[0, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["18,"][s, 0, p, q],
        (loop) ** (2)
        * conj(CKM[1, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["18,"][s, 1, p, q],
        (loop) ** (2)
        * conj(CKM[1, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["18,"][s, 1, p, q],
        (loop) ** (2)
        * conj(CKM[1, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["18,"][s, 1, p, q],
        (loop) ** (2)
        * conj(CKM[2, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["18,"][s, 2, p, q],
        (loop) ** (2)
        * conj(CKM[2, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["18,"][s, 2, p, q],
        (loop) ** (2)
        * conj(CKM[2, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["18,"][s, 2, p, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["18,"][s, p, 0, q],
        (loop) ** (2)
        * conj(CKM[0, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["18,"][s, p, 0, q],
        (loop) ** (2)
        * conj(CKM[0, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["18,"][s, p, 0, q],
        (loop) ** (2)
        * conj(CKM[1, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["18,"][s, p, 1, q],
        (loop) ** (2)
        * conj(CKM[1, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["18,"][s, p, 1, q],
        (loop) ** (2)
        * conj(CKM[1, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["18,"][s, p, 1, q],
        (loop) ** (2)
        * conj(CKM[2, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["18,"][s, p, 2, q],
        (loop) ** (2)
        * conj(CKM[2, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["18,"][s, p, 2, q],
        (loop) ** (2)
        * conj(CKM[2, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["18,"][s, p, 2, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["18,"][s, p, q, 0],
        (loop) ** (2)
        * conj(CKM[0, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["18,"][s, p, q, 0],
        (loop) ** (2)
        * conj(CKM[0, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["18,"][s, p, q, 0],
        (loop) ** (2)
        * conj(CKM[1, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["18,"][s, p, q, 1],
        (loop) ** (2)
        * conj(CKM[1, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["18,"][s, p, q, 1],
        (loop) ** (2)
        * conj(CKM[1, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["18,"][s, p, q, 1],
        (loop) ** (2)
        * conj(CKM[2, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["18,"][s, p, q, 2],
        (loop) ** (2)
        * conj(CKM[2, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["18,"][s, p, q, 2],
        (loop) ** (2)
        * conj(CKM[2, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["18,"][s, p, q, 2],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * (ye[s]) ** (2) * X["18,"][s, p, q, r],
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (loop * X["18,"][s, p, q, r],)

    LOOP_LEVEL_MATCHING["19,"][G["qqql"][p, q, r, s]] += (
        loop * yu[r] * X["19,"][s, p, q, r],
    )

    LOOP_LEVEL_MATCHING["19,"][G["duql"][p, q, r, s]] += (
        loop * conj(CKM[0, p]) * yd[p] * X["19,"][s, 0, r, q],
        loop * conj(CKM[1, p]) * yd[p] * X["19,"][s, 1, r, q],
        loop * conj(CKM[2, p]) * yd[p] * X["19,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["19,"][G["duql"][p, q, r, s]] += (
        loop * conj(CKM[0, p]) * yd[p] * X["19,"][s, r, 0, q],
        loop * conj(CKM[1, p]) * yd[p] * X["19,"][s, r, 1, q],
        loop * conj(CKM[2, p]) * yd[p] * X["19,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["19,"][G["qque"][p, q, r, s]] += (
        loop * ye[q] * X["19,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["20,"][G["qque"][p, q, r, s]] += (
        loop * yu[p] * X["20,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["20,"][G["qque"][p, q, r, s]] += (
        loop * yu[p] * X["20,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["20,"][G["qque"][p, q, r, s]] += (
        loop * yu[p] * X["20,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["20,"][G["qqql"][p, q, r, s]] += (
        loop * ye[s] * X["20,"][s, p, q, r],
    )

    LOOP_LEVEL_MATCHING["21,"][G["duue"][p, q, r, s]] += (
        loop * yu[r] * X["21,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["21,"][G["qque"][p, q, r, s]] += (
        loop * conj(CKM[s, 0]) * yd[0] * X["21,"][q, r, p, 0],
        loop * conj(CKM[s, 1]) * yd[1] * X["21,"][q, r, p, 1],
        loop * conj(CKM[s, 2]) * yd[2] * X["21,"][q, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["21,"][G["duql"][p, q, r, s]] += (
        loop * ye[s] * X["21,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * yu[p] * yu[s] * X["22,"][q, r, p, s],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * yu[p] * yu[s] * X["22,"][q, r, p, s],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * (yu[p]) ** (2) * X["22,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * ye[s] * yu[r] * X["22,"][s, p, q, r],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * yu[p] * yu[s] * X["22,"][q, r, p, s],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * (yu[s]) ** (2) * X["22,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["22,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["22,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["22,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["22,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * yu[p] * yu[s] * X["22,"][q, r, p, s],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * (yu[s]) ** (2) * X["22,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["22,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["22,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["22,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["22,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["22,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["22,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["22,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["22,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, 0])
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["22,"][q, 0, r, p],
        (loop) ** (2)
        * conj(CKM[0, 1])
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["22,"][q, 0, r, p],
        (loop) ** (2)
        * conj(CKM[0, 2])
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["22,"][q, 0, r, p],
        (loop) ** (2)
        * conj(CKM[1, 0])
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["22,"][q, 1, r, p],
        (loop) ** (2)
        * conj(CKM[1, 1])
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["22,"][q, 1, r, p],
        (loop) ** (2)
        * conj(CKM[1, 2])
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["22,"][q, 1, r, p],
        (loop) ** (2)
        * conj(CKM[2, 0])
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["22,"][q, 2, r, p],
        (loop) ** (2)
        * conj(CKM[2, 1])
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["22,"][q, 2, r, p],
        (loop) ** (2)
        * conj(CKM[2, 2])
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["22,"][q, 2, r, p],
    )

    LOOP_LEVEL_MATCHING["22,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["22,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["22,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["22,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["22,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["22,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["22,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["22,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, 0])
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["22,"][q, r, 0, p],
        (loop) ** (2)
        * conj(CKM[0, 1])
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["22,"][q, r, 0, p],
        (loop) ** (2)
        * conj(CKM[0, 2])
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["22,"][q, r, 0, p],
        (loop) ** (2)
        * conj(CKM[1, 0])
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["22,"][q, r, 1, p],
        (loop) ** (2)
        * conj(CKM[1, 1])
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["22,"][q, r, 1, p],
        (loop) ** (2)
        * conj(CKM[1, 2])
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["22,"][q, r, 1, p],
        (loop) ** (2)
        * conj(CKM[2, 0])
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["22,"][q, r, 2, p],
        (loop) ** (2)
        * conj(CKM[2, 1])
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["22,"][q, r, 2, p],
        (loop) ** (2)
        * conj(CKM[2, 2])
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["22,"][q, r, 2, p],
    )

    LOOP_LEVEL_MATCHING["22,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["22,"][s, r, 0, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["22,"][s, r, 1, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["22,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["22,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["22,"][s, 0, r, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["22,"][s, 1, r, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["22,"][s, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["22,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["22,"][s, r, 0, q],
        (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["22,"][s, r, 1, q],
        (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["22,"][s, r, 2, q],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * (ye[q]) ** (2) * X["22,"][q, r, s, p],
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (loop * X["22,"][q, r, s, p],)

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * (yu[r]) ** (2) * X["23,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["23,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[r] * X["23,"][q, r, p, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[r] * X["23,"][q, r, p, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[r] * X["23,"][q, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["23,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * ye[s] * yu[r] * X["23,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * (yu[r]) ** (2) * X["23,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["23,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[r] * X["23,"][q, p, r, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[r] * X["23,"][q, p, r, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[r] * X["23,"][q, p, r, 2],
    )

    LOOP_LEVEL_MATCHING["23,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * ye[s] * yu[r] * X["23,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["23,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[r] * X["23,"][q, r, p, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[r] * X["23,"][q, r, p, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[r] * X["23,"][q, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["23,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[r] * X["23,"][q, p, r, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[r] * X["23,"][q, p, r, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[r] * X["23,"][q, p, r, 2],
    )

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, 0])
        * conj(CKM[0, p])
        * yd[0]
        * yd[p]
        * X["23,"][s, q, r, 0],
        (loop) ** (2)
        * conj(CKM[1, 0])
        * conj(CKM[1, p])
        * yd[0]
        * yd[p]
        * X["23,"][s, q, r, 0],
        (loop) ** (2)
        * conj(CKM[2, 0])
        * conj(CKM[2, p])
        * yd[0]
        * yd[p]
        * X["23,"][s, q, r, 0],
        (loop) ** (2)
        * conj(CKM[0, 1])
        * conj(CKM[0, p])
        * yd[1]
        * yd[p]
        * X["23,"][s, q, r, 1],
        (loop) ** (2)
        * conj(CKM[1, 1])
        * conj(CKM[1, p])
        * yd[1]
        * yd[p]
        * X["23,"][s, q, r, 1],
        (loop) ** (2)
        * conj(CKM[2, 1])
        * conj(CKM[2, p])
        * yd[1]
        * yd[p]
        * X["23,"][s, q, r, 1],
        (loop) ** (2)
        * conj(CKM[0, 2])
        * conj(CKM[0, p])
        * yd[2]
        * yd[p]
        * X["23,"][s, q, r, 2],
        (loop) ** (2)
        * conj(CKM[1, 2])
        * conj(CKM[1, p])
        * yd[2]
        * yd[p]
        * X["23,"][s, q, r, 2],
        (loop) ** (2)
        * conj(CKM[2, 2])
        * conj(CKM[2, p])
        * yd[2]
        * yd[p]
        * X["23,"][s, q, r, 2],
    )

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * (ye[s]) ** (2) * X["23,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (loop * X["23,"][s, q, r, p],)

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * yu[q] * yu[r] * X["24,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * (yu[q]) ** (2) * X["24,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["24,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["24,"][s, p, q, 0],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["24,"][s, p, q, 1],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["24,"][s, p, q, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * yu[q] * yu[r] * X["24,"][s, q, r, p],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * (yu[r]) ** (2) * X["24,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * ye[s] * yu[r] * X["24,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["24,"][G["qqql"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["24,"][s, p, q, 0],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["24,"][s, p, q, 1],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["24,"][s, p, q, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, p])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[p]
        * X["24,"][s, 0, q, 0],
        (loop) ** (2)
        * conj(CKM[0, p])
        * conj(CKM[r, 1])
        * yd[1]
        * yd[p]
        * X["24,"][s, 0, q, 1],
        (loop) ** (2)
        * conj(CKM[0, p])
        * conj(CKM[r, 2])
        * yd[2]
        * yd[p]
        * X["24,"][s, 0, q, 2],
        (loop) ** (2)
        * conj(CKM[1, p])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[p]
        * X["24,"][s, 1, q, 0],
        (loop) ** (2)
        * conj(CKM[1, p])
        * conj(CKM[r, 1])
        * yd[1]
        * yd[p]
        * X["24,"][s, 1, q, 1],
        (loop) ** (2)
        * conj(CKM[1, p])
        * conj(CKM[r, 2])
        * yd[2]
        * yd[p]
        * X["24,"][s, 1, q, 2],
        (loop) ** (2)
        * conj(CKM[2, p])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[p]
        * X["24,"][s, 2, q, 0],
        (loop) ** (2)
        * conj(CKM[2, p])
        * conj(CKM[r, 1])
        * yd[1]
        * yd[p]
        * X["24,"][s, 2, q, 1],
        (loop) ** (2)
        * conj(CKM[2, p])
        * conj(CKM[r, 2])
        * yd[2]
        * yd[p]
        * X["24,"][s, 2, q, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, 0])
        * conj(CKM[0, p])
        * yd[0]
        * yd[p]
        * X["24,"][s, r, q, 0],
        (loop) ** (2)
        * conj(CKM[1, 0])
        * conj(CKM[1, p])
        * yd[0]
        * yd[p]
        * X["24,"][s, r, q, 0],
        (loop) ** (2)
        * conj(CKM[2, 0])
        * conj(CKM[2, p])
        * yd[0]
        * yd[p]
        * X["24,"][s, r, q, 0],
        (loop) ** (2)
        * conj(CKM[0, 1])
        * conj(CKM[0, p])
        * yd[1]
        * yd[p]
        * X["24,"][s, r, q, 1],
        (loop) ** (2)
        * conj(CKM[1, 1])
        * conj(CKM[1, p])
        * yd[1]
        * yd[p]
        * X["24,"][s, r, q, 1],
        (loop) ** (2)
        * conj(CKM[2, 1])
        * conj(CKM[2, p])
        * yd[1]
        * yd[p]
        * X["24,"][s, r, q, 1],
        (loop) ** (2)
        * conj(CKM[0, 2])
        * conj(CKM[0, p])
        * yd[2]
        * yd[p]
        * X["24,"][s, r, q, 2],
        (loop) ** (2)
        * conj(CKM[1, 2])
        * conj(CKM[1, p])
        * yd[2]
        * yd[p]
        * X["24,"][s, r, q, 2],
        (loop) ** (2)
        * conj(CKM[2, 2])
        * conj(CKM[2, p])
        * yd[2]
        * yd[p]
        * X["24,"][s, r, q, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * ye[q] * X["24,"][q, r, p, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * ye[q] * X["24,"][q, r, p, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * ye[q] * X["24,"][q, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, p])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[p]
        * X["24,"][s, 0, q, 0],
        (loop) ** (2)
        * conj(CKM[0, p])
        * conj(CKM[r, 1])
        * yd[1]
        * yd[p]
        * X["24,"][s, 0, q, 1],
        (loop) ** (2)
        * conj(CKM[0, p])
        * conj(CKM[r, 2])
        * yd[2]
        * yd[p]
        * X["24,"][s, 0, q, 2],
        (loop) ** (2)
        * conj(CKM[1, p])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[p]
        * X["24,"][s, 1, q, 0],
        (loop) ** (2)
        * conj(CKM[1, p])
        * conj(CKM[r, 1])
        * yd[1]
        * yd[p]
        * X["24,"][s, 1, q, 1],
        (loop) ** (2)
        * conj(CKM[1, p])
        * conj(CKM[r, 2])
        * yd[2]
        * yd[p]
        * X["24,"][s, 1, q, 2],
        (loop) ** (2)
        * conj(CKM[2, p])
        * conj(CKM[r, 0])
        * yd[0]
        * yd[p]
        * X["24,"][s, 2, q, 0],
        (loop) ** (2)
        * conj(CKM[2, p])
        * conj(CKM[r, 1])
        * yd[1]
        * yd[p]
        * X["24,"][s, 2, q, 1],
        (loop) ** (2)
        * conj(CKM[2, p])
        * conj(CKM[r, 2])
        * yd[2]
        * yd[p]
        * X["24,"][s, 2, q, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2)
        * conj(CKM[0, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["24,"][s, 0, q, p],
        (loop) ** (2)
        * conj(CKM[0, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["24,"][s, 0, q, p],
        (loop) ** (2)
        * conj(CKM[0, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["24,"][s, 0, q, p],
        (loop) ** (2)
        * conj(CKM[1, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["24,"][s, 1, q, p],
        (loop) ** (2)
        * conj(CKM[1, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["24,"][s, 1, q, p],
        (loop) ** (2)
        * conj(CKM[1, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["24,"][s, 1, q, p],
        (loop) ** (2)
        * conj(CKM[2, 0])
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["24,"][s, 2, q, p],
        (loop) ** (2)
        * conj(CKM[2, 1])
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["24,"][s, 2, q, p],
        (loop) ** (2)
        * conj(CKM[2, 2])
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["24,"][s, 2, q, p],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duue"][p, q, r, s]] += (
        (loop) ** (2) * ye[s] * yu[r] * X["24,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["24,"][G["qque"][p, q, r, s]] += (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * ye[q] * X["24,"][q, r, p, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * ye[q] * X["24,"][q, r, p, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * ye[q] * X["24,"][q, r, p, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop) ** (2) * (ye[s]) ** (2) * X["24,"][s, r, q, p],
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (loop * X["24,"][s, r, q, p],)

    ###################
    ### Dimension 9 ###
    ###################

    LOOP_LEVEL_MATCHING["25,"][G["e~dddD"][p, q, r, s]] += (
        loop * conj(X["25,"][0, p, 0, q, r, s]),
        loop * conj(X["25,"][1, p, 1, q, r, s]),
        loop * conj(X["25,"][2, p, 2, q, r, s]),
    )

LOOP_LEVEL_MATCHING["25,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["25,"][0, p, 0, q, r, s]),
    loop * ye[p] * conj(X["25,"][1, p, 1, q, r, s]),
    loop * ye[p] * conj(X["25,"][2, p, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["25,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["25,"][0, p, 0, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["25,"][0, p, 0, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["25,"][0, p, 0, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["25,"][1, p, 1, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["25,"][1, p, 1, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["25,"][1, p, 1, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["25,"][2, p, 2, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["25,"][2, p, 2, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["25,"][2, p, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["25,"][G["e~dddD"][p, q, r, s]] += (
    loop * conj(X["25,"][p, 0, 0, q, r, s]),
    loop * conj(X["25,"][p, 1, 1, q, r, s]),
    loop * conj(X["25,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["25,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["25,"][p, 0, 0, q, r, s]),
    loop * ye[p] * conj(X["25,"][p, 1, 1, q, r, s]),
    loop * ye[p] * conj(X["25,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["25,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["25,"][p, 0, 0, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["25,"][p, 0, 0, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["25,"][p, 0, 0, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["25,"][p, 1, 1, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["25,"][p, 1, 1, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["25,"][p, 1, 1, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["25,"][p, 2, 2, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["25,"][p, 2, 2, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["25,"][p, 2, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["26,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["26,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["26,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["26,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["26,"][p, 0, q, 0]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, 0, q, 1]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 0, q, 2]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["26,"][p, 1, q, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, 1, q, 1]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 1, q, 2]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, 2, q, 0]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, 2, q, 1]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["26,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * ye[p] * conj(X["26,"][p, 0, r, s]),
    (loop) ** (2) * CKM[1, q] * yd[q] * ye[p] * conj(X["26,"][p, 1, r, s]),
    (loop) ** (2) * CKM[2, q] * yd[q] * ye[p] * conj(X["26,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["26,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["26,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["26,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["26,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 0, 0]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 0, 1]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 0, 2]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["26,"][p, q, 1, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 1, 1]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 1, 2]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, q, 2, 0]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, q, 2, 1]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["26,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * ye[p] * conj(X["26,"][p, r, 0, s]),
    (loop) ** (2) * CKM[1, q] * yd[q] * ye[p] * conj(X["26,"][p, r, 1, s]),
    (loop) ** (2) * CKM[2, q] * yd[q] * ye[p] * conj(X["26,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["26,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["26,"][p, 0, q, 0]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["26,"][p, 0, q, 1]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, 0, q, 2]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, 1, q, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, 1, q, 1]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, 1, q, 2]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 2, q, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 2, q, 1]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["26,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 0, 0]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["26,"][p, q, 0, 1]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, q, 0, 2]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 1, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 1, 1]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["26,"][p, q, 1, 2]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 2, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 2, 1]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["26,"][p, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["26,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * ye[p] * conj(X["26,"][p, r, s, 0]),
    (loop) ** (2) * CKM[1, q] * yd[q] * ye[p] * conj(X["26,"][p, r, s, 1]),
    (loop) ** (2) * CKM[2, q] * yd[q] * ye[p] * conj(X["26,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["26,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * ye[p] * conj(X["26,"][p, 0, r, s]),
    (loop) ** (2) * CKM[1, q] * yd[q] * ye[p] * conj(X["26,"][p, 1, r, s]),
    (loop) ** (2) * CKM[2, q] * yd[q] * ye[p] * conj(X["26,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["26,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * ye[p] * conj(X["26,"][p, r, 0, s]),
    (loop) ** (2) * CKM[1, q] * yd[q] * ye[p] * conj(X["26,"][p, r, 1, s]),
    (loop) ** (2) * CKM[2, q] * yd[q] * ye[p] * conj(X["26,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["26,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * ye[p] * conj(X["26,"][p, r, s, 0]),
    (loop) ** (2) * CKM[1, q] * yd[q] * ye[p] * conj(X["26,"][p, r, s, 1]),
    (loop) ** (2) * CKM[2, q] * yd[q] * ye[p] * conj(X["26,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["e~dddD"][p, q, r, s]] += (
    loop * conj(X["27,"][p, q, r, s, 0, 0]),
    loop * conj(X["27,"][p, q, r, s, 1, 1]),
    loop * conj(X["27,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["27,"][p, q, r, s, 0, 0]),
    loop * ye[p] * conj(X["27,"][p, q, r, s, 1, 1]),
    loop * ye[p] * conj(X["27,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 0, 0]),
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 1, 1]),
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 2, 2]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 0, 0]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 1, 1]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 2, 2]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 0, 0]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 1, 1]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["e~dddD"][p, q, r, s]] += (
    loop * conj(X["27,"][p, q, r, s, 0, 0]),
    loop * conj(X["27,"][p, q, r, s, 1, 1]),
    loop * conj(X["27,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["27,"][p, q, r, s, 0, 0]),
    loop * ye[p] * conj(X["27,"][p, q, r, s, 1, 1]),
    loop * ye[p] * conj(X["27,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 0, 0]),
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 1, 1]),
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 2, 2]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 0, 0]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 1, 1]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 2, 2]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 0, 0]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 1, 1]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["e~dddD"][p, q, r, s]] += (
    loop * conj(X["27,"][p, q, r, s, 0, 0]),
    loop * conj(X["27,"][p, q, r, s, 1, 1]),
    loop * conj(X["27,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["27,"][p, q, r, s, 0, 0]),
    loop * ye[p] * conj(X["27,"][p, q, r, s, 1, 1]),
    loop * ye[p] * conj(X["27,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 0, 0]),
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 1, 1]),
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 2, 2]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 0, 0]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 1, 1]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 2, 2]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 0, 0]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 1, 1]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["e~dddD"][p, q, r, s]] += (
    loop * conj(X["27,"][p, q, r, s, 0, 0]),
    loop * conj(X["27,"][p, q, r, s, 1, 1]),
    loop * conj(X["27,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["27,"][p, q, r, s, 0, 0]),
    loop * ye[p] * conj(X["27,"][p, q, r, s, 1, 1]),
    loop * ye[p] * conj(X["27,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["27,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 0, 0]),
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 1, 1]),
    loop * CKM[0, q] * yd[q] * conj(X["27,"][p, 0, r, s, 2, 2]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 0, 0]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 1, 1]),
    loop * CKM[1, q] * yd[q] * conj(X["27,"][p, 1, r, s, 2, 2]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 0, 0]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 1, 1]),
    loop * CKM[2, q] * yd[q] * conj(X["27,"][p, 2, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~dudH~"][p, q, r, s]] += (
    loop * ye[0] * conj(X["28,"][p, 0, 0, r, q, s]),
    loop * ye[1] * conj(X["28,"][p, 1, 1, r, q, s]),
    loop * ye[2] * conj(X["28,"][p, 2, 2, r, q, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~dudH~"][p, q, r, s]] += (
    loop * ye[0] * conj(X["28,"][p, 0, 0, r, q, s]),
    loop * ye[1] * conj(X["28,"][p, 1, 1, r, q, s]),
    loop * ye[2] * conj(X["28,"][p, 2, 2, r, q, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * yu[q] * conj(X["28,"][p, 0, 0, q, r, s]),
    (loop) ** (2) * ye[1] * yu[q] * conj(X["28,"][p, 1, 1, q, r, s]),
    (loop) ** (2) * ye[2] * yu[q] * conj(X["28,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * ye[p] * yu[q] * conj(X["28,"][p, 0, 0, q, r, s]),
    (loop) ** (2) * ye[1] * ye[p] * yu[q] * conj(X["28,"][p, 1, 1, q, r, s]),
    (loop) ** (2) * ye[2] * ye[p] * yu[q] * conj(X["28,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * (yu[r]) ** (2) * conj(X["28,"][p, 0, 0, r, q, s]),
    (loop) ** (2) * ye[1] * (yu[r]) ** (2) * conj(X["28,"][p, 1, 1, r, q, s]),
    (loop) ** (2) * ye[2] * (yu[r]) ** (2) * conj(X["28,"][p, 2, 2, r, q, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[0]
    * yu[0]
    * conj(X["28,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[0]
    * yu[1]
    * conj(X["28,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[0]
    * yu[2]
    * conj(X["28,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[1]
    * yu[0]
    * conj(X["28,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[1]
    * yu[1]
    * conj(X["28,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[1]
    * yu[2]
    * conj(X["28,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[2]
    * yu[0]
    * conj(X["28,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[2]
    * yu[1]
    * conj(X["28,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[2]
    * yu[2]
    * conj(X["28,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[0]
    * yu[r]
    * conj(X["28,"][p, 0, 0, r, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[0]
    * yu[r]
    * conj(X["28,"][p, 0, 0, r, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[0]
    * yu[r]
    * conj(X["28,"][p, 0, 0, r, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[1]
    * yu[r]
    * conj(X["28,"][p, 1, 1, r, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[1]
    * yu[r]
    * conj(X["28,"][p, 1, 1, r, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[1]
    * yu[r]
    * conj(X["28,"][p, 1, 1, r, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[2]
    * yu[r]
    * conj(X["28,"][p, 2, 2, r, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[2]
    * yu[r]
    * conj(X["28,"][p, 2, 2, r, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[2]
    * yu[r]
    * conj(X["28,"][p, 2, 2, r, 2, q]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * yu[q] * conj(X["28,"][p, 0, 0, q, r, s]),
    (loop) ** (2) * ye[1] * yu[q] * conj(X["28,"][p, 1, 1, q, r, s]),
    (loop) ** (2) * ye[2] * yu[q] * conj(X["28,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * ye[p] * yu[q] * conj(X["28,"][p, 0, 0, q, r, s]),
    (loop) ** (2) * ye[1] * ye[p] * yu[q] * conj(X["28,"][p, 1, 1, q, r, s]),
    (loop) ** (2) * ye[2] * ye[p] * yu[q] * conj(X["28,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * (yu[r]) ** (2) * conj(X["28,"][p, 0, 0, r, q, s]),
    (loop) ** (2) * ye[1] * (yu[r]) ** (2) * conj(X["28,"][p, 1, 1, r, q, s]),
    (loop) ** (2) * ye[2] * (yu[r]) ** (2) * conj(X["28,"][p, 2, 2, r, q, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[0]
    * yu[0]
    * conj(X["28,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[0]
    * yu[1]
    * conj(X["28,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[0]
    * yu[2]
    * conj(X["28,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[1]
    * yu[0]
    * conj(X["28,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[1]
    * yu[1]
    * conj(X["28,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[1]
    * yu[2]
    * conj(X["28,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[2]
    * yu[0]
    * conj(X["28,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[2]
    * yu[1]
    * conj(X["28,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[2]
    * yu[2]
    * conj(X["28,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["28,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[0]
    * yu[r]
    * conj(X["28,"][p, 0, 0, r, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[0]
    * yu[r]
    * conj(X["28,"][p, 0, 0, r, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[0]
    * yu[r]
    * conj(X["28,"][p, 0, 0, r, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[1]
    * yu[r]
    * conj(X["28,"][p, 1, 1, r, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[1]
    * yu[r]
    * conj(X["28,"][p, 1, 1, r, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[1]
    * yu[r]
    * conj(X["28,"][p, 1, 1, r, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[2]
    * yu[r]
    * conj(X["28,"][p, 2, 2, r, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[2]
    * yu[r]
    * conj(X["28,"][p, 2, 2, r, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[2]
    * yu[r]
    * conj(X["28,"][p, 2, 2, r, 2, q]),
)

LOOP_LEVEL_MATCHING["29,"][G["e~qddH~"][p, q, r, s]] += (
    loop * yu[0] * conj(X["29,"][p, q, 0, 0, r, s]),
    loop * yu[1] * conj(X["29,"][p, q, 1, 1, r, s]),
    loop * yu[2] * conj(X["29,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["e~qddH~"][p, q, r, s]] += (
    loop * yu[0] * conj(X["29,"][p, q, 0, 0, r, s]),
    loop * yu[1] * conj(X["29,"][p, q, 1, 1, r, s]),
    loop * yu[2] * conj(X["29,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["29,"][p, 0, 0, 0, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[1] * conj(X["29,"][p, 0, 1, 1, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[2] * conj(X["29,"][p, 0, 2, 2, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[0] * conj(X["29,"][p, 1, 0, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["29,"][p, 1, 1, 1, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[2] * conj(X["29,"][p, 1, 2, 2, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[0] * conj(X["29,"][p, 2, 0, 0, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[1] * conj(X["29,"][p, 2, 1, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["29,"][p, 2, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["29,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[0] * conj(X["29,"][p, q, 0, 0, r, s]),
    (loop) ** (2) * ye[p] * yu[1] * conj(X["29,"][p, q, 1, 1, r, s]),
    (loop) ** (2) * ye[p] * yu[2] * conj(X["29,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * yu[0] * conj(X["29,"][p, q, 0, 0, r, s]),
    (loop) ** (2) * (ye[p]) ** (2) * yu[1] * conj(X["29,"][p, q, 1, 1, r, s]),
    (loop) ** (2) * (ye[p]) ** (2) * yu[2] * conj(X["29,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[0] * yu[r] * conj(X["29,"][p, r, 0, 0, q, s]),
    (loop) ** (2) * ye[p] * yu[1] * yu[r] * conj(X["29,"][p, r, 1, 1, q, s]),
    (loop) ** (2) * ye[p] * yu[2] * yu[r] * conj(X["29,"][p, r, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, r, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, r, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, r, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, r, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, r, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, r, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, r, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, r, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, r, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["29,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["29,"][p, 0, 0, 0, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[1] * conj(X["29,"][p, 0, 1, 1, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[2] * conj(X["29,"][p, 0, 2, 2, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[0] * conj(X["29,"][p, 1, 0, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["29,"][p, 1, 1, 1, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[2] * conj(X["29,"][p, 1, 2, 2, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[0] * conj(X["29,"][p, 2, 0, 0, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[1] * conj(X["29,"][p, 2, 1, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["29,"][p, 2, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["29,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[0] * conj(X["29,"][p, q, 0, 0, r, s]),
    (loop) ** (2) * ye[p] * yu[1] * conj(X["29,"][p, q, 1, 1, r, s]),
    (loop) ** (2) * ye[p] * yu[2] * conj(X["29,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * yu[0] * conj(X["29,"][p, q, 0, 0, r, s]),
    (loop) ** (2) * (ye[p]) ** (2) * yu[1] * conj(X["29,"][p, q, 1, 1, r, s]),
    (loop) ** (2) * (ye[p]) ** (2) * yu[2] * conj(X["29,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[0] * yu[r] * conj(X["29,"][p, r, 0, 0, q, s]),
    (loop) ** (2) * ye[p] * yu[1] * yu[r] * conj(X["29,"][p, r, 1, 1, q, s]),
    (loop) ** (2) * ye[p] * yu[2] * yu[r] * conj(X["29,"][p, r, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 0, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 0, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 1, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 1, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, 2, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, 2, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["29,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, r, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, r, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[p]
    * yu[0]
    * conj(X["29,"][p, r, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, r, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, r, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[p]
    * yu[1]
    * conj(X["29,"][p, r, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, r, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, r, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[p]
    * yu[2]
    * conj(X["29,"][p, r, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * ye[0] * conj(X["30,"][0, p, 0, r, s, q]),
    loop * ye[1] * conj(X["30,"][1, p, 1, r, s, q]),
    loop * ye[2] * conj(X["30,"][2, p, 2, r, s, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * ye[0] * conj(X["30,"][p, 0, 0, r, s, q]),
    loop * ye[1] * conj(X["30,"][p, 1, 1, r, s, q]),
    loop * ye[2] * conj(X["30,"][p, 2, 2, r, s, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[0] * conj(X["30,"][0, p, 0, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[0] * conj(X["30,"][0, p, 0, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[0] * conj(X["30,"][0, p, 0, 2, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[1] * conj(X["30,"][1, p, 1, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[1] * conj(X["30,"][1, p, 1, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[1] * conj(X["30,"][1, p, 1, 2, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[2] * conj(X["30,"][2, p, 2, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[2] * conj(X["30,"][2, p, 2, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[2] * conj(X["30,"][2, p, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["30,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][0, p, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][0, p, 0, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][0, p, 0, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][1, p, 1, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][1, p, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][1, p, 1, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][2, p, 2, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][2, p, 2, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][2, p, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][0, p, 0, 0, r, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][0, p, 0, 1, r, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][0, p, 0, 2, r, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][1, p, 1, 0, r, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][1, p, 1, 1, r, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][1, p, 1, 2, r, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][2, p, 2, 0, r, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][2, p, 2, 1, r, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][2, p, 2, 2, r, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[0] * conj(X["30,"][0, p, 0, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[0] * conj(X["30,"][0, p, 0, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[0] * conj(X["30,"][0, p, 0, q, 2, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[1] * conj(X["30,"][1, p, 1, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[1] * conj(X["30,"][1, p, 1, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[1] * conj(X["30,"][1, p, 1, q, 2, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[2] * conj(X["30,"][2, p, 2, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[2] * conj(X["30,"][2, p, 2, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[2] * conj(X["30,"][2, p, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["30,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][0, p, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][0, p, 0, q, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][0, p, 0, q, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][1, p, 1, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][1, p, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][1, p, 1, q, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][2, p, 2, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][2, p, 2, q, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][2, p, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][0, p, 0, r, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][0, p, 0, r, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][0, p, 0, r, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][1, p, 1, r, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][1, p, 1, r, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][1, p, 1, r, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][2, p, 2, r, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][2, p, 2, r, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][2, p, 2, r, 2, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][0, p, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][1, p, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][2, p, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][0, p, 0, r, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][1, p, 1, r, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][2, p, 2, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[0] * conj(X["30,"][p, 0, 0, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[0] * conj(X["30,"][p, 0, 0, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[0] * conj(X["30,"][p, 0, 0, 2, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[1] * conj(X["30,"][p, 1, 1, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[1] * conj(X["30,"][p, 1, 1, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[1] * conj(X["30,"][p, 1, 1, 2, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[2] * conj(X["30,"][p, 2, 2, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[2] * conj(X["30,"][p, 2, 2, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[2] * conj(X["30,"][p, 2, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["30,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][p, 0, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][p, 0, 0, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][p, 0, 0, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][p, 1, 1, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][p, 1, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][p, 1, 1, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][p, 2, 2, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][p, 2, 2, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][p, 2, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][p, 0, 0, 0, r, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][p, 0, 0, 1, r, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][p, 0, 0, 2, r, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][p, 1, 1, 0, r, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][p, 1, 1, 1, r, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][p, 1, 1, 2, r, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][p, 2, 2, 0, r, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][p, 2, 2, 1, r, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][p, 2, 2, 2, r, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[0] * conj(X["30,"][p, 0, 0, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[0] * conj(X["30,"][p, 0, 0, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[0] * conj(X["30,"][p, 0, 0, q, 2, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[1] * conj(X["30,"][p, 1, 1, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[1] * conj(X["30,"][p, 1, 1, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[1] * conj(X["30,"][p, 1, 1, q, 2, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[2] * conj(X["30,"][p, 2, 2, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[2] * conj(X["30,"][p, 2, 2, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[2] * conj(X["30,"][p, 2, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["30,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][p, 0, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][p, 0, 0, q, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["30,"][p, 0, 0, q, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][p, 1, 1, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][p, 1, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["30,"][p, 1, 1, q, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][p, 2, 2, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][p, 2, 2, q, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["30,"][p, 2, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][p, 0, 0, r, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][p, 0, 0, r, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[0]
    * yu[r]
    * conj(X["30,"][p, 0, 0, r, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][p, 1, 1, r, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][p, 1, 1, r, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[1]
    * yu[r]
    * conj(X["30,"][p, 1, 1, r, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][p, 2, 2, r, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][p, 2, 2, r, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[2]
    * yu[r]
    * conj(X["30,"][p, 2, 2, r, 2, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[0]
    * conj(X["30,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[1]
    * conj(X["30,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[2]
    * conj(X["30,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["30,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[0]
    * conj(X["30,"][p, 0, 0, r, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[1]
    * conj(X["30,"][p, 1, 1, r, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[2]
    * conj(X["30,"][p, 2, 2, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["31,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["31,"][0, p, 0, q, r, s]),
    loop * conj(X["31,"][1, p, 1, q, r, s]),
    loop * conj(X["31,"][2, p, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["31,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["31,"][0, p, 0, q, r, s]),
    loop * ye[p] * conj(X["31,"][1, p, 1, q, r, s]),
    loop * ye[p] * conj(X["31,"][2, p, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["31,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["31,"][0, p, 0, r, q, s]),
    loop * yu[r] * conj(X["31,"][1, p, 1, r, q, s]),
    loop * yu[r] * conj(X["31,"][2, p, 2, r, q, s]),
)

LOOP_LEVEL_MATCHING["31,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["31,"][0, p, 0, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["31,"][0, p, 0, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["31,"][0, p, 0, 2, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["31,"][1, p, 1, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["31,"][1, p, 1, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["31,"][1, p, 1, 2, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["31,"][2, p, 2, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["31,"][2, p, 2, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["31,"][2, p, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["31,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["31,"][0, p, 0, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["31,"][0, p, 0, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["31,"][0, p, 0, r, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["31,"][1, p, 1, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["31,"][1, p, 1, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["31,"][1, p, 1, r, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["31,"][2, p, 2, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["31,"][2, p, 2, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["31,"][2, p, 2, r, 2, q]),
)

LOOP_LEVEL_MATCHING["31,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["31,"][p, 0, 0, q, r, s]),
    loop * conj(X["31,"][p, 1, 1, q, r, s]),
    loop * conj(X["31,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["31,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["31,"][p, 0, 0, q, r, s]),
    loop * ye[p] * conj(X["31,"][p, 1, 1, q, r, s]),
    loop * ye[p] * conj(X["31,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["31,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["31,"][p, 0, 0, r, q, s]),
    loop * yu[r] * conj(X["31,"][p, 1, 1, r, q, s]),
    loop * yu[r] * conj(X["31,"][p, 2, 2, r, q, s]),
)

LOOP_LEVEL_MATCHING["31,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["31,"][p, 0, 0, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["31,"][p, 0, 0, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["31,"][p, 0, 0, 2, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["31,"][p, 1, 1, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["31,"][p, 1, 1, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["31,"][p, 1, 1, 2, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["31,"][p, 2, 2, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["31,"][p, 2, 2, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["31,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["31,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["31,"][p, 0, 0, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["31,"][p, 0, 0, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["31,"][p, 0, 0, r, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["31,"][p, 1, 1, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["31,"][p, 1, 1, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["31,"][p, 1, 1, r, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["31,"][p, 2, 2, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["31,"][p, 2, 2, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["31,"][p, 2, 2, r, 2, q]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[0, 0] * yd[0] * conj(X["32,"][p, 0, q, r, s, 0]),
    loop * CKM[0, 1] * yd[1] * conj(X["32,"][p, 0, q, r, s, 1]),
    loop * CKM[0, 2] * yd[2] * conj(X["32,"][p, 0, q, r, s, 2]),
    loop * CKM[1, 0] * yd[0] * conj(X["32,"][p, 1, q, r, s, 0]),
    loop * CKM[1, 1] * yd[1] * conj(X["32,"][p, 1, q, r, s, 1]),
    loop * CKM[1, 2] * yd[2] * conj(X["32,"][p, 1, q, r, s, 2]),
    loop * CKM[2, 0] * yd[0] * conj(X["32,"][p, 2, q, r, s, 0]),
    loop * CKM[2, 1] * yd[1] * conj(X["32,"][p, 2, q, r, s, 1]),
    loop * CKM[2, 2] * yd[2] * conj(X["32,"][p, 2, q, r, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * conj(X["32,"][p, 0, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 0, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 0, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 0, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 0, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * conj(X["32,"][p, 1, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 1, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 1, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 1, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 1, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * conj(X["32,"][p, 2, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 2, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 2, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 2, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 2, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, r, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 0, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 0, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 0, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 0, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 0, 2, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 1, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 1, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 1, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 1, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 1, 2, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 2, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 2, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 2, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 2, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 2, 2, r, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 0, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 0, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 0, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 1, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 1, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 1, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 2, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 2, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 2, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 2, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 2, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * (CKM[0, 0]) ** (2)
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 0]
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 0]
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 1, q, s, 0]),
    (loop) ** (2)
    * (CKM[0, 1]) ** (2)
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 0, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 1]
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, q, s, 1]),
    (loop) ** (2)
    * (CKM[0, 2]) ** (2)
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 0, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 1, 0, q, s, 0]),
    (loop) ** (2)
    * (CKM[1, 0]) ** (2)
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 0]
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * (CKM[1, 1]) ** (2)
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 1]
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, q, s, 2]),
    (loop) ** (2)
    * (CKM[1, 2]) ** (2)
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 1, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 2, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 0]
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 0, q, s, 0]),
    (loop) ** (2)
    * (CKM[2, 0]) ** (2)
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 2, 1, q, s, 1]),
    (loop) ** (2)
    * (CKM[2, 1]) ** (2)
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, q, s, 2]),
    (loop) ** (2)
    * (CKM[2, 2]) ** (2)
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 2, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 0, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 0, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 0, 2, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 1, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 1, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 1, 2, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 2, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 2, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 2, 2, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * conj(X["32,"][p, 0, r, 0, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 0, r, 0, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 0, r, 0, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 0, r, 1, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, r, 1, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, r, 1, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 0, r, 2, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, r, 2, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, r, 2, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * conj(X["32,"][p, 1, r, 0, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 1, r, 0, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 1, r, 0, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 1, r, 1, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, r, 1, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, r, 1, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 1, r, 2, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, r, 2, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, r, 2, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * conj(X["32,"][p, 2, r, 0, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 2, r, 0, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 2, r, 0, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 2, r, 1, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, r, 1, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, r, 1, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 2, r, 2, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, r, 2, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, r, 2, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 0, r, 0, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 0, r, 0, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, r, 0, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 0, r, 1, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 0, r, 1, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, r, 1, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, r, 2, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, r, 2, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 0, r, 2, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 1, r, 0, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 1, r, 0, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, r, 0, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 1, r, 1, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 1, r, 1, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, r, 1, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, r, 2, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, r, 2, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 1, r, 2, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 2, r, 0, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 2, r, 0, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, r, 0, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 2, r, 1, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 2, r, 1, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, r, 1, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, r, 2, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, r, 2, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 2, r, 2, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 0, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 0, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 0, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 0, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 0, q, 2, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 1, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 1, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 1, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 1, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 1, q, 2, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 2, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 2, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 2, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 2, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 2, q, 2, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * (CKM[0, 0]) ** (2)
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 0, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 0]
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 0]
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, 1, s, 0]),
    (loop) ** (2)
    * (CKM[0, 1]) ** (2)
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 0, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 1]
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, 2, s, 1]),
    (loop) ** (2)
    * (CKM[0, 2]) ** (2)
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, 2, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, 2, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 0, q, 2, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 1, q, 0, s, 0]),
    (loop) ** (2)
    * (CKM[1, 0]) ** (2)
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 0]
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, q, 1, s, 1]),
    (loop) ** (2)
    * (CKM[1, 1]) ** (2)
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 1, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 1]
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, 2, s, 2]),
    (loop) ** (2)
    * (CKM[1, 2]) ** (2)
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, 2, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 1, q, 2, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 2, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 0]
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, q, 0, s, 0]),
    (loop) ** (2)
    * (CKM[2, 0]) ** (2)
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, 0, s, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, 0, s, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, 0, s, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, 1, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 2, q, 1, s, 1]),
    (loop) ** (2)
    * (CKM[2, 1]) ** (2)
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, 1, s, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, 1, s, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, 2, s, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, 2, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, 2, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, 2, s, 2]),
    (loop) ** (2)
    * (CKM[2, 2]) ** (2)
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 2, q, 2, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 0, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 0, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 0, 2, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 1, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 1, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 1, 2, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 2, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 2, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 2, 2, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * conj(X["32,"][p, 0, r, s, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 0, r, s, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 0, r, s, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 0, r, s, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, r, s, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, r, s, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 0, r, s, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, r, s, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, r, s, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * conj(X["32,"][p, 1, r, s, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 1, r, s, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 1, r, s, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 1, r, s, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, r, s, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, r, s, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 1, r, s, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, r, s, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, r, s, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * conj(X["32,"][p, 2, r, s, 0, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 2, r, s, 0, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 2, r, s, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * conj(X["32,"][p, 2, r, s, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, r, s, 1, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, r, s, 1, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * conj(X["32,"][p, 2, r, s, 2, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, r, s, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 0, r, s, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 0, r, s, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, r, s, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 0, r, s, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 0, r, s, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, r, s, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, r, s, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 0, r, s, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 0, r, s, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 1, r, s, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 1, r, s, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, r, s, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 1, r, s, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 1, r, s, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, r, s, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, r, s, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 1, r, s, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 1, r, s, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 2, r, s, 0, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 2, r, s, 0, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, r, s, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["32,"][p, 2, r, s, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 2, r, s, 1, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, r, s, 1, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, r, s, 2, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["32,"][p, 2, r, s, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["32,"][p, 2, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 0, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 0, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 0, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 0, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 0, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 0, q, s, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 1, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 1, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 1, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 1, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 1, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 1, q, s, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 2, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 2, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["32,"][p, 2, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 2, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["32,"][p, 2, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["32,"][p, 2, q, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * (CKM[0, 0]) ** (2)
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 0, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 0]
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 0]
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 1, 0]),
    (loop) ** (2)
    * (CKM[0, 1]) ** (2)
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 0, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 1]
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, s, 2, 1]),
    (loop) ** (2)
    * (CKM[0, 2]) ** (2)
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, s, 2, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, q, s, 2, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 0, q, s, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 1, q, s, 0, 0]),
    (loop) ** (2)
    * (CKM[1, 0]) ** (2)
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 0]
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, q, s, 1, 1]),
    (loop) ** (2)
    * (CKM[1, 1]) ** (2)
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 1, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 1]
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, s, 2, 2]),
    (loop) ** (2)
    * (CKM[1, 2]) ** (2)
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, q, s, 2, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 1, q, s, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 2, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 0]
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, q, s, 0, 0]),
    (loop) ** (2)
    * (CKM[2, 0]) ** (2)
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 1]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 1]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 2]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, s, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 2, q, s, 1, 1]),
    (loop) ** (2)
    * (CKM[2, 1]) ** (2)
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 2]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, s, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, s, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, 2]
    * CKM[r, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, s, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, s, 2, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, q, s, 2, 2]),
    (loop) ** (2)
    * (CKM[2, 2]) ** (2)
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 2, q, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 0, 0, q, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 0, q, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 0, q, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 0, q, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 0, q, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 0, q, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 0, q, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 0, q, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 0, q, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 0, 1, q, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 1, q, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 1, q, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 0, 1, q, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 0, 1, q, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 1, q, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 1, q, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 1, q, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 1, q, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 2, q, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 2, q, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, q, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 0, 2, q, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 0, 2, q, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, q, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, q, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 0, 2, q, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 0, 2, q, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 1, 0, q, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 0, q, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 0, q, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 0, q, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 0, q, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 0, q, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 0, q, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 0, q, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 0, q, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 1, 1, q, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 1, q, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 1, q, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 1, 1, q, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 1, 1, q, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 1, q, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 1, q, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 1, q, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 1, q, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 2, q, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 2, q, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, q, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 1, 2, q, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 1, 2, q, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, q, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, q, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 1, 2, q, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 1, 2, q, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["32,"][p, 2, 0, q, 0, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 0, q, 0, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 0, q, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 0, q, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 0, q, 1, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 0, q, 1, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 0, q, 2, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 0, q, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 0, q, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["32,"][p, 2, 1, q, 0, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 1, q, 0, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 1, q, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * CKM[s, 1]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["32,"][p, 2, 1, q, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["32,"][p, 2, 1, q, 1, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 1, q, 1, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 1, q, 2, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 1, q, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 1, q, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 2, q, 0, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 2, q, 0, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, q, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[0]
    * yd[1]
    * yd[2]
    * conj(X["32,"][p, 2, 2, q, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["32,"][p, 2, 2, q, 1, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, q, 1, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, q, 2, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * CKM[s, 2]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["32,"][p, 2, 2, q, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["32,"][p, 2, 2, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * yd[0] * ye[p] * conj(X["32,"][p, 0, q, r, s, 0]),
    (loop) ** (2) * CKM[0, 1] * yd[1] * ye[p] * conj(X["32,"][p, 0, q, r, s, 1]),
    (loop) ** (2) * CKM[0, 2] * yd[2] * ye[p] * conj(X["32,"][p, 0, q, r, s, 2]),
    (loop) ** (2) * CKM[1, 0] * yd[0] * ye[p] * conj(X["32,"][p, 1, q, r, s, 0]),
    (loop) ** (2) * CKM[1, 1] * yd[1] * ye[p] * conj(X["32,"][p, 1, q, r, s, 1]),
    (loop) ** (2) * CKM[1, 2] * yd[2] * ye[p] * conj(X["32,"][p, 1, q, r, s, 2]),
    (loop) ** (2) * CKM[2, 0] * yd[0] * ye[p] * conj(X["32,"][p, 2, q, r, s, 0]),
    (loop) ** (2) * CKM[2, 1] * yd[1] * ye[p] * conj(X["32,"][p, 2, q, r, s, 1]),
    (loop) ** (2) * CKM[2, 2] * yd[2] * ye[p] * conj(X["32,"][p, 2, q, r, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["32,"][p, 0, q, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["32,"][p, 0, q, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["32,"][p, 0, q, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["32,"][p, 1, q, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["32,"][p, 1, q, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["32,"][p, 1, q, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["32,"][p, 2, q, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["32,"][p, 2, q, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["32,"][p, 2, q, r, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 0, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 0, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 0, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 0, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 0, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 0, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 0, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 0, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 0, 2, r, s, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 1, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 1, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 1, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 1, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 1, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 1, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 1, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 1, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 1, 2, r, s, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 2, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 2, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 2, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 2, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 2, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 2, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 2, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 2, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["32,"][p, 2, 2, r, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["32,"][p, q, 0, r, s, 0]),
    loop * conj(X["32,"][p, q, 1, r, s, 1]),
    loop * conj(X["32,"][p, q, 2, r, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["32,"][p, q, 0, r, s, 0]),
    loop * ye[p] * conj(X["32,"][p, q, 1, r, s, 1]),
    loop * ye[p] * conj(X["32,"][p, q, 2, r, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["32,"][p, r, 0, q, s, 0]),
    loop * yu[r] * conj(X["32,"][p, r, 1, q, s, 1]),
    loop * yu[r] * conj(X["32,"][p, r, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["32,"][p, 0, 0, q, s, 0]),
    loop * CKM[r, 0] * yd[0] * conj(X["32,"][p, 0, 1, q, s, 1]),
    loop * CKM[r, 0] * yd[0] * conj(X["32,"][p, 0, 2, q, s, 2]),
    loop * CKM[r, 1] * yd[1] * conj(X["32,"][p, 1, 0, q, s, 0]),
    loop * CKM[r, 1] * yd[1] * conj(X["32,"][p, 1, 1, q, s, 1]),
    loop * CKM[r, 1] * yd[1] * conj(X["32,"][p, 1, 2, q, s, 2]),
    loop * CKM[r, 2] * yd[2] * conj(X["32,"][p, 2, 0, q, s, 0]),
    loop * CKM[r, 2] * yd[2] * conj(X["32,"][p, 2, 1, q, s, 1]),
    loop * CKM[r, 2] * yd[2] * conj(X["32,"][p, 2, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["32,"][p, r, 0, 0, q, 0]),
    loop * CKM[s, 1] * yd[1] * conj(X["32,"][p, r, 0, 1, q, 0]),
    loop * CKM[s, 2] * yd[2] * conj(X["32,"][p, r, 0, 2, q, 0]),
    loop * CKM[s, 0] * yd[0] * conj(X["32,"][p, r, 1, 0, q, 1]),
    loop * CKM[s, 1] * yd[1] * conj(X["32,"][p, r, 1, 1, q, 1]),
    loop * CKM[s, 2] * yd[2] * conj(X["32,"][p, r, 1, 2, q, 1]),
    loop * CKM[s, 0] * yd[0] * conj(X["32,"][p, r, 2, 0, q, 2]),
    loop * CKM[s, 1] * yd[1] * conj(X["32,"][p, r, 2, 1, q, 2]),
    loop * CKM[s, 2] * yd[2] * conj(X["32,"][p, r, 2, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["32,"][p, q, r, 0, s, 0]),
    loop * conj(X["32,"][p, q, r, 1, s, 1]),
    loop * conj(X["32,"][p, q, r, 2, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["32,"][p, q, r, 0, s, 0]),
    loop * ye[p] * conj(X["32,"][p, q, r, 1, s, 1]),
    loop * ye[p] * conj(X["32,"][p, q, r, 2, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["32,"][p, r, q, 0, s, 0]),
    loop * yu[r] * conj(X["32,"][p, r, q, 1, s, 1]),
    loop * yu[r] * conj(X["32,"][p, r, q, 2, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["32,"][p, 0, q, 0, s, 0]),
    loop * CKM[r, 0] * yd[0] * conj(X["32,"][p, 0, q, 1, s, 1]),
    loop * CKM[r, 0] * yd[0] * conj(X["32,"][p, 0, q, 2, s, 2]),
    loop * CKM[r, 1] * yd[1] * conj(X["32,"][p, 1, q, 0, s, 0]),
    loop * CKM[r, 1] * yd[1] * conj(X["32,"][p, 1, q, 1, s, 1]),
    loop * CKM[r, 1] * yd[1] * conj(X["32,"][p, 1, q, 2, s, 2]),
    loop * CKM[r, 2] * yd[2] * conj(X["32,"][p, 2, q, 0, s, 0]),
    loop * CKM[r, 2] * yd[2] * conj(X["32,"][p, 2, q, 1, s, 1]),
    loop * CKM[r, 2] * yd[2] * conj(X["32,"][p, 2, q, 2, s, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["32,"][p, r, 0, 0, q, 0]),
    loop * CKM[s, 0] * yd[0] * conj(X["32,"][p, r, 0, 1, q, 1]),
    loop * CKM[s, 0] * yd[0] * conj(X["32,"][p, r, 0, 2, q, 2]),
    loop * CKM[s, 1] * yd[1] * conj(X["32,"][p, r, 1, 0, q, 0]),
    loop * CKM[s, 1] * yd[1] * conj(X["32,"][p, r, 1, 1, q, 1]),
    loop * CKM[s, 1] * yd[1] * conj(X["32,"][p, r, 1, 2, q, 2]),
    loop * CKM[s, 2] * yd[2] * conj(X["32,"][p, r, 2, 0, q, 0]),
    loop * CKM[s, 2] * yd[2] * conj(X["32,"][p, r, 2, 1, q, 1]),
    loop * CKM[s, 2] * yd[2] * conj(X["32,"][p, r, 2, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["32,"][p, q, r, s, 0, 0]),
    loop * conj(X["32,"][p, q, r, s, 1, 1]),
    loop * conj(X["32,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["32,"][p, q, r, s, 0, 0]),
    loop * ye[p] * conj(X["32,"][p, q, r, s, 1, 1]),
    loop * ye[p] * conj(X["32,"][p, q, r, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["32,"][p, r, q, s, 0, 0]),
    loop * yu[r] * conj(X["32,"][p, r, q, s, 1, 1]),
    loop * yu[r] * conj(X["32,"][p, r, q, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["32,"][p, 0, q, s, 0, 0]),
    loop * CKM[r, 0] * yd[0] * conj(X["32,"][p, 0, q, s, 1, 1]),
    loop * CKM[r, 0] * yd[0] * conj(X["32,"][p, 0, q, s, 2, 2]),
    loop * CKM[r, 1] * yd[1] * conj(X["32,"][p, 1, q, s, 0, 0]),
    loop * CKM[r, 1] * yd[1] * conj(X["32,"][p, 1, q, s, 1, 1]),
    loop * CKM[r, 1] * yd[1] * conj(X["32,"][p, 1, q, s, 2, 2]),
    loop * CKM[r, 2] * yd[2] * conj(X["32,"][p, 2, q, s, 0, 0]),
    loop * CKM[r, 2] * yd[2] * conj(X["32,"][p, 2, q, s, 1, 1]),
    loop * CKM[r, 2] * yd[2] * conj(X["32,"][p, 2, q, s, 2, 2]),
)

LOOP_LEVEL_MATCHING["32,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["32,"][p, r, 0, q, 0, 0]),
    loop * CKM[s, 0] * yd[0] * conj(X["32,"][p, r, 0, q, 1, 1]),
    loop * CKM[s, 0] * yd[0] * conj(X["32,"][p, r, 0, q, 2, 2]),
    loop * CKM[s, 1] * yd[1] * conj(X["32,"][p, r, 1, q, 0, 0]),
    loop * CKM[s, 1] * yd[1] * conj(X["32,"][p, r, 1, q, 1, 1]),
    loop * CKM[s, 1] * yd[1] * conj(X["32,"][p, r, 1, q, 2, 2]),
    loop * CKM[s, 2] * yd[2] * conj(X["32,"][p, r, 2, q, 0, 0]),
    loop * CKM[s, 2] * yd[2] * conj(X["32,"][p, r, 2, q, 1, 1]),
    loop * CKM[s, 2] * yd[2] * conj(X["32,"][p, r, 2, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["33,"][G["e~dddD"][p, q, r, s]] += (
    loop * conj(X["33,"][p, 0, 0, q, r, s]),
    loop * conj(X["33,"][p, 1, 1, q, r, s]),
    loop * conj(X["33,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["33,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["33,"][p, 0, 0, q, r, s]),
    loop * ye[p] * conj(X["33,"][p, 1, 1, q, r, s]),
    loop * ye[p] * conj(X["33,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["33,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["33,"][p, 0, 0, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["33,"][p, 0, 0, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["33,"][p, 0, 0, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["33,"][p, 1, 1, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["33,"][p, 1, 1, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["33,"][p, 1, 1, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["33,"][p, 2, 2, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["33,"][p, 2, 2, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["33,"][p, 2, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, s] * yd[s] * conj(X["34,"][p, 0, q, r]),
    loop * CKM[1, s] * yd[s] * conj(X["34,"][p, 1, q, r]),
    loop * CKM[2, s] * yd[s] * conj(X["34,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, s] * yd[s] * conj(X["34,"][p, q, 0, r]),
    loop * CKM[1, s] * yd[s] * conj(X["34,"][p, q, 1, r]),
    loop * CKM[2, s] * yd[s] * conj(X["34,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["34,"][p, r, s, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["34,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["34,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["34,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["34,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["34,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["34,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["34,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["34,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["34,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, r]
    * CKM[0, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, r]
    * CKM[1, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[1, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * CKM[2, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, r]
    * CKM[1, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, r]
    * CKM[1, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["34,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["34,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["34,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, 0, r, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, 1, r, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["34,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["34,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["34,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["34,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["34,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["34,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["34,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["34,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["34,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, r]
    * CKM[0, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[1, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * CKM[2, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, r]
    * CKM[1, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, r]
    * CKM[1, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, r]
    * CKM[1, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[2, r]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, r]
    * CKM[2, s]
    * yd[q]
    * yd[r]
    * yd[s]
    * conj(X["34,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["34,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["34,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["34,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, r, 0, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, r, 1, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["34,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["34,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["34,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, 0, r, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, 1, r, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["34,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["34,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["34,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * (ye[p]) ** (2) * conj(X["34,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, r, 0, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, r, 1, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * yu[r] * conj(X["34,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["34,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["34,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * ye[p]
    * conj(X["34,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[0] * conj(X["35,"][p, 0, 0, q, r, s]),
    loop * ye[1] * conj(X["35,"][p, 1, 1, q, r, s]),
    loop * ye[2] * conj(X["35,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[0] * conj(X["35,"][p, 0, 0, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[0] * conj(X["35,"][p, 0, 0, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[0] * conj(X["35,"][p, 0, 0, 2, r, s]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[1] * conj(X["35,"][p, 1, 1, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[1] * conj(X["35,"][p, 1, 1, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[1] * conj(X["35,"][p, 1, 1, 2, r, s]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[2] * conj(X["35,"][p, 2, 2, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[2] * conj(X["35,"][p, 2, 2, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[2] * conj(X["35,"][p, 2, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, 0, r, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, 1, r, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, 2, r, s]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, 0, r, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, 1, r, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, 2, r, s]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, 0, r, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, 1, r, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[0]
    * yu[r]
    * conj(X["35,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[0]
    * yu[r]
    * conj(X["35,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[0]
    * yu[r]
    * conj(X["35,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[1]
    * yu[r]
    * conj(X["35,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[1]
    * yu[r]
    * conj(X["35,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[1]
    * yu[r]
    * conj(X["35,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[2]
    * yu[r]
    * conj(X["35,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[2]
    * yu[r]
    * conj(X["35,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[2]
    * yu[r]
    * conj(X["35,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[0] * conj(X["35,"][p, 0, 0, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[0] * conj(X["35,"][p, 0, 0, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[0] * conj(X["35,"][p, 0, 0, r, 2, s]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[1] * conj(X["35,"][p, 1, 1, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[1] * conj(X["35,"][p, 1, 1, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[1] * conj(X["35,"][p, 1, 1, r, 2, s]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[2] * conj(X["35,"][p, 2, 2, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[2] * conj(X["35,"][p, 2, 2, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[2] * conj(X["35,"][p, 2, 2, r, 2, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, r, 0, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, r, 1, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, r, 2, s]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, r, 0, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, r, 1, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, r, 2, s]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, r, 0, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, r, 1, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, r, 2, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[0]
    * yu[r]
    * conj(X["35,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[0]
    * yu[r]
    * conj(X["35,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[0]
    * yu[r]
    * conj(X["35,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[1]
    * yu[r]
    * conj(X["35,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[1]
    * yu[r]
    * conj(X["35,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[1]
    * yu[r]
    * conj(X["35,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[2]
    * yu[r]
    * conj(X["35,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[2]
    * yu[r]
    * conj(X["35,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[2]
    * yu[r]
    * conj(X["35,"][p, 2, 2, q, 2, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, 2, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[0] * conj(X["35,"][p, 0, 0, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[0] * conj(X["35,"][p, 0, 0, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[0] * conj(X["35,"][p, 0, 0, r, s, 2]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[1] * conj(X["35,"][p, 1, 1, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[1] * conj(X["35,"][p, 1, 1, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[1] * conj(X["35,"][p, 1, 1, r, s, 2]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[2] * conj(X["35,"][p, 2, 2, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[2] * conj(X["35,"][p, 2, 2, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[2] * conj(X["35,"][p, 2, 2, r, s, 2]),
)

LOOP_LEVEL_MATCHING["35,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, r, s, 2]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[0]
    * yu[r]
    * conj(X["35,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[0]
    * yu[r]
    * conj(X["35,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[0]
    * yu[r]
    * conj(X["35,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[1]
    * yu[r]
    * conj(X["35,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[1]
    * yu[r]
    * conj(X["35,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[1]
    * yu[r]
    * conj(X["35,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[2]
    * yu[r]
    * conj(X["35,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[2]
    * yu[r]
    * conj(X["35,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[2]
    * yu[r]
    * conj(X["35,"][p, 2, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[0]
    * conj(X["35,"][p, 0, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[1]
    * conj(X["35,"][p, 1, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[2]
    * conj(X["35,"][p, 2, 2, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["35,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * ye[p] * conj(X["35,"][p, 0, 0, q, r, s]),
    (loop) ** (2) * ye[1] * ye[p] * conj(X["35,"][p, 1, 1, q, r, s]),
    (loop) ** (2) * ye[2] * ye[p] * conj(X["35,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * (ye[p]) ** (2) * conj(X["35,"][p, 0, 0, q, r, s]),
    (loop) ** (2) * ye[1] * (ye[p]) ** (2) * conj(X["35,"][p, 1, 1, q, r, s]),
    (loop) ** (2) * ye[2] * (ye[p]) ** (2) * conj(X["35,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * yd[q]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, 0, r, s]),
    (loop) ** (2)
    * CKM[1, q]
    * yd[q]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, 1, r, s]),
    (loop) ** (2)
    * CKM[2, q]
    * yd[q]
    * ye[0]
    * ye[p]
    * conj(X["35,"][p, 0, 0, 2, r, s]),
    (loop) ** (2)
    * CKM[0, q]
    * yd[q]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, 0, r, s]),
    (loop) ** (2)
    * CKM[1, q]
    * yd[q]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, 1, r, s]),
    (loop) ** (2)
    * CKM[2, q]
    * yd[q]
    * ye[1]
    * ye[p]
    * conj(X["35,"][p, 1, 1, 2, r, s]),
    (loop) ** (2)
    * CKM[0, q]
    * yd[q]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, 0, r, s]),
    (loop) ** (2)
    * CKM[1, q]
    * yd[q]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, 1, r, s]),
    (loop) ** (2)
    * CKM[2, q]
    * yd[q]
    * ye[2]
    * ye[p]
    * conj(X["35,"][p, 2, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["e~dddD"][p, q, r, s]] += (
    loop * conj(X["35,"][0, 0, p, q, r, s]),
    loop * conj(X["35,"][1, 1, p, q, r, s]),
    loop * conj(X["35,"][2, 2, p, q, r, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["35,"][0, 0, p, q, r, s]),
    loop * ye[p] * conj(X["35,"][1, 1, p, q, r, s]),
    loop * ye[p] * conj(X["35,"][2, 2, p, q, r, s]),
)

LOOP_LEVEL_MATCHING["35,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["35,"][0, 0, p, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["35,"][0, 0, p, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["35,"][0, 0, p, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["35,"][1, 1, p, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["35,"][1, 1, p, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["35,"][1, 1, p, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["35,"][2, 2, p, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["35,"][2, 2, p, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["35,"][2, 2, p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    loop * conj(X["36,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * yu[r] * conj(X["36,"][p, 0, q, s]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * yu[r] * conj(X["36,"][p, 1, q, s]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * yu[r] * conj(X["36,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, q, 0]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 0, q, 1]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 0, q, 2]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 1, q, 0]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, q, 1]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 1, q, 2]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 2, q, 0]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 2, q, 1]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["36,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["36,"][p, 0, q, r]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["36,"][p, 0, q, r]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["36,"][p, 1, q, r]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["36,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["36,"][p, 1, q, r]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["36,"][p, 2, q, r]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["36,"][p, 2, q, r]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["36,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * conj(X["36,"][p, 0, r, s]),
    loop * loop * CKM[q, 1] * yd[1] * conj(X["36,"][p, 1, r, s]),
    loop * loop * CKM[q, 2] * yd[2] * conj(X["36,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, 0, r, s]),
    loop * loop * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, 1, r, s]),
    loop * loop * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * yd[0] * yu[r] * conj(X["36,"][p, 0, q, s]),
    loop * loop * CKM[r, 1] * yd[1] * yu[r] * conj(X["36,"][p, 1, q, s]),
    loop * loop * CKM[r, 2] * yd[2] * yu[r] * conj(X["36,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, 0] * CKM[r, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, q, s]),
    loop * loop * CKM[1, 0] * CKM[r, 1] * yd[0] * yd[1] * conj(X["36,"][p, 0, q, s]),
    loop * loop * CKM[2, 0] * CKM[r, 2] * yd[0] * yd[2] * conj(X["36,"][p, 0, q, s]),
    loop * loop * CKM[0, 1] * CKM[r, 0] * yd[0] * yd[1] * conj(X["36,"][p, 1, q, s]),
    loop * loop * CKM[1, 1] * CKM[r, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, q, s]),
    loop * loop * CKM[2, 1] * CKM[r, 2] * yd[1] * yd[2] * conj(X["36,"][p, 1, q, s]),
    loop * loop * CKM[0, 2] * CKM[r, 0] * yd[0] * yd[2] * conj(X["36,"][p, 2, q, s]),
    loop * loop * CKM[1, 2] * CKM[r, 1] * yd[1] * yd[2] * conj(X["36,"][p, 2, q, s]),
    loop * loop * CKM[2, 2] * CKM[r, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, 0, q]),
    loop * loop * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 0, 1, q]),
    loop * loop * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 0, 2, q]),
    loop * loop * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 1, 0, q]),
    loop * loop * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, 1, q]),
    loop * loop * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 1, 2, q]),
    loop * loop * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 2, 0, q]),
    loop * loop * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 2, 1, q]),
    loop * loop * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * yu[r] * conj(X["36,"][p, q, 0, s]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * yu[r] * conj(X["36,"][p, q, 1, s]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * yu[r] * conj(X["36,"][p, q, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, q, 0, 0]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, q, 0, 1]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, q, 0, 2]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, q, 1, 0]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, q, 1, 1]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, q, 1, 2]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, q, 2, 0]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, q, 2, 1]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["36,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["36,"][p, q, 0, r]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["36,"][p, q, 0, r]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["36,"][p, q, 1, r]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["36,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["36,"][p, q, 1, r]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["36,"][p, q, 2, r]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["36,"][p, q, 2, r]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["36,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * conj(X["36,"][p, r, 0, s]),
    loop * loop * CKM[q, 1] * yd[1] * conj(X["36,"][p, r, 1, s]),
    loop * loop * CKM[q, 2] * yd[2] * conj(X["36,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, r, 0, s]),
    loop * loop * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, r, 1, s]),
    loop * loop * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * yd[0] * yu[r] * conj(X["36,"][p, q, 0, s]),
    loop * loop * CKM[r, 1] * yd[1] * yu[r] * conj(X["36,"][p, q, 1, s]),
    loop * loop * CKM[r, 2] * yd[2] * yu[r] * conj(X["36,"][p, q, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, 0] * CKM[r, 0] * (yd[0]) ** (2) * conj(X["36,"][p, q, 0, s]),
    loop * loop * CKM[1, 0] * CKM[r, 1] * yd[0] * yd[1] * conj(X["36,"][p, q, 0, s]),
    loop * loop * CKM[2, 0] * CKM[r, 2] * yd[0] * yd[2] * conj(X["36,"][p, q, 0, s]),
    loop * loop * CKM[0, 1] * CKM[r, 0] * yd[0] * yd[1] * conj(X["36,"][p, q, 1, s]),
    loop * loop * CKM[1, 1] * CKM[r, 1] * (yd[1]) ** (2) * conj(X["36,"][p, q, 1, s]),
    loop * loop * CKM[2, 1] * CKM[r, 2] * yd[1] * yd[2] * conj(X["36,"][p, q, 1, s]),
    loop * loop * CKM[0, 2] * CKM[r, 0] * yd[0] * yd[2] * conj(X["36,"][p, q, 2, s]),
    loop * loop * CKM[1, 2] * CKM[r, 1] * yd[1] * yd[2] * conj(X["36,"][p, q, 2, s]),
    loop * loop * CKM[2, 2] * CKM[r, 2] * (yd[2]) ** (2) * conj(X["36,"][p, q, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, 0, q]),
    loop * loop * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 0, 1, q]),
    loop * loop * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 0, 2, q]),
    loop * loop * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 1, 0, q]),
    loop * loop * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, 1, q]),
    loop * loop * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 1, 2, q]),
    loop * loop * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 2, 0, q]),
    loop * loop * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 2, 1, q]),
    loop * loop * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * yu[r] * conj(X["36,"][p, q, s, 0]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * yu[r] * conj(X["36,"][p, q, s, 1]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * yu[r] * conj(X["36,"][p, q, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, q, 0]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 0, q, 1]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 0, q, 2]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 1, q, 0]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, q, 1]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 1, q, 2]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 2, q, 0]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 2, q, 1]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, q, 0, 0]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, q, 0, 1]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, q, 0, 2]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, q, 1, 0]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, q, 1, 1]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, q, 1, 2]),
    (loop) ** (2) * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, q, 2, 0]),
    (loop) ** (2) * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, q, 2, 1]),
    (loop) ** (2) * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["36,"][p, q, r, 0]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["36,"][p, q, r, 0]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["36,"][p, q, r, 0]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["36,"][p, q, r, 1]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["36,"][p, q, r, 1]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["36,"][p, q, r, 1]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["36,"][p, q, r, 2]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["36,"][p, q, r, 2]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["36,"][p, q, r, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * conj(X["36,"][p, r, s, 0]),
    loop * loop * CKM[q, 1] * yd[1] * conj(X["36,"][p, r, s, 1]),
    loop * loop * CKM[q, 2] * yd[2] * conj(X["36,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, r, s, 0]),
    loop * loop * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, r, s, 1]),
    loop * loop * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * yd[0] * yu[r] * conj(X["36,"][p, q, s, 0]),
    loop * loop * CKM[r, 1] * yd[1] * yu[r] * conj(X["36,"][p, q, s, 1]),
    loop * loop * CKM[r, 2] * yd[2] * yu[r] * conj(X["36,"][p, q, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, 0] * CKM[r, 0] * (yd[0]) ** (2) * conj(X["36,"][p, q, s, 0]),
    loop * loop * CKM[1, 0] * CKM[r, 1] * yd[0] * yd[1] * conj(X["36,"][p, q, s, 0]),
    loop * loop * CKM[2, 0] * CKM[r, 2] * yd[0] * yd[2] * conj(X["36,"][p, q, s, 0]),
    loop * loop * CKM[0, 1] * CKM[r, 0] * yd[0] * yd[1] * conj(X["36,"][p, q, s, 1]),
    loop * loop * CKM[1, 1] * CKM[r, 1] * (yd[1]) ** (2) * conj(X["36,"][p, q, s, 1]),
    loop * loop * CKM[2, 1] * CKM[r, 2] * yd[1] * yd[2] * conj(X["36,"][p, q, s, 1]),
    loop * loop * CKM[0, 2] * CKM[r, 0] * yd[0] * yd[2] * conj(X["36,"][p, q, s, 2]),
    loop * loop * CKM[1, 2] * CKM[r, 1] * yd[1] * yd[2] * conj(X["36,"][p, q, s, 2]),
    loop * loop * CKM[2, 2] * CKM[r, 2] * (yd[2]) ** (2) * conj(X["36,"][p, q, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, q, 0]),
    loop * loop * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 0, q, 1]),
    loop * loop * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 0, q, 2]),
    loop * loop * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 1, q, 0]),
    loop * loop * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, q, 1]),
    loop * loop * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 1, q, 2]),
    loop * loop * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 2, q, 0]),
    loop * loop * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 2, q, 1]),
    loop * loop * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * conj(X["36,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~dddD"][p, q, r, s]] += (
    loop * loop * ye[p] * conj(X["36,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * (ye[p]) ** (2) * conj(X["36,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[0, q] * yd[q] * ye[p] * conj(X["36,"][p, 0, r, s]),
    loop * loop * CKM[1, q] * yd[q] * ye[p] * conj(X["36,"][p, 1, r, s]),
    loop * loop * CKM[2, q] * yd[q] * ye[p] * conj(X["36,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * conj(X["36,"][p, 0, r, s]),
    loop * loop * CKM[q, 1] * yd[1] * conj(X["36,"][p, 1, r, s]),
    loop * loop * CKM[q, 2] * yd[2] * conj(X["36,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, 0, r, s]),
    loop * loop * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, 1, r, s]),
    loop * loop * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * yd[0] * yu[r] * conj(X["36,"][p, 0, q, s]),
    loop * loop * CKM[r, 1] * yd[1] * yu[r] * conj(X["36,"][p, 1, q, s]),
    loop * loop * CKM[r, 2] * yd[2] * yu[r] * conj(X["36,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, 0] * CKM[r, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, q, s]),
    loop * loop * CKM[1, 0] * CKM[r, 1] * yd[0] * yd[1] * conj(X["36,"][p, 0, q, s]),
    loop * loop * CKM[2, 0] * CKM[r, 2] * yd[0] * yd[2] * conj(X["36,"][p, 0, q, s]),
    loop * loop * CKM[0, 1] * CKM[r, 0] * yd[0] * yd[1] * conj(X["36,"][p, 1, q, s]),
    loop * loop * CKM[1, 1] * CKM[r, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, q, s]),
    loop * loop * CKM[2, 1] * CKM[r, 2] * yd[1] * yd[2] * conj(X["36,"][p, 1, q, s]),
    loop * loop * CKM[0, 2] * CKM[r, 0] * yd[0] * yd[2] * conj(X["36,"][p, 2, q, s]),
    loop * loop * CKM[1, 2] * CKM[r, 1] * yd[1] * yd[2] * conj(X["36,"][p, 2, q, s]),
    loop * loop * CKM[2, 2] * CKM[r, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, 0, q]),
    loop * loop * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 0, 1, q]),
    loop * loop * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 0, 2, q]),
    loop * loop * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 1, 0, q]),
    loop * loop * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, 1, q]),
    loop * loop * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 1, 2, q]),
    loop * loop * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 2, 0, q]),
    loop * loop * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 2, 1, q]),
    loop * loop * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * conj(X["36,"][p, r, 0, s]),
    loop * loop * CKM[q, 1] * yd[1] * conj(X["36,"][p, r, 1, s]),
    loop * loop * CKM[q, 2] * yd[2] * conj(X["36,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, r, 0, s]),
    loop * loop * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, r, 1, s]),
    loop * loop * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * yd[0] * yu[r] * conj(X["36,"][p, q, 0, s]),
    loop * loop * CKM[r, 1] * yd[1] * yu[r] * conj(X["36,"][p, q, 1, s]),
    loop * loop * CKM[r, 2] * yd[2] * yu[r] * conj(X["36,"][p, q, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, 0] * CKM[r, 0] * (yd[0]) ** (2) * conj(X["36,"][p, q, 0, s]),
    loop * loop * CKM[1, 0] * CKM[r, 1] * yd[0] * yd[1] * conj(X["36,"][p, q, 0, s]),
    loop * loop * CKM[2, 0] * CKM[r, 2] * yd[0] * yd[2] * conj(X["36,"][p, q, 0, s]),
    loop * loop * CKM[0, 1] * CKM[r, 0] * yd[0] * yd[1] * conj(X["36,"][p, q, 1, s]),
    loop * loop * CKM[1, 1] * CKM[r, 1] * (yd[1]) ** (2) * conj(X["36,"][p, q, 1, s]),
    loop * loop * CKM[2, 1] * CKM[r, 2] * yd[1] * yd[2] * conj(X["36,"][p, q, 1, s]),
    loop * loop * CKM[0, 2] * CKM[r, 0] * yd[0] * yd[2] * conj(X["36,"][p, q, 2, s]),
    loop * loop * CKM[1, 2] * CKM[r, 1] * yd[1] * yd[2] * conj(X["36,"][p, q, 2, s]),
    loop * loop * CKM[2, 2] * CKM[r, 2] * (yd[2]) ** (2) * conj(X["36,"][p, q, 2, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, 0, q]),
    loop * loop * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 0, 1, q]),
    loop * loop * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 0, 2, q]),
    loop * loop * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 1, 0, q]),
    loop * loop * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, 1, q]),
    loop * loop * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 1, 2, q]),
    loop * loop * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 2, 0, q]),
    loop * loop * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 2, 1, q]),
    loop * loop * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * conj(X["36,"][p, r, s, 0]),
    loop * loop * CKM[q, 1] * yd[1] * conj(X["36,"][p, r, s, 1]),
    loop * loop * CKM[q, 2] * yd[2] * conj(X["36,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[q, 0] * yd[0] * ye[p] * conj(X["36,"][p, r, s, 0]),
    loop * loop * CKM[q, 1] * yd[1] * ye[p] * conj(X["36,"][p, r, s, 1]),
    loop * loop * CKM[q, 2] * yd[2] * ye[p] * conj(X["36,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * yd[0] * yu[r] * conj(X["36,"][p, q, s, 0]),
    loop * loop * CKM[r, 1] * yd[1] * yu[r] * conj(X["36,"][p, q, s, 1]),
    loop * loop * CKM[r, 2] * yd[2] * yu[r] * conj(X["36,"][p, q, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, 0] * CKM[r, 0] * (yd[0]) ** (2) * conj(X["36,"][p, q, s, 0]),
    loop * loop * CKM[1, 0] * CKM[r, 1] * yd[0] * yd[1] * conj(X["36,"][p, q, s, 0]),
    loop * loop * CKM[2, 0] * CKM[r, 2] * yd[0] * yd[2] * conj(X["36,"][p, q, s, 0]),
    loop * loop * CKM[0, 1] * CKM[r, 0] * yd[0] * yd[1] * conj(X["36,"][p, q, s, 1]),
    loop * loop * CKM[1, 1] * CKM[r, 1] * (yd[1]) ** (2) * conj(X["36,"][p, q, s, 1]),
    loop * loop * CKM[2, 1] * CKM[r, 2] * yd[1] * yd[2] * conj(X["36,"][p, q, s, 1]),
    loop * loop * CKM[0, 2] * CKM[r, 0] * yd[0] * yd[2] * conj(X["36,"][p, q, s, 2]),
    loop * loop * CKM[1, 2] * CKM[r, 1] * yd[1] * yd[2] * conj(X["36,"][p, q, s, 2]),
    loop * loop * CKM[2, 2] * CKM[r, 2] * (yd[2]) ** (2) * conj(X["36,"][p, q, s, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["36,"][p, 0, q, 0]),
    loop * loop * CKM[r, 1] * CKM[s, 0] * yd[0] * yd[1] * conj(X["36,"][p, 0, q, 1]),
    loop * loop * CKM[r, 2] * CKM[s, 0] * yd[0] * yd[2] * conj(X["36,"][p, 0, q, 2]),
    loop * loop * CKM[r, 0] * CKM[s, 1] * yd[0] * yd[1] * conj(X["36,"][p, 1, q, 0]),
    loop * loop * CKM[r, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["36,"][p, 1, q, 1]),
    loop * loop * CKM[r, 2] * CKM[s, 1] * yd[1] * yd[2] * conj(X["36,"][p, 1, q, 2]),
    loop * loop * CKM[r, 0] * CKM[s, 2] * yd[0] * yd[2] * conj(X["36,"][p, 2, q, 0]),
    loop * loop * CKM[r, 1] * CKM[s, 2] * yd[1] * yd[2] * conj(X["36,"][p, 2, q, 1]),
    loop * loop * CKM[r, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["36,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~dddD"][p, q, r, s]] += (
    loop * loop * ye[p] * conj(X["36,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * (ye[p]) ** (2) * conj(X["36,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["36,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[0, q] * yd[q] * ye[p] * conj(X["36,"][p, 0, r, s]),
    loop * loop * CKM[1, q] * yd[q] * ye[p] * conj(X["36,"][p, 1, r, s]),
    loop * loop * CKM[2, q] * yd[q] * ye[p] * conj(X["36,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["37,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * yu[s] * conj(X["37,"][p, 0, r, s]),
    (loop) ** (2) * CKM[1, q] * yd[q] * yu[s] * conj(X["37,"][p, 1, r, s]),
    (loop) ** (2) * CKM[2, q] * yd[q] * yu[s] * conj(X["37,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["37,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * yu[s] * conj(X["37,"][p, r, 0, s]),
    (loop) ** (2) * CKM[1, q] * yd[q] * yu[s] * conj(X["37,"][p, r, 1, s]),
    (loop) ** (2) * CKM[2, q] * yd[q] * yu[s] * conj(X["37,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["37,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * yu[0] * conj(X["37,"][p, r, s, 0]),
    (loop) ** (2) * CKM[1, q] * yd[q] * yu[1] * conj(X["37,"][p, r, s, 1]),
    (loop) ** (2) * CKM[2, q] * yd[q] * yu[2] * conj(X["37,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["37,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * yu[s] * conj(X["37,"][p, 0, r, s]),
    (loop) ** (2) * CKM[1, q] * yd[q] * yu[s] * conj(X["37,"][p, 1, r, s]),
    (loop) ** (2) * CKM[2, q] * yd[q] * yu[s] * conj(X["37,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["37,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * CKM[0, s] * yd[q] * yd[s] * conj(X["37,"][p, 0, 0, r]),
    (loop) ** (2) * CKM[0, q] * CKM[1, s] * yd[q] * yd[s] * conj(X["37,"][p, 0, 1, r]),
    (loop) ** (2) * CKM[0, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["37,"][p, 0, 2, r]),
    (loop) ** (2) * CKM[0, s] * CKM[1, q] * yd[q] * yd[s] * conj(X["37,"][p, 1, 0, r]),
    (loop) ** (2) * CKM[1, q] * CKM[1, s] * yd[q] * yd[s] * conj(X["37,"][p, 1, 1, r]),
    (loop) ** (2) * CKM[1, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["37,"][p, 1, 2, r]),
    (loop) ** (2) * CKM[0, s] * CKM[2, q] * yd[q] * yd[s] * conj(X["37,"][p, 2, 0, r]),
    (loop) ** (2) * CKM[1, s] * CKM[2, q] * yd[q] * yd[s] * conj(X["37,"][p, 2, 1, r]),
    (loop) ** (2) * CKM[2, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["37,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["37,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * yu[s] * conj(X["37,"][p, r, 0, s]),
    (loop) ** (2) * CKM[1, q] * yd[q] * yu[s] * conj(X["37,"][p, r, 1, s]),
    (loop) ** (2) * CKM[2, q] * yd[q] * yu[s] * conj(X["37,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["37,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * CKM[0, s] * yd[q] * yd[s] * conj(X["37,"][p, 0, 0, r]),
    (loop) ** (2) * CKM[0, s] * CKM[1, q] * yd[q] * yd[s] * conj(X["37,"][p, 0, 1, r]),
    (loop) ** (2) * CKM[0, s] * CKM[2, q] * yd[q] * yd[s] * conj(X["37,"][p, 0, 2, r]),
    (loop) ** (2) * CKM[0, q] * CKM[1, s] * yd[q] * yd[s] * conj(X["37,"][p, 1, 0, r]),
    (loop) ** (2) * CKM[1, q] * CKM[1, s] * yd[q] * yd[s] * conj(X["37,"][p, 1, 1, r]),
    (loop) ** (2) * CKM[1, s] * CKM[2, q] * yd[q] * yd[s] * conj(X["37,"][p, 1, 2, r]),
    (loop) ** (2) * CKM[0, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["37,"][p, 2, 0, r]),
    (loop) ** (2) * CKM[1, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["37,"][p, 2, 1, r]),
    (loop) ** (2) * CKM[2, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["37,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["38,"][p, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["38,"][p, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["38,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["38,"][p, r, 0, s]),
    loop * CKM[1, q] * yd[q] * conj(X["38,"][p, r, 1, s]),
    loop * CKM[2, q] * yd[q] * conj(X["38,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["38,"][p, r, s, 0]),
    loop * CKM[1, q] * yd[q] * conj(X["38,"][p, r, s, 1]),
    loop * CKM[2, q] * yd[q] * conj(X["38,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["38,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["38,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["38,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 2, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 2, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["38,"][p, 0, q, 0]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, 0, q, 1]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 0, q, 2]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["38,"][p, 1, q, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, 1, q, 1]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 1, q, 2]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, 2, q, 0]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, 2, q, 1]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["38,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["38,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["38,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 2, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 2, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 0, 0]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 0, 1]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 0, 2]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["38,"][p, q, 1, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 1, 1]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 1, 2]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, q, 2, 0]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, q, 2, 1]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 0, 0]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 0, 1]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 0, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 1, 0]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 1, 1]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 1, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 2, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 2, 1]),
    (loop) ** (2)
    * CKM[2, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["38,"][p, 0, q, 0]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["38,"][p, 0, q, 1]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, 0, q, 2]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, 1, q, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, 1, q, 1]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, 1, q, 2]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 2, q, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 2, q, 1]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 0, 0]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["38,"][p, q, 0, 1]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, q, 0, 2]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 1, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 1, 1]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["38,"][p, q, 1, 2]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 2, 0]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 2, 1]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["38,"][p, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, r]
    * CKM[0, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 0, 2]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 1, 0]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[1, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 1, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, r]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 1, 2]),
    (loop) ** (2)
    * CKM[0, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 2, 0]),
    (loop) ** (2)
    * CKM[1, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 2, 1]),
    (loop) ** (2)
    * CKM[2, r]
    * CKM[2, s]
    * yd[r]
    * yd[s]
    * ye[p]
    * conj(X["38,"][p, q, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * yu[r]
    * conj(X["38,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["38,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["38,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["38,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, 0] * yd[0] * conj(X["39,"][p, 0, q, 0, r, s]),
    loop * CKM[0, 1] * yd[1] * conj(X["39,"][p, 0, q, 1, r, s]),
    loop * CKM[0, 2] * yd[2] * conj(X["39,"][p, 0, q, 2, r, s]),
    loop * CKM[1, 0] * yd[0] * conj(X["39,"][p, 1, q, 0, r, s]),
    loop * CKM[1, 1] * yd[1] * conj(X["39,"][p, 1, q, 1, r, s]),
    loop * CKM[1, 2] * yd[2] * conj(X["39,"][p, 1, q, 2, r, s]),
    loop * CKM[2, 0] * yd[0] * conj(X["39,"][p, 2, q, 0, r, s]),
    loop * CKM[2, 1] * yd[1] * conj(X["39,"][p, 2, q, 1, r, s]),
    loop * CKM[2, 2] * yd[2] * conj(X["39,"][p, 2, q, 2, r, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, 0] * yd[0] * conj(X["39,"][p, 0, q, r, 0, s]),
    loop * CKM[0, 1] * yd[1] * conj(X["39,"][p, 0, q, r, 1, s]),
    loop * CKM[0, 2] * yd[2] * conj(X["39,"][p, 0, q, r, 2, s]),
    loop * CKM[1, 0] * yd[0] * conj(X["39,"][p, 1, q, r, 0, s]),
    loop * CKM[1, 1] * yd[1] * conj(X["39,"][p, 1, q, r, 1, s]),
    loop * CKM[1, 2] * yd[2] * conj(X["39,"][p, 1, q, r, 2, s]),
    loop * CKM[2, 0] * yd[0] * conj(X["39,"][p, 2, q, r, 0, s]),
    loop * CKM[2, 1] * yd[1] * conj(X["39,"][p, 2, q, r, 1, s]),
    loop * CKM[2, 2] * yd[2] * conj(X["39,"][p, 2, q, r, 2, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, 0] * yd[0] * conj(X["39,"][p, 0, q, r, s, 0]),
    loop * CKM[0, 1] * yd[1] * conj(X["39,"][p, 0, q, r, s, 1]),
    loop * CKM[0, 2] * yd[2] * conj(X["39,"][p, 0, q, r, s, 2]),
    loop * CKM[1, 0] * yd[0] * conj(X["39,"][p, 1, q, r, s, 0]),
    loop * CKM[1, 1] * yd[1] * conj(X["39,"][p, 1, q, r, s, 1]),
    loop * CKM[1, 2] * yd[2] * conj(X["39,"][p, 1, q, r, s, 2]),
    loop * CKM[2, 0] * yd[0] * conj(X["39,"][p, 2, q, r, s, 0]),
    loop * CKM[2, 1] * yd[1] * conj(X["39,"][p, 2, q, r, s, 1]),
    loop * CKM[2, 2] * yd[2] * conj(X["39,"][p, 2, q, r, s, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, q, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, q, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, q, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, q, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, q, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, q, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, q, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, q, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, q, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, q, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, q, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, q, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, q, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, q, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 0, 1, q, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 0, 2, q, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 1, 0, q, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 1, 2, q, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 2, 0, q, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 2, 1, q, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 2, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 0, 1, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 0, 2, q, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 1, 0, q, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 1, 2, q, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 2, 0, q, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 2, 1, q, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 2, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 0, 0, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 0, 1, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 0, 2, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 1, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 1, 1, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 1, 2, q, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 2, 0, q, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 2, 1, q, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 2, 2, q, r]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[0, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[0, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[0, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, 1, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, 1, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, 1, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, 1, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * yd[0] * ye[p] * conj(X["39,"][p, 0, q, 0, r, s]),
    (loop) ** (2) * CKM[0, 1] * yd[1] * ye[p] * conj(X["39,"][p, 0, q, 1, r, s]),
    (loop) ** (2) * CKM[0, 2] * yd[2] * ye[p] * conj(X["39,"][p, 0, q, 2, r, s]),
    (loop) ** (2) * CKM[1, 0] * yd[0] * ye[p] * conj(X["39,"][p, 1, q, 0, r, s]),
    (loop) ** (2) * CKM[1, 1] * yd[1] * ye[p] * conj(X["39,"][p, 1, q, 1, r, s]),
    (loop) ** (2) * CKM[1, 2] * yd[2] * ye[p] * conj(X["39,"][p, 1, q, 2, r, s]),
    (loop) ** (2) * CKM[2, 0] * yd[0] * ye[p] * conj(X["39,"][p, 2, q, 0, r, s]),
    (loop) ** (2) * CKM[2, 1] * yd[1] * ye[p] * conj(X["39,"][p, 2, q, 1, r, s]),
    (loop) ** (2) * CKM[2, 2] * yd[2] * ye[p] * conj(X["39,"][p, 2, q, 2, r, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 0, q, 0, r, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 0, q, 1, r, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 0, q, 2, r, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 1, q, 0, r, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 1, q, 1, r, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 1, q, 2, r, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 2, q, 0, r, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 2, q, 1, r, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 2, q, 2, r, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 0, r, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 0, r, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 0, r, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 1, r, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 1, r, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 1, r, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 2, r, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 2, r, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 2, r, 2, q, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, r, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 0, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 0, 0, q, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 0, 0, q, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 0, 1, q, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 0, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 0, 1, q, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 0, 2, q, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 0, 2, q, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 0, 2, q, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 1, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 1, 0, q, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 1, 0, q, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 1, 1, q, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 1, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 1, 1, q, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 1, 2, q, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 1, 2, q, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 1, 2, q, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 2, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 2, 0, q, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 2, 0, q, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 2, 1, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 2, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 2, 1, q, 2, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 2, 2, q, 0, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 2, 2, q, 1, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 2, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, 2, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, 0, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, 1, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[0, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[0, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[0, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * yd[0] * ye[p] * conj(X["39,"][p, 0, q, r, 0, s]),
    (loop) ** (2) * CKM[0, 1] * yd[1] * ye[p] * conj(X["39,"][p, 0, q, r, 1, s]),
    (loop) ** (2) * CKM[0, 2] * yd[2] * ye[p] * conj(X["39,"][p, 0, q, r, 2, s]),
    (loop) ** (2) * CKM[1, 0] * yd[0] * ye[p] * conj(X["39,"][p, 1, q, r, 0, s]),
    (loop) ** (2) * CKM[1, 1] * yd[1] * ye[p] * conj(X["39,"][p, 1, q, r, 1, s]),
    (loop) ** (2) * CKM[1, 2] * yd[2] * ye[p] * conj(X["39,"][p, 1, q, r, 2, s]),
    (loop) ** (2) * CKM[2, 0] * yd[0] * ye[p] * conj(X["39,"][p, 2, q, r, 0, s]),
    (loop) ** (2) * CKM[2, 1] * yd[1] * ye[p] * conj(X["39,"][p, 2, q, r, 1, s]),
    (loop) ** (2) * CKM[2, 2] * yd[2] * ye[p] * conj(X["39,"][p, 2, q, r, 2, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 0, q, r, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 0, q, r, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 0, q, r, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 1, q, r, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 1, q, r, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 1, q, r, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 2, q, r, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 2, q, r, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 2, q, r, 2, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 0, r, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 0, r, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 0, r, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 1, r, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 1, r, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 1, r, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 2, r, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 2, r, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 2, r, q, 2, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, 2, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, r, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 0, 0, q, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 0, 0, q, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 0, 0, q, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 0, 1, q, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 0, 1, q, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 0, 1, q, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 0, 2, q, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 0, 2, q, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 0, 2, q, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 1, 0, q, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 1, 0, q, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 1, 0, q, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 1, 1, q, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 1, 1, q, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 1, 1, q, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 1, 2, q, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 1, 2, q, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 1, 2, q, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 2, 0, q, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 2, 0, q, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 2, 0, q, r, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 2, 1, q, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 2, 1, q, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 2, 1, q, r, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["39,"][p, 2, 2, q, r, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["39,"][p, 2, 2, q, r, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["39,"][p, 2, 2, q, r, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, r, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, r, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, r, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, r, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, r, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[0, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[0, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[0, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 0, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 1, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 0, 2, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 0, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 1, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 1, 2, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 0, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 1, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["39,"][p, 2, 2, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * yd[0] * ye[p] * conj(X["39,"][p, 0, q, r, s, 0]),
    (loop) ** (2) * CKM[0, 1] * yd[1] * ye[p] * conj(X["39,"][p, 0, q, r, s, 1]),
    (loop) ** (2) * CKM[0, 2] * yd[2] * ye[p] * conj(X["39,"][p, 0, q, r, s, 2]),
    (loop) ** (2) * CKM[1, 0] * yd[0] * ye[p] * conj(X["39,"][p, 1, q, r, s, 0]),
    (loop) ** (2) * CKM[1, 1] * yd[1] * ye[p] * conj(X["39,"][p, 1, q, r, s, 1]),
    (loop) ** (2) * CKM[1, 2] * yd[2] * ye[p] * conj(X["39,"][p, 1, q, r, s, 2]),
    (loop) ** (2) * CKM[2, 0] * yd[0] * ye[p] * conj(X["39,"][p, 2, q, r, s, 0]),
    (loop) ** (2) * CKM[2, 1] * yd[1] * ye[p] * conj(X["39,"][p, 2, q, r, s, 1]),
    (loop) ** (2) * CKM[2, 2] * yd[2] * ye[p] * conj(X["39,"][p, 2, q, r, s, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 0, q, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 0, q, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 0, q, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 1, q, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 1, q, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 1, q, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 2, q, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 2, q, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * (ye[p]) ** (2)
    * conj(X["39,"][p, 2, q, r, s, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 0, r, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 0, r, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 0, r, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 1, r, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 1, r, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 1, r, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 2, r, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 2, r, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * ye[p]
    * yu[r]
    * conj(X["39,"][p, 2, r, q, s, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, r, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, r, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 0, r, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, r, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 0, r, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 0, r, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, r, 0, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, r, 0, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 1, r, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, r, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 1, r, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 1, r, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, r, 0, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, r, 0, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 0, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["39,"][p, 2, r, 1, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, r, 1, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["39,"][p, 2, r, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["39,"][p, 2, r, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~dddD"][p, q, r, s]] += (
    loop * conj(X["39,"][p, 0, 0, q, r, s]),
    loop * conj(X["39,"][p, 1, 1, q, r, s]),
    loop * conj(X["39,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["39,"][p, 0, 0, q, r, s]),
    loop * ye[p] * conj(X["39,"][p, 1, 1, q, r, s]),
    loop * ye[p] * conj(X["39,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["39,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["39,"][p, 0, 0, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["39,"][p, 0, 0, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["39,"][p, 0, 0, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["39,"][p, 1, 1, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["39,"][p, 1, 1, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["39,"][p, 1, 1, 2, r, s]),
    loop * CKM[0, q] * yd[q] * conj(X["39,"][p, 2, 2, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["39,"][p, 2, 2, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["39,"][p, 2, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * yu[0] * conj(X["40,"][p, 0, r, s, 0, q]),
    loop * yu[1] * conj(X["40,"][p, 1, r, s, 1, q]),
    loop * yu[2] * conj(X["40,"][p, 2, r, s, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * yu[0] * conj(X["40,"][p, r, 0, s, 0, q]),
    loop * yu[1] * conj(X["40,"][p, r, 1, s, 1, q]),
    loop * yu[2] * conj(X["40,"][p, r, 2, s, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * yu[0] * conj(X["40,"][p, r, s, 0, 0, q]),
    loop * yu[1] * conj(X["40,"][p, r, s, 1, 1, q]),
    loop * yu[2] * conj(X["40,"][p, r, s, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["40,"][p, 0, 0, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[0] * conj(X["40,"][p, 0, 1, q, 0, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[0] * conj(X["40,"][p, 0, 2, q, 0, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[1] * conj(X["40,"][p, 1, 0, q, 1, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["40,"][p, 1, 1, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[1] * conj(X["40,"][p, 1, 2, q, 1, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[2] * conj(X["40,"][p, 2, 0, q, 2, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[2] * conj(X["40,"][p, 2, 1, q, 2, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["40,"][p, 2, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 0, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 0, 1, q, 0, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 0, 2, q, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 1, 0, q, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 1, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 1, 2, q, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 2, 0, q, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 2, 1, q, 2, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 2, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 0, 0, r, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 0, 1, r, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 0, 2, r, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 1, 0, r, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 1, 1, r, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 1, 2, r, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 2, 0, r, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 2, 1, r, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 2, 2, r, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 0, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 0, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 0, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 1, r, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 1, r, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 1, r, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 2, r, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 2, r, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 2, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 0, r, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 0, r, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 0, r, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 1, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 1, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 1, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 2, r, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 2, r, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 2, r, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 0, r, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 0, r, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 0, r, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 1, r, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 1, r, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 1, r, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 2, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 2, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 2, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["40,"][p, 0, q, 0, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[0] * conj(X["40,"][p, 0, q, 1, 0, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[0] * conj(X["40,"][p, 0, q, 2, 0, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[1] * conj(X["40,"][p, 1, q, 0, 1, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["40,"][p, 1, q, 1, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[1] * conj(X["40,"][p, 1, q, 2, 1, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[2] * conj(X["40,"][p, 2, q, 0, 2, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[2] * conj(X["40,"][p, 2, q, 1, 2, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["40,"][p, 2, q, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 0, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 0, q, 1, 0, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 0, q, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 1, q, 0, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 1, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 1, q, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 2, q, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 2, q, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 2, q, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 0, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 0, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 0, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 1, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 1, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 1, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 2, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 2, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 2, r, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 1, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 0, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["40,"][p, 0, 0, q, 0, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[1] * conj(X["40,"][p, 0, 1, q, 1, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[2] * conj(X["40,"][p, 0, 2, q, 2, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[0] * conj(X["40,"][p, 1, 0, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["40,"][p, 1, 1, q, 1, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[2] * conj(X["40,"][p, 1, 2, q, 2, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[0] * conj(X["40,"][p, 2, 0, q, 0, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[1] * conj(X["40,"][p, 2, 1, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["40,"][p, 2, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 0, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 0, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 0, 2, q, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 1, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 1, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 1, 2, q, 2, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 2, 0, q, 0, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 2, 1, q, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 2, 2, q, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 0, 0, r, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 0, 1, r, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 0, 2, r, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 1, 0, r, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 1, 1, r, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 1, 2, r, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 2, 0, r, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 2, 1, r, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 2, 2, r, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 0, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 0, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, 0, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 0, 1, r, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 0, 1, r, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 0, 1, r, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 0, 2, r, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 0, 2, r, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 0, 2, r, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 1, 0, r, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 1, 0, r, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 1, 0, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 1, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 1, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, 1, r, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 1, 2, r, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 1, 2, r, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 1, 2, r, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 2, 0, r, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 2, 0, r, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 2, 0, r, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 2, 1, r, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 2, 1, r, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 2, 1, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 2, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 2, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, 2, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["40,"][p, q, 0, 0, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[0] * conj(X["40,"][p, q, 0, 1, 0, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[0] * conj(X["40,"][p, q, 0, 2, 0, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[1] * conj(X["40,"][p, q, 1, 0, 1, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["40,"][p, q, 1, 1, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[1] * conj(X["40,"][p, q, 1, 2, 1, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[2] * conj(X["40,"][p, q, 2, 0, 2, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[2] * conj(X["40,"][p, q, 2, 1, 2, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["40,"][p, q, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, q, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, q, 0, 1, 0, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, q, 0, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, q, 1, 0, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, q, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, q, 1, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, q, 2, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, q, 2, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, q, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, r, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, r, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, r, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, r, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, r, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, r, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, r, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, r, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, r, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 0, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 1, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 0, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 1, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["40,"][p, 0, q, 0, 0, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[1] * conj(X["40,"][p, 0, q, 1, 1, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[2] * conj(X["40,"][p, 0, q, 2, 2, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[0] * conj(X["40,"][p, 1, q, 0, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["40,"][p, 1, q, 1, 1, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[2] * conj(X["40,"][p, 1, q, 2, 2, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[0] * conj(X["40,"][p, 2, q, 0, 0, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[1] * conj(X["40,"][p, 2, q, 1, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["40,"][p, 2, q, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 0, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 0, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 0, q, 2, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 1, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 1, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 1, q, 2, 2, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, 2, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, 2, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, 2, q, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 0, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 0, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 0, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 1, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 1, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 1, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, 2, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, 2, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, 2, r, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 0, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 0, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 0, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 0, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 0, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 0, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 0, r, 2, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 1, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 1, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 1, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 1, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 1, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 1, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 1, r, 2, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 2, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 2, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, 2, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 2, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 2, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, 2, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, 2, r, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["40,"][p, q, 0, 0, 0, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[1] * conj(X["40,"][p, q, 0, 1, 1, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[2] * conj(X["40,"][p, q, 0, 2, 2, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[0] * conj(X["40,"][p, q, 1, 0, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["40,"][p, q, 1, 1, 1, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[2] * conj(X["40,"][p, q, 1, 2, 2, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[0] * conj(X["40,"][p, q, 2, 0, 0, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[1] * conj(X["40,"][p, q, 2, 1, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["40,"][p, q, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, q, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, q, 0, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, q, 0, 2, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, q, 1, 0, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, q, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, q, 1, 2, 2, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[0]
    * conj(X["40,"][p, q, 2, 0, 0, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[1]
    * conj(X["40,"][p, q, 2, 1, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[p]
    * yu[2]
    * conj(X["40,"][p, q, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, r, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, r, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, r, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, r, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, r, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, r, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[0]
    * yu[r]
    * conj(X["40,"][p, r, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[1]
    * yu[r]
    * conj(X["40,"][p, r, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * yu[2]
    * yu[r]
    * conj(X["40,"][p, r, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 0, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 0, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 0, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 1, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 1, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 1, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["40,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["40,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["40,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["40,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 0, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 0, 1, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 0, 1, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 0, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 0, 2, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 0, 2, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 0, 2, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 1, 0, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 1, 0, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 1, 0, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 1, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 1, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 1, 2, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 1, 2, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 2, 0, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 2, 0, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["40,"][p, r, 2, 0, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 2, 1, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 2, 1, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["40,"][p, r, 2, 1, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["40,"][p, r, 2, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dddH"][p, q, r, s]] += (
    loop * yu[0] * conj(X["41,"][p, 0, 0, q, r, s]),
    loop * yu[1] * conj(X["41,"][p, 1, 1, q, r, s]),
    loop * yu[2] * conj(X["41,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dudH~"][p, q, r, s]] += (
    loop * CKM[0, 0] * yd[0] * conj(X["41,"][p, 0, r, 0, q, s]),
    loop * CKM[0, 1] * yd[1] * conj(X["41,"][p, 0, r, 1, q, s]),
    loop * CKM[0, 2] * yd[2] * conj(X["41,"][p, 0, r, 2, q, s]),
    loop * CKM[1, 0] * yd[0] * conj(X["41,"][p, 1, r, 0, q, s]),
    loop * CKM[1, 1] * yd[1] * conj(X["41,"][p, 1, r, 1, q, s]),
    loop * CKM[1, 2] * yd[2] * conj(X["41,"][p, 1, r, 2, q, s]),
    loop * CKM[2, 0] * yd[0] * conj(X["41,"][p, 2, r, 0, q, s]),
    loop * CKM[2, 1] * yd[1] * conj(X["41,"][p, 2, r, 1, q, s]),
    loop * CKM[2, 2] * yd[2] * conj(X["41,"][p, 2, r, 2, q, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dudH~"][p, q, r, s]] += (
    loop * CKM[0, 0] * yd[0] * conj(X["41,"][p, 0, r, q, 0, s]),
    loop * CKM[0, 1] * yd[1] * conj(X["41,"][p, 0, r, q, 1, s]),
    loop * CKM[0, 2] * yd[2] * conj(X["41,"][p, 0, r, q, 2, s]),
    loop * CKM[1, 0] * yd[0] * conj(X["41,"][p, 1, r, q, 0, s]),
    loop * CKM[1, 1] * yd[1] * conj(X["41,"][p, 1, r, q, 1, s]),
    loop * CKM[1, 2] * yd[2] * conj(X["41,"][p, 1, r, q, 2, s]),
    loop * CKM[2, 0] * yd[0] * conj(X["41,"][p, 2, r, q, 0, s]),
    loop * CKM[2, 1] * yd[1] * conj(X["41,"][p, 2, r, q, 1, s]),
    loop * CKM[2, 2] * yd[2] * conj(X["41,"][p, 2, r, q, 2, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dudH~"][p, q, r, s]] += (
    loop * CKM[0, 0] * yd[0] * conj(X["41,"][p, 0, r, q, s, 0]),
    loop * CKM[0, 1] * yd[1] * conj(X["41,"][p, 0, r, q, s, 1]),
    loop * CKM[0, 2] * yd[2] * conj(X["41,"][p, 0, r, q, s, 2]),
    loop * CKM[1, 0] * yd[0] * conj(X["41,"][p, 1, r, q, s, 0]),
    loop * CKM[1, 1] * yd[1] * conj(X["41,"][p, 1, r, q, s, 1]),
    loop * CKM[1, 2] * yd[2] * conj(X["41,"][p, 1, r, q, s, 2]),
    loop * CKM[2, 0] * yd[0] * conj(X["41,"][p, 2, r, q, s, 0]),
    loop * CKM[2, 1] * yd[1] * conj(X["41,"][p, 2, r, q, s, 1]),
    loop * CKM[2, 2] * yd[2] * conj(X["41,"][p, 2, r, q, s, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * yu[0] * conj(X["41,"][p, 0, 0, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * yu[0] * conj(X["41,"][p, 0, 0, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * yu[0] * conj(X["41,"][p, 0, 0, 2, r, s]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * yu[1] * conj(X["41,"][p, 1, 1, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * yu[1] * conj(X["41,"][p, 1, 1, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * yu[1] * conj(X["41,"][p, 1, 1, 2, r, s]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * yu[2] * conj(X["41,"][p, 2, 2, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * yu[2] * conj(X["41,"][p, 2, 2, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * yu[2] * conj(X["41,"][p, 2, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, r, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, r, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, r, s]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, r, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, r, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, r, s]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, r, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, r, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[0]
    * yu[r]
    * conj(X["41,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[0]
    * yu[r]
    * conj(X["41,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[0]
    * yu[r]
    * conj(X["41,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[1]
    * yu[r]
    * conj(X["41,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[1]
    * yu[r]
    * conj(X["41,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[1]
    * yu[r]
    * conj(X["41,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[2]
    * yu[r]
    * conj(X["41,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[2]
    * yu[r]
    * conj(X["41,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[2]
    * yu[r]
    * conj(X["41,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * yu[0] * conj(X["41,"][p, 0, 0, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * yu[0] * conj(X["41,"][p, 0, 0, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * yu[0] * conj(X["41,"][p, 0, 0, r, 2, s]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * yu[1] * conj(X["41,"][p, 1, 1, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * yu[1] * conj(X["41,"][p, 1, 1, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * yu[1] * conj(X["41,"][p, 1, 1, r, 2, s]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * yu[2] * conj(X["41,"][p, 2, 2, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * yu[2] * conj(X["41,"][p, 2, 2, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * yu[2] * conj(X["41,"][p, 2, 2, r, 2, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, r, 0, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, r, 1, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, r, 2, s]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, r, 0, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, r, 1, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, r, 2, s]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, r, 0, s]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, r, 1, s]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, r, 2, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[0]
    * yu[r]
    * conj(X["41,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[0]
    * yu[r]
    * conj(X["41,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[0]
    * yu[r]
    * conj(X["41,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[1]
    * yu[r]
    * conj(X["41,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[1]
    * yu[r]
    * conj(X["41,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[1]
    * yu[r]
    * conj(X["41,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[2]
    * yu[r]
    * conj(X["41,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[2]
    * yu[r]
    * conj(X["41,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[2]
    * yu[r]
    * conj(X["41,"][p, 2, 2, q, 2, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 2, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * yu[0] * conj(X["41,"][p, 0, 0, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * yu[0] * conj(X["41,"][p, 0, 0, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * yu[0] * conj(X["41,"][p, 0, 0, r, s, 2]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * yu[1] * conj(X["41,"][p, 1, 1, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * yu[1] * conj(X["41,"][p, 1, 1, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * yu[1] * conj(X["41,"][p, 1, 1, r, s, 2]),
    (loop) ** (2) * CKM[q, 0] * yd[0] * yu[2] * conj(X["41,"][p, 2, 2, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * yu[2] * conj(X["41,"][p, 2, 2, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * yu[2] * conj(X["41,"][p, 2, 2, r, s, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, r, s, 0]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, r, s, 1]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, r, s, 2]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, r, s, 0]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, r, s, 1]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, r, s, 2]),
    (loop) ** (2)
    * CKM[q, 0]
    * yd[0]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, r, s, 0]),
    (loop) ** (2)
    * CKM[q, 1]
    * yd[1]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, r, s, 1]),
    (loop) ** (2)
    * CKM[q, 2]
    * yd[2]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, r, s, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[0]
    * yu[r]
    * conj(X["41,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[0]
    * yu[r]
    * conj(X["41,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[0]
    * yu[r]
    * conj(X["41,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[1]
    * yu[r]
    * conj(X["41,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[1]
    * yu[r]
    * conj(X["41,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[1]
    * yu[r]
    * conj(X["41,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[2]
    * yu[r]
    * conj(X["41,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[2]
    * yu[r]
    * conj(X["41,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[2]
    * yu[r]
    * conj(X["41,"][p, 2, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[0] * conj(X["41,"][p, 0, 0, q, r, s]),
    (loop) ** (2) * ye[p] * yu[1] * conj(X["41,"][p, 1, 1, q, r, s]),
    (loop) ** (2) * ye[p] * yu[2] * conj(X["41,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * yu[0] * conj(X["41,"][p, 0, 0, q, r, s]),
    (loop) ** (2) * (ye[p]) ** (2) * yu[1] * conj(X["41,"][p, 1, 1, q, r, s]),
    (loop) ** (2) * (ye[p]) ** (2) * yu[2] * conj(X["41,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * yd[q]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, r, s]),
    (loop) ** (2)
    * CKM[1, q]
    * yd[q]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, r, s]),
    (loop) ** (2)
    * CKM[2, q]
    * yd[q]
    * ye[p]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, r, s]),
    (loop) ** (2)
    * CKM[0, q]
    * yd[q]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, r, s]),
    (loop) ** (2)
    * CKM[1, q]
    * yd[q]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, r, s]),
    (loop) ** (2)
    * CKM[2, q]
    * yd[q]
    * ye[p]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, r, s]),
    (loop) ** (2)
    * CKM[0, q]
    * yd[q]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, r, s]),
    (loop) ** (2)
    * CKM[1, q]
    * yd[q]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, r, s]),
    (loop) ** (2)
    * CKM[2, q]
    * yd[q]
    * ye[p]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * yd[0] * yu[q] * conj(X["41,"][p, 0, q, 0, r, s]),
    (loop) ** (2) * CKM[0, 1] * yd[1] * yu[q] * conj(X["41,"][p, 0, q, 1, r, s]),
    (loop) ** (2) * CKM[0, 2] * yd[2] * yu[q] * conj(X["41,"][p, 0, q, 2, r, s]),
    (loop) ** (2) * CKM[1, 0] * yd[0] * yu[q] * conj(X["41,"][p, 1, q, 0, r, s]),
    (loop) ** (2) * CKM[1, 1] * yd[1] * yu[q] * conj(X["41,"][p, 1, q, 1, r, s]),
    (loop) ** (2) * CKM[1, 2] * yd[2] * yu[q] * conj(X["41,"][p, 1, q, 2, r, s]),
    (loop) ** (2) * CKM[2, 0] * yd[0] * yu[q] * conj(X["41,"][p, 2, q, 0, r, s]),
    (loop) ** (2) * CKM[2, 1] * yd[1] * yu[q] * conj(X["41,"][p, 2, q, 1, r, s]),
    (loop) ** (2) * CKM[2, 2] * yd[2] * yu[q] * conj(X["41,"][p, 2, q, 2, r, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 0, q, 0, r, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 0, q, 1, r, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 0, q, 2, r, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 1, q, 0, r, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 1, q, 1, r, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 1, q, 2, r, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 2, q, 0, r, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 2, q, 1, r, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 2, q, 2, r, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 0, r, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 0, r, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 0, r, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 1, r, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 1, r, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 1, r, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 2, r, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 2, r, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 2, r, 2, q, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 0, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 0, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 0, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 0, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 0, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 0, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 1, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 1, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 1, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 1, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 1, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 1, 2, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 2, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 2, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 2, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 2, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 2, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 2, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 0, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 0, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 0, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 0, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 0, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 1, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 1, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 1, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 1, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 1, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 2, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 2, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 2, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 2, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 2, r, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * yd[0] * yu[q] * conj(X["41,"][p, 0, q, r, 0, s]),
    (loop) ** (2) * CKM[0, 1] * yd[1] * yu[q] * conj(X["41,"][p, 0, q, r, 1, s]),
    (loop) ** (2) * CKM[0, 2] * yd[2] * yu[q] * conj(X["41,"][p, 0, q, r, 2, s]),
    (loop) ** (2) * CKM[1, 0] * yd[0] * yu[q] * conj(X["41,"][p, 1, q, r, 0, s]),
    (loop) ** (2) * CKM[1, 1] * yd[1] * yu[q] * conj(X["41,"][p, 1, q, r, 1, s]),
    (loop) ** (2) * CKM[1, 2] * yd[2] * yu[q] * conj(X["41,"][p, 1, q, r, 2, s]),
    (loop) ** (2) * CKM[2, 0] * yd[0] * yu[q] * conj(X["41,"][p, 2, q, r, 0, s]),
    (loop) ** (2) * CKM[2, 1] * yd[1] * yu[q] * conj(X["41,"][p, 2, q, r, 1, s]),
    (loop) ** (2) * CKM[2, 2] * yd[2] * yu[q] * conj(X["41,"][p, 2, q, r, 2, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 0, q, r, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 0, q, r, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 0, q, r, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 1, q, r, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 1, q, r, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 1, q, r, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 2, q, r, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 2, q, r, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 2, q, r, 2, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 0, r, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 0, r, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 0, r, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 1, r, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 1, r, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 1, r, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 2, r, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 2, r, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 2, r, q, 2, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 0, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 0, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 0, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 0, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 0, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 0, 2, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 1, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 1, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 1, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 1, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 1, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 1, 2, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 2, 0, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 2, 0, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 2, 0, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 2, 1, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 2, 1, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 2, 1, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, 2, s]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 0, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 0, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 0, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 0, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 0, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 1, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 1, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 1, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 1, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 1, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 2, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 2, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 2, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 2, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 2, r, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * yd[0] * yu[q] * conj(X["41,"][p, 0, q, r, s, 0]),
    (loop) ** (2) * CKM[0, 1] * yd[1] * yu[q] * conj(X["41,"][p, 0, q, r, s, 1]),
    (loop) ** (2) * CKM[0, 2] * yd[2] * yu[q] * conj(X["41,"][p, 0, q, r, s, 2]),
    (loop) ** (2) * CKM[1, 0] * yd[0] * yu[q] * conj(X["41,"][p, 1, q, r, s, 0]),
    (loop) ** (2) * CKM[1, 1] * yd[1] * yu[q] * conj(X["41,"][p, 1, q, r, s, 1]),
    (loop) ** (2) * CKM[1, 2] * yd[2] * yu[q] * conj(X["41,"][p, 1, q, r, s, 2]),
    (loop) ** (2) * CKM[2, 0] * yd[0] * yu[q] * conj(X["41,"][p, 2, q, r, s, 0]),
    (loop) ** (2) * CKM[2, 1] * yd[1] * yu[q] * conj(X["41,"][p, 2, q, r, s, 1]),
    (loop) ** (2) * CKM[2, 2] * yd[2] * yu[q] * conj(X["41,"][p, 2, q, r, s, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 0, q, r, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 0, q, r, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 0, q, r, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 1, q, r, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 1, q, r, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 1, q, r, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 2, q, r, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 2, q, r, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * ye[p]
    * yu[q]
    * conj(X["41,"][p, 2, q, r, s, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * yd[0]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 0, r, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * yd[1]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 0, r, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * yd[2]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 0, r, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * yd[0]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 1, r, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * yd[1]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 1, r, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * yd[2]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 1, r, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * yd[0]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 2, r, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * yd[1]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 2, r, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * yd[2]
    * (yu[r]) ** (2)
    * conj(X["41,"][p, 2, r, q, s, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 0, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 0, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 0, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 0, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 0, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 0, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 0, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 1, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 1, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 1, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 1, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 1, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 1, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 1, 2, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[0]
    * conj(X["41,"][p, 2, 0, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yu[0]
    * conj(X["41,"][p, 2, 0, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yu[0]
    * conj(X["41,"][p, 2, 0, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yu[1]
    * conj(X["41,"][p, 2, 1, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[1]
    * conj(X["41,"][p, 2, 1, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yu[1]
    * conj(X["41,"][p, 2, 1, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[2]
    * conj(X["41,"][p, 2, 2, q, s, 2]),
)

LOOP_LEVEL_MATCHING["41,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 0, r, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 0, r, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 0, r, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 0, r, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 0, r, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 0, r, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 1, r, 0, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 1, r, 0, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 1, r, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 1, r, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 1, r, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 1, r, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 2, r, 0, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 2, r, 0, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 0, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yu[r]
    * conj(X["41,"][p, 2, r, 1, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 2, r, 1, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yu[r]
    * conj(X["41,"][p, 2, r, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["41,"][p, 2, r, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[0, 0] * yd[0] * conj(X["42,"][p, r, s, 0, 0, q]),
    loop * CKM[0, 1] * yd[1] * conj(X["42,"][p, r, s, 0, 1, q]),
    loop * CKM[0, 2] * yd[2] * conj(X["42,"][p, r, s, 0, 2, q]),
    loop * CKM[1, 0] * yd[0] * conj(X["42,"][p, r, s, 1, 0, q]),
    loop * CKM[1, 1] * yd[1] * conj(X["42,"][p, r, s, 1, 1, q]),
    loop * CKM[1, 2] * yd[2] * conj(X["42,"][p, r, s, 1, 2, q]),
    loop * CKM[2, 0] * yd[0] * conj(X["42,"][p, r, s, 2, 0, q]),
    loop * CKM[2, 1] * yd[1] * conj(X["42,"][p, r, s, 2, 1, q]),
    loop * CKM[2, 2] * yd[2] * conj(X["42,"][p, r, s, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[0, 0] * yd[0] * conj(X["42,"][p, r, s, 0, q, 0]),
    loop * CKM[0, 1] * yd[1] * conj(X["42,"][p, r, s, 0, q, 1]),
    loop * CKM[0, 2] * yd[2] * conj(X["42,"][p, r, s, 0, q, 2]),
    loop * CKM[1, 0] * yd[0] * conj(X["42,"][p, r, s, 1, q, 0]),
    loop * CKM[1, 1] * yd[1] * conj(X["42,"][p, r, s, 1, q, 1]),
    loop * CKM[1, 2] * yd[2] * conj(X["42,"][p, r, s, 1, q, 2]),
    loop * CKM[2, 0] * yd[0] * conj(X["42,"][p, r, s, 2, q, 0]),
    loop * CKM[2, 1] * yd[1] * conj(X["42,"][p, r, s, 2, q, 1]),
    loop * CKM[2, 2] * yd[2] * conj(X["42,"][p, r, s, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 0, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, q, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, q, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 0, q, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, q, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 0, q, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, q, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, q, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 1, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, q, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, q, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 1, q, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, q, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 1, q, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, q, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, q, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 2, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, q, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, q, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 2, q, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, q, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 2, q, 2, 0, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, q, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, q, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["42,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 2, 0, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 0, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 0, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 0, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 0, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 0, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 0, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 0, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 1, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 1, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 1, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 1, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 1, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 1, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 2, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 2, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 2, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 2, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 2, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 2, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["42,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 2, 0, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 0, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 0, q, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, q, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, q, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 0, q, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, q, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, q, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 0, q, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, q, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, q, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 1, q, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, q, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, q, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 1, q, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, q, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, q, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 1, q, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, q, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, q, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 2, q, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, q, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, q, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 2, q, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, q, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, q, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, 2, q, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, q, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, q, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 0, q, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 1, q, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, 2, q, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 0, r, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 1, r, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, 2, r, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 0, r, 2, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 1, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 1, r, 2, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, 2, r, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 0, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 0, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 0, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 0, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 0, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 0, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 0, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 0, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 0, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 1, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 1, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 1, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 1, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 1, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 1, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 1, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 1, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 1, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 2, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 2, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 2, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 2, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 2, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 2, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * conj(X["42,"][p, q, 2, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, q, 2, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, q, 2, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 0, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 1, 2, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["42,"][p, q, 2, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["42,"][p, r, 2, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 0, 2, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 1, 2, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 0, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 1, 2, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["42,"][p, 2, 2, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 0, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 1, 2, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 0, 2, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 1, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 1, 2, 2, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["42,"][p, r, 2, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["42,"][p, 0, q, 0, r, s]),
    loop * conj(X["42,"][p, 1, q, 1, r, s]),
    loop * conj(X["42,"][p, 2, q, 2, r, s]),
)

LOOP_LEVEL_MATCHING["42,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["42,"][p, 0, q, 0, r, s]),
    loop * ye[p] * conj(X["42,"][p, 1, q, 1, r, s]),
    loop * ye[p] * conj(X["42,"][p, 2, q, 2, r, s]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["42,"][p, 0, r, 0, q, s]),
    loop * yu[r] * conj(X["42,"][p, 1, r, 1, q, s]),
    loop * yu[r] * conj(X["42,"][p, 2, r, 2, q, s]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["42,"][p, 0, 0, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["42,"][p, 0, 1, 0, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["42,"][p, 0, 2, 0, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["42,"][p, 1, 0, 1, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["42,"][p, 1, 1, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["42,"][p, 1, 2, 1, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["42,"][p, 2, 0, 2, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["42,"][p, 2, 1, 2, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["42,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["42,"][p, 0, r, 0, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["42,"][p, 0, r, 0, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["42,"][p, 0, r, 0, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["42,"][p, 1, r, 1, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["42,"][p, 1, r, 1, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["42,"][p, 1, r, 1, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["42,"][p, 2, r, 2, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["42,"][p, 2, r, 2, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["42,"][p, 2, r, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["42,"][p, q, 0, 0, r, s]),
    loop * conj(X["42,"][p, q, 1, 1, r, s]),
    loop * conj(X["42,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["42,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["42,"][p, q, 0, 0, r, s]),
    loop * ye[p] * conj(X["42,"][p, q, 1, 1, r, s]),
    loop * ye[p] * conj(X["42,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["42,"][p, r, 0, 0, q, s]),
    loop * yu[r] * conj(X["42,"][p, r, 1, 1, q, s]),
    loop * yu[r] * conj(X["42,"][p, r, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["42,"][p, 0, 0, 0, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["42,"][p, 0, 1, 1, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["42,"][p, 0, 2, 2, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["42,"][p, 1, 0, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["42,"][p, 1, 1, 1, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["42,"][p, 1, 2, 2, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["42,"][p, 2, 0, 0, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["42,"][p, 2, 1, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["42,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["42,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["42,"][p, r, 0, 0, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["42,"][p, r, 0, 0, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["42,"][p, r, 0, 0, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["42,"][p, r, 1, 1, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["42,"][p, r, 1, 1, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["42,"][p, r, 1, 1, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["42,"][p, r, 2, 2, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["42,"][p, r, 2, 2, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["42,"][p, r, 2, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["43,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["43,"][p, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["43,"][p, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["43,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["43,"][p, r, q, 0]),
    loop * CKM[s, 1] * yd[1] * conj(X["43,"][p, r, q, 1]),
    loop * CKM[s, 2] * yd[2] * conj(X["43,"][p, r, q, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[0, s] * yd[s] * conj(X["43,"][p, 0, q, r]),
    loop * CKM[1, s] * yd[s] * conj(X["43,"][p, 1, q, r]),
    loop * CKM[2, s] * yd[s] * conj(X["43,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["43,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["43,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["43,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["43,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["43,"][p, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["43,"][p, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["43,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["43,"][p, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["43,"][p, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["43,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * (yu[q]) ** (2) * conj(X["43,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * (yu[q]) ** (2) * conj(X["43,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * (yu[r]) ** (3) * conj(X["43,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * (yu[0]) ** (2) * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * (yu[1]) ** (2) * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * (yu[2]) ** (2) * conj(X["43,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * (yu[r]) ** (2) * conj(X["43,"][p, r, 0, q]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * (yu[r]) ** (2) * conj(X["43,"][p, r, 1, q]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * (yu[r]) ** (2) * conj(X["43,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 0, 0, r]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 0, 1, r]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 0, 2, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 1, 0, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 1, 1, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 1, 2, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 2, 0, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 2, 1, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["43,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["43,"][p, q, 0, r]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["43,"][p, q, 0, r]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["43,"][p, q, 1, r]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["43,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["43,"][p, q, 1, r]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["43,"][p, q, 2, r]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["43,"][p, q, 2, r]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["43,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, 0, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, 0, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, 1, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, 2, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, 2, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, 0, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, 1, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, 2, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 2, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 2, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 0, r, 0]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 0, r, 1]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 0, r, 2]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 1, r, 0]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 1, r, 1]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 1, r, 2]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 2, r, 0]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 2, r, 1]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["43,"][p, q, r, 0]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["43,"][p, q, r, 0]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["43,"][p, q, r, 0]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["43,"][p, q, r, 1]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["43,"][p, q, r, 1]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["43,"][p, q, r, 1]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["43,"][p, q, r, 2]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["43,"][p, q, r, 2]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["43,"][p, q, r, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, r, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, r, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, r, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, r, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, r, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, r, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, q, r, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, q, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, q, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, q, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, q, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, q, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, q, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, r, q, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 2, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 2, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 0, 0, r]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 0, 1, r]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 0, 2, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 1, 0, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 1, 1, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 1, 2, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 2, 0, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 2, 1, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 0, r, 0]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 0, r, 1]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 0, r, 2]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 1, r, 0]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 1, r, 1]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 1, r, 2]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["43,"][p, 2, r, 0]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["43,"][p, 2, r, 1]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["43,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 0]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 1]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[q, 2]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[r]
    * conj(X["43,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, s]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * yd[s]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, s]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * yd[s]
    * conj(X["43,"][p, 2, q, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yd[s]
    * conj(X["43,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 0, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 0, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 0, 1, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 1, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 1, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 2, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 0, 2, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 0, 2, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 0, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 1, 0, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 1, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 1, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 2, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 1, 2, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 1, 2, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 0, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 2, 0, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 0, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * yd[q]
    * conj(X["43,"][p, 2, 1, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 1, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * yd[q]
    * conj(X["43,"][p, 2, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * yd[q]
    * conj(X["43,"][p, 2, 2, 2]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[q, 0] * (yd[0]) ** (2) * conj(X["43,"][p, 0, r, s]),
    (loop) ** (2) * CKM[0, 1] * CKM[q, 1] * (yd[1]) ** (2) * conj(X["43,"][p, 0, r, s]),
    (loop) ** (2) * CKM[0, 2] * CKM[q, 2] * (yd[2]) ** (2) * conj(X["43,"][p, 0, r, s]),
    (loop) ** (2) * CKM[1, 0] * CKM[q, 0] * (yd[0]) ** (2) * conj(X["43,"][p, 1, r, s]),
    (loop) ** (2) * CKM[1, 1] * CKM[q, 1] * (yd[1]) ** (2) * conj(X["43,"][p, 1, r, s]),
    (loop) ** (2) * CKM[1, 2] * CKM[q, 2] * (yd[2]) ** (2) * conj(X["43,"][p, 1, r, s]),
    (loop) ** (2) * CKM[2, 0] * CKM[q, 0] * (yd[0]) ** (2) * conj(X["43,"][p, 2, r, s]),
    (loop) ** (2) * CKM[2, 1] * CKM[q, 1] * (yd[1]) ** (2) * conj(X["43,"][p, 2, r, s]),
    (loop) ** (2) * CKM[2, 2] * CKM[q, 2] * (yd[2]) ** (2) * conj(X["43,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["43,"][p, 0, r, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["43,"][p, 0, r, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["43,"][p, 0, r, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["43,"][p, 1, r, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["43,"][p, 1, r, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["43,"][p, 1, r, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[q, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["43,"][p, 2, r, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[q, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["43,"][p, 2, r, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[q, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["43,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * yu[r]
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * yu[r]
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * yu[r]
    * conj(X["43,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * (CKM[0, 0]) ** (2)
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 0]
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * (CKM[0, 1]) ** (2)
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 0]
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 1]
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * (CKM[0, 2]) ** (2)
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[1, 0]
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * (CKM[1, 0]) ** (2)
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[1, 1]
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * (CKM[1, 1]) ** (2)
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 0]
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 1]
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[1, 2]
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * (CKM[1, 2]) ** (2)
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[2, 0]
    * CKM[r, 0]
    * (yd[0]) ** (3)
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[2, 0]
    * CKM[r, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[2, 1]
    * CKM[r, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[2, 1]
    * CKM[r, 1]
    * (yd[1]) ** (3)
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * (CKM[2, 0]) ** (2)
    * CKM[r, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * (CKM[2, 1]) ** (2)
    * CKM[r, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[2, 2]
    * CKM[r, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[2, 2]
    * CKM[r, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 2, q, s]),
    (loop) ** (2)
    * (CKM[2, 2]) ** (2)
    * CKM[r, 2]
    * (yd[2]) ** (3)
    * conj(X["43,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["43,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["43,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (3)
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * (yd[1]) ** (2)
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 1]
    * (yd[0]) ** (2)
    * yd[1]
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (3)
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * (yd[2]) ** (2)
    * conj(X["43,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 0]
    * CKM[s, 2]
    * (yd[0]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 1]
    * CKM[s, 2]
    * (yd[1]) ** (2)
    * yd[2]
    * conj(X["43,"][p, 2, 2, q]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (3)
    * conj(X["43,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["43,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["43,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["43,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * (ye[p]) ** (2) * conj(X["43,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * (ye[p]) ** (2) * conj(X["43,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * (ye[p]) ** (2) * conj(X["43,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["43,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["43,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["43,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * (ye[p]) ** (2) * conj(X["43,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * (ye[p]) ** (2) * conj(X["43,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * (ye[p]) ** (2) * conj(X["43,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[p]
    * conj(X["43,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * conj(X["43,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (3) * conj(X["43,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * yu[r] * conj(X["43,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * (ye[p]) ** (2) * conj(X["43,"][p, 0, q, s]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * (ye[p]) ** (2) * conj(X["43,"][p, 1, q, s]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * (ye[p]) ** (2) * conj(X["43,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["43,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * (ye[p]) ** (2) * conj(X["43,"][p, r, 0, q]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * (ye[p]) ** (2) * conj(X["43,"][p, r, 1, q]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * (ye[p]) ** (2) * conj(X["43,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * yu[s] * conj(X["44,"][p, r, s, q]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dudH~"][p, q, r, s]] += (
    loop * CKM[0, s] * yd[s] * conj(X["44,"][p, 0, r, q]),
    loop * CKM[1, s] * yd[s] * conj(X["44,"][p, 1, r, q]),
    loop * CKM[2, s] * yd[s] * conj(X["44,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[q] * conj(X["44,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[q] * conj(X["44,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[q] * conj(X["44,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["44,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * yu[q] * conj(X["44,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * yu[q] * conj(X["44,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * yu[q] * conj(X["44,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * (yu[r]) ** (2) * conj(X["44,"][p, 0, r, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * (yu[r]) ** (2) * conj(X["44,"][p, 1, r, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * (yu[r]) ** (2) * conj(X["44,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["44,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["44,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["44,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["44,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["44,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["44,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["44,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["44,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["44,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["44,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["44,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["44,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["44,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * yu[0] * conj(X["44,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * yu[1] * conj(X["44,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * yu[2] * conj(X["44,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * yu[r] * conj(X["44,"][p, r, 0, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * yu[r] * conj(X["44,"][p, r, 1, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * yu[r] * conj(X["44,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["44,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[1]
    * conj(X["44,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[2]
    * conj(X["44,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[0]
    * conj(X["44,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["44,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[2]
    * conj(X["44,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[0]
    * conj(X["44,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[1]
    * conj(X["44,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["44,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[0]
    * conj(X["44,"][p, r, 0, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[0]
    * conj(X["44,"][p, r, 0, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[0]
    * conj(X["44,"][p, r, 0, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[1]
    * conj(X["44,"][p, r, 1, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[1]
    * conj(X["44,"][p, r, 1, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[1]
    * conj(X["44,"][p, r, 1, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[2]
    * conj(X["44,"][p, r, 2, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[2]
    * conj(X["44,"][p, r, 2, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[2]
    * conj(X["44,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[q] * conj(X["44,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[q] * conj(X["44,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[q] * conj(X["44,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["44,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * yu[q] * conj(X["44,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * yu[q] * conj(X["44,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * yu[q] * conj(X["44,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * (yu[r]) ** (2) * conj(X["44,"][p, 0, r, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * (yu[r]) ** (2) * conj(X["44,"][p, 1, r, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * (yu[r]) ** (2) * conj(X["44,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["44,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["44,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["44,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["44,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["44,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["44,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 0]
    * yd[0]
    * yd[s]
    * yu[0]
    * conj(X["44,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 1]
    * yd[1]
    * yd[s]
    * yu[1]
    * conj(X["44,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[2, s]
    * CKM[r, 2]
    * yd[2]
    * yd[s]
    * yu[2]
    * conj(X["44,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["44,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 0]
    * yd[0]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 1]
    * yd[1]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[s, 2]
    * yd[2]
    * yd[q]
    * yu[r]
    * conj(X["44,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * conj(X["45,"][p, r, s, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * (yu[s]) ** (2) * conj(X["45,"][p, s, r, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 0, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 1, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * (yu[s]) ** (2) * conj(X["45,"][p, r, s, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[r] * conj(X["45,"][p, 0, r, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[r] * conj(X["45,"][p, 1, r, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[r] * conj(X["45,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 0, r, 0]),
    (loop) ** (2) * CKM[0, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 0, r, 1]),
    (loop) ** (2) * CKM[0, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 0, r, 2]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 1, r, 0]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 1, r, 1]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 1, r, 2]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 2, r, 0]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 2, r, 1]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 0, 0]),
    (loop) ** (2) * CKM[0, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 0, 1]),
    (loop) ** (2) * CKM[0, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 0, 2]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 1, 0]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 1, 1]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 1, 2]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 2, 0]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 2, 1]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, q] * yd[0] * yd[q] * conj(X["45,"][p, r, s, 0]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, q] * yd[0] * yd[q] * conj(X["45,"][p, r, s, 0]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, q] * yd[0] * yd[q] * conj(X["45,"][p, r, s, 0]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, q] * yd[1] * yd[q] * conj(X["45,"][p, r, s, 1]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, q] * yd[1] * yd[q] * conj(X["45,"][p, r, s, 1]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, q] * yd[1] * yd[q] * conj(X["45,"][p, r, s, 1]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, q] * yd[2] * yd[q] * conj(X["45,"][p, r, s, 2]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, q] * yd[2] * yd[q] * conj(X["45,"][p, r, s, 2]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, q] * yd[2] * yd[q] * conj(X["45,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[r] * conj(X["45,"][p, 0, r, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[r] * conj(X["45,"][p, 1, r, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[r] * conj(X["45,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 0, r, 0]),
    (loop) ** (2) * CKM[0, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 0, r, 1]),
    (loop) ** (2) * CKM[0, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 0, r, 2]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 1, r, 0]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 1, r, 1]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 1, r, 2]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 2, r, 0]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 2, r, 1]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["45,"][p, 0, r, q]),
    (loop) ** (2) * CKM[0, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["45,"][p, 0, r, q]),
    (loop) ** (2) * CKM[0, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["45,"][p, 0, r, q]),
    (loop) ** (2) * CKM[1, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["45,"][p, 1, r, q]),
    (loop) ** (2) * CKM[1, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["45,"][p, 1, r, q]),
    (loop) ** (2) * CKM[1, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["45,"][p, 1, r, q]),
    (loop) ** (2) * CKM[2, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["45,"][p, 2, r, q]),
    (loop) ** (2) * CKM[2, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["45,"][p, 2, r, q]),
    (loop) ** (2) * CKM[2, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["45,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["45,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["45,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["45,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["45,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["45,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["45,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["45,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["45,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["45,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["45,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["45,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["45,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * conj(X["45,"][p, 0, q, r]),
    loop * loop * CKM[1, s] * yd[s] * conj(X["45,"][p, 1, q, r]),
    loop * loop * CKM[2, s] * yd[s] * conj(X["45,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * ye[p] * conj(X["45,"][p, 0, q, r]),
    loop * loop * CKM[1, s] * yd[s] * ye[p] * conj(X["45,"][p, 1, q, r]),
    loop * loop * CKM[2, s] * yd[s] * ye[p] * conj(X["45,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * yu[r] * conj(X["45,"][p, 0, r, q]),
    loop * loop * CKM[1, s] * yd[s] * yu[r] * conj(X["45,"][p, 1, r, q]),
    loop * loop * CKM[2, s] * yd[s] * yu[r] * conj(X["45,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 0, 0, q]),
    loop * loop * CKM[0, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 0, 1, q]),
    loop * loop * CKM[0, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 0, 2, q]),
    loop * loop * CKM[1, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 1, 0, q]),
    loop * loop * CKM[1, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 1, 1, q]),
    loop * loop * CKM[1, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 1, 2, q]),
    loop * loop * CKM[2, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 2, 0, q]),
    loop * loop * CKM[2, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 2, 1, q]),
    loop * loop * CKM[2, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[0, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 0, r, 0]),
    loop * loop * CKM[0, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 0, r, 1]),
    loop * loop * CKM[0, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 0, r, 2]),
    loop * loop * CKM[1, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 1, r, 0]),
    loop * loop * CKM[1, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 1, r, 1]),
    loop * loop * CKM[1, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 1, r, 2]),
    loop * loop * CKM[2, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 2, r, 0]),
    loop * loop * CKM[2, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 2, r, 1]),
    loop * loop * CKM[2, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 0, q]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 1, q]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 0, 0]),
    (loop) ** (2) * CKM[0, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 0, 1]),
    (loop) ** (2) * CKM[0, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 0, 2]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 1, 0]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 1, 1]),
    (loop) ** (2) * CKM[1, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 1, 2]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 2, 0]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 2, 1]),
    (loop) ** (2) * CKM[2, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["45,"][p, r, 0, q]),
    (loop) ** (2) * CKM[0, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["45,"][p, r, 0, q]),
    (loop) ** (2) * CKM[0, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["45,"][p, r, 0, q]),
    (loop) ** (2) * CKM[1, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["45,"][p, r, 1, q]),
    (loop) ** (2) * CKM[1, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["45,"][p, r, 1, q]),
    (loop) ** (2) * CKM[1, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["45,"][p, r, 1, q]),
    (loop) ** (2) * CKM[2, 0] * CKM[s, 0] * (yd[0]) ** (2) * conj(X["45,"][p, r, 2, q]),
    (loop) ** (2) * CKM[2, 1] * CKM[s, 1] * (yd[1]) ** (2) * conj(X["45,"][p, r, 2, q]),
    (loop) ** (2) * CKM[2, 2] * CKM[s, 2] * (yd[2]) ** (2) * conj(X["45,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, r] * CKM[0, s] * yd[r] * yd[s] * conj(X["45,"][p, 0, 0, q]),
    (loop) ** (2) * CKM[0, s] * CKM[1, r] * yd[r] * yd[s] * conj(X["45,"][p, 0, 1, q]),
    (loop) ** (2) * CKM[0, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["45,"][p, 0, 2, q]),
    (loop) ** (2) * CKM[0, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["45,"][p, 1, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[1, s] * yd[r] * yd[s] * conj(X["45,"][p, 1, 1, q]),
    (loop) ** (2) * CKM[1, s] * CKM[2, r] * yd[r] * yd[s] * conj(X["45,"][p, 1, 2, q]),
    (loop) ** (2) * CKM[0, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["45,"][p, 2, 0, q]),
    (loop) ** (2) * CKM[1, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["45,"][p, 2, 1, q]),
    (loop) ** (2) * CKM[2, r] * CKM[2, s] * yd[r] * yd[s] * conj(X["45,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * conj(X["45,"][p, q, 0, r]),
    loop * loop * CKM[1, s] * yd[s] * conj(X["45,"][p, q, 1, r]),
    loop * loop * CKM[2, s] * yd[s] * conj(X["45,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 0, r]),
    loop * loop * CKM[1, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 1, r]),
    loop * loop * CKM[2, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 0, q]),
    loop * loop * CKM[1, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 1, q]),
    loop * loop * CKM[2, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 0, 0, q]),
    loop * loop * CKM[1, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 0, 1, q]),
    loop * loop * CKM[2, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 0, 2, q]),
    loop * loop * CKM[0, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 1, 0, q]),
    loop * loop * CKM[1, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 1, 1, q]),
    loop * loop * CKM[2, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 1, 2, q]),
    loop * loop * CKM[0, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 2, 0, q]),
    loop * loop * CKM[1, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 2, 1, q]),
    loop * loop * CKM[2, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[0, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 0, 0]),
    loop * loop * CKM[0, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 0, 1]),
    loop * loop * CKM[0, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 0, 2]),
    loop * loop * CKM[1, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 1, 0]),
    loop * loop * CKM[1, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 1, 1]),
    loop * loop * CKM[1, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 1, 2]),
    loop * loop * CKM[2, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 2, 0]),
    loop * loop * CKM[2, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 2, 1]),
    loop * loop * CKM[2, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["45,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["45,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["45,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["45,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * conj(X["45,"][p, r, s, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * conj(X["45,"][p, 0, q, r]),
    loop * loop * CKM[1, s] * yd[s] * conj(X["45,"][p, 1, q, r]),
    loop * loop * CKM[2, s] * yd[s] * conj(X["45,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * ye[p] * conj(X["45,"][p, 0, q, r]),
    loop * loop * CKM[1, s] * yd[s] * ye[p] * conj(X["45,"][p, 1, q, r]),
    loop * loop * CKM[2, s] * yd[s] * ye[p] * conj(X["45,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * yu[r] * conj(X["45,"][p, 0, r, q]),
    loop * loop * CKM[1, s] * yd[s] * yu[r] * conj(X["45,"][p, 1, r, q]),
    loop * loop * CKM[2, s] * yd[s] * yu[r] * conj(X["45,"][p, 2, r, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 0, 0, q]),
    loop * loop * CKM[0, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 0, 1, q]),
    loop * loop * CKM[0, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 0, 2, q]),
    loop * loop * CKM[1, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 1, 0, q]),
    loop * loop * CKM[1, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 1, 1, q]),
    loop * loop * CKM[1, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 1, 2, q]),
    loop * loop * CKM[2, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 2, 0, q]),
    loop * loop * CKM[2, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 2, 1, q]),
    loop * loop * CKM[2, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[0, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 0, r, 0]),
    loop * loop * CKM[0, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 0, r, 1]),
    loop * loop * CKM[0, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 0, r, 2]),
    loop * loop * CKM[1, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 1, r, 0]),
    loop * loop * CKM[1, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 1, r, 1]),
    loop * loop * CKM[1, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 1, r, 2]),
    loop * loop * CKM[2, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, 2, r, 0]),
    loop * loop * CKM[2, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, 2, r, 1]),
    loop * loop * CKM[2, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * conj(X["45,"][p, q, 0, r]),
    loop * loop * CKM[1, s] * yd[s] * conj(X["45,"][p, q, 1, r]),
    loop * loop * CKM[2, s] * yd[s] * conj(X["45,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 0, r]),
    loop * loop * CKM[1, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 1, r]),
    loop * loop * CKM[2, s] * yd[s] * ye[p] * conj(X["45,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 0, q]),
    loop * loop * CKM[1, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 1, q]),
    loop * loop * CKM[2, s] * yd[s] * yu[r] * conj(X["45,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 0, 0, q]),
    loop * loop * CKM[1, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 0, 1, q]),
    loop * loop * CKM[2, s] * CKM[r, 0] * yd[0] * yd[s] * conj(X["45,"][p, 0, 2, q]),
    loop * loop * CKM[0, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 1, 0, q]),
    loop * loop * CKM[1, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 1, 1, q]),
    loop * loop * CKM[2, s] * CKM[r, 1] * yd[1] * yd[s] * conj(X["45,"][p, 1, 2, q]),
    loop * loop * CKM[0, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 2, 0, q]),
    loop * loop * CKM[1, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 2, 1, q]),
    loop * loop * CKM[2, s] * CKM[r, 2] * yd[2] * yd[s] * conj(X["45,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["45,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[0, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 0, 0]),
    loop * loop * CKM[0, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 0, 1]),
    loop * loop * CKM[0, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 0, 2]),
    loop * loop * CKM[1, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 1, 0]),
    loop * loop * CKM[1, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 1, 1]),
    loop * loop * CKM[1, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 1, 2]),
    loop * loop * CKM[2, q] * CKM[s, 0] * yd[0] * yd[q] * conj(X["45,"][p, r, 2, 0]),
    loop * loop * CKM[2, q] * CKM[s, 1] * yd[1] * yd[q] * conj(X["45,"][p, r, 2, 1]),
    loop * loop * CKM[2, q] * CKM[s, 2] * yd[2] * yd[q] * conj(X["45,"][p, r, 2, 2]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dudH~"][p, q, r, s]] += (
    loop * conj(X["46,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * (yu[r]) ** (2) * conj(X["46,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * yu[r] * conj(X["46,"][p, r, 0, q]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * yu[r] * conj(X["46,"][p, r, 1, q]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * yu[r] * conj(X["46,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * yu[r] * conj(X["46,"][p, r, q, 0]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * yu[r] * conj(X["46,"][p, r, q, 1]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * yu[r] * conj(X["46,"][p, r, q, 2]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * yu[0] * conj(X["46,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * yu[1] * conj(X["46,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * yu[2] * conj(X["46,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["46,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[q] * conj(X["46,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * yu[q] * conj(X["46,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["46,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * ye[p] * yu[q] * conj(X["46,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * (yu[r]) ** (2) * conj(X["46,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * yd[0] * yu[0] * conj(X["46,"][p, 0, q, s]),
    loop * loop * CKM[r, 1] * yd[1] * yu[1] * conj(X["46,"][p, 1, q, s]),
    loop * loop * CKM[r, 2] * yd[2] * yu[2] * conj(X["46,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[s, 0] * yd[0] * yu[r] * conj(X["46,"][p, r, 0, q]),
    loop * loop * CKM[s, 1] * yd[1] * yu[r] * conj(X["46,"][p, r, 1, q]),
    loop * loop * CKM[s, 2] * yd[2] * yu[r] * conj(X["46,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * yu[r] * conj(X["46,"][p, r, 0, q]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * yu[r] * conj(X["46,"][p, r, 1, q]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * yu[r] * conj(X["46,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["46,"][p, r, 0, q]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["46,"][p, r, 0, q]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["46,"][p, r, 0, q]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["46,"][p, r, 1, q]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["46,"][p, r, 1, q]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["46,"][p, r, 1, q]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["46,"][p, r, 2, q]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["46,"][p, r, 2, q]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["46,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * yu[r] * conj(X["46,"][p, r, q, 0]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * yu[r] * conj(X["46,"][p, r, q, 1]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * yu[r] * conj(X["46,"][p, r, q, 2]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["46,"][p, r, q, 0]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["46,"][p, r, q, 0]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["46,"][p, r, q, 0]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["46,"][p, r, q, 1]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["46,"][p, r, q, 1]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["46,"][p, r, q, 1]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["46,"][p, r, q, 2]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["46,"][p, r, q, 2]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["46,"][p, r, q, 2]),
)

LOOP_LEVEL_MATCHING["46,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[q] * conj(X["46,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["46,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * conj(X["46,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    loop * conj(X["47,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * (yu[q]) ** (2) * conj(X["47,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[r] * conj(X["47,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 0, 0, r]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 0, 1, r]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 0, 2, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 1, 0, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 1, 1, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 1, 2, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 2, 0, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 2, 1, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["47,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["47,"][p, q, 0, r]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["47,"][p, q, 0, r]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["47,"][p, q, 1, r]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["47,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["47,"][p, q, 1, r]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["47,"][p, q, 2, r]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["47,"][p, q, 2, r]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["47,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * ye[p] * conj(X["47,"][p, r, 0, q]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * ye[p] * conj(X["47,"][p, r, 1, q]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * ye[p] * conj(X["47,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 0, r, 0]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 0, r, 1]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 0, r, 2]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 1, r, 0]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 1, r, 1]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 1, r, 2]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 2, r, 0]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 2, r, 1]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["47,"][p, q, r, 0]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["47,"][p, q, r, 0]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["47,"][p, q, r, 0]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["47,"][p, q, r, 1]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["47,"][p, q, r, 1]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["47,"][p, q, r, 1]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["47,"][p, q, r, 2]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["47,"][p, q, r, 2]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["47,"][p, q, r, 2]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * ye[p] * conj(X["47,"][p, r, q, 0]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * ye[p] * conj(X["47,"][p, r, q, 1]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * ye[p] * conj(X["47,"][p, r, q, 2]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 0, 0, r]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 0, 1, r]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 0, 2, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 1, 0, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 1, 1, r]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 1, 2, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 2, 0, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 2, 1, r]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 0, r, 0]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 0, r, 1]),
    (loop) ** (2) * CKM[0, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 0, r, 2]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 1, r, 0]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 1, r, 1]),
    (loop) ** (2) * CKM[1, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 1, r, 2]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 0] * yd[0] * yd[s] * conj(X["47,"][p, 2, r, 0]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 1] * yd[1] * yd[s] * conj(X["47,"][p, 2, r, 1]),
    (loop) ** (2) * CKM[2, s] * CKM[q, 2] * yd[2] * yd[s] * conj(X["47,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[q, 0] * (yd[0]) ** (2) * conj(X["47,"][p, 0, r, s]),
    (loop) ** (2) * CKM[0, 1] * CKM[q, 1] * (yd[1]) ** (2) * conj(X["47,"][p, 0, r, s]),
    (loop) ** (2) * CKM[0, 2] * CKM[q, 2] * (yd[2]) ** (2) * conj(X["47,"][p, 0, r, s]),
    (loop) ** (2) * CKM[1, 0] * CKM[q, 0] * (yd[0]) ** (2) * conj(X["47,"][p, 1, r, s]),
    (loop) ** (2) * CKM[1, 1] * CKM[q, 1] * (yd[1]) ** (2) * conj(X["47,"][p, 1, r, s]),
    (loop) ** (2) * CKM[1, 2] * CKM[q, 2] * (yd[2]) ** (2) * conj(X["47,"][p, 1, r, s]),
    (loop) ** (2) * CKM[2, 0] * CKM[q, 0] * (yd[0]) ** (2) * conj(X["47,"][p, 2, r, s]),
    (loop) ** (2) * CKM[2, 1] * CKM[q, 1] * (yd[1]) ** (2) * conj(X["47,"][p, 2, r, s]),
    (loop) ** (2) * CKM[2, 2] * CKM[q, 2] * (yd[2]) ** (2) * conj(X["47,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["47,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["47,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["47,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~dddD"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * conj(X["47,"][p, 0, q, r]),
    loop * loop * CKM[1, s] * yd[s] * conj(X["47,"][p, 1, q, r]),
    loop * loop * CKM[2, s] * yd[s] * conj(X["47,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * ye[p] * conj(X["47,"][p, 0, q, r]),
    loop * loop * CKM[1, s] * yd[s] * ye[p] * conj(X["47,"][p, 1, q, r]),
    loop * loop * CKM[2, s] * yd[s] * ye[p] * conj(X["47,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[0, q] * CKM[0, s] * yd[q] * yd[s] * conj(X["47,"][p, 0, 0, r]),
    loop * loop * CKM[0, s] * CKM[1, q] * yd[q] * yd[s] * conj(X["47,"][p, 0, 1, r]),
    loop * loop * CKM[0, s] * CKM[2, q] * yd[q] * yd[s] * conj(X["47,"][p, 0, 2, r]),
    loop * loop * CKM[0, q] * CKM[1, s] * yd[q] * yd[s] * conj(X["47,"][p, 1, 0, r]),
    loop * loop * CKM[1, q] * CKM[1, s] * yd[q] * yd[s] * conj(X["47,"][p, 1, 1, r]),
    loop * loop * CKM[1, s] * CKM[2, q] * yd[q] * yd[s] * conj(X["47,"][p, 1, 2, r]),
    loop * loop * CKM[0, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["47,"][p, 2, 0, r]),
    loop * loop * CKM[1, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["47,"][p, 2, 1, r]),
    loop * loop * CKM[2, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["47,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[r] * conj(X["47,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * ye[p] * conj(X["47,"][p, r, 0, q]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * ye[p] * conj(X["47,"][p, r, 1, q]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * ye[p] * conj(X["47,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[s, 0] * yd[0] * ye[p] * conj(X["47,"][p, r, q, 0]),
    (loop) ** (2) * CKM[s, 1] * yd[1] * ye[p] * conj(X["47,"][p, r, q, 1]),
    (loop) ** (2) * CKM[s, 2] * yd[2] * ye[p] * conj(X["47,"][p, r, q, 2]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[p] * conj(X["47,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[p] * conj(X["47,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[p] * conj(X["47,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * conj(X["47,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~qdDd"][p, q, r, s]] += (
    loop * loop * ye[p] * conj(X["47,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * (ye[p]) ** (2) * conj(X["47,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dudH~"][p, q, r, s]] += (
    loop * loop * ye[p] * yu[r] * conj(X["47,"][p, r, q, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[r, 0] * yd[0] * ye[p] * conj(X["47,"][p, 0, q, s]),
    loop * loop * CKM[r, 1] * yd[1] * ye[p] * conj(X["47,"][p, 1, q, s]),
    loop * loop * CKM[r, 2] * yd[2] * ye[p] * conj(X["47,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * loop * CKM[s, 0] * yd[0] * ye[p] * conj(X["47,"][p, r, 0, q]),
    loop * loop * CKM[s, 1] * yd[1] * ye[p] * conj(X["47,"][p, r, 1, q]),
    loop * loop * CKM[s, 2] * yd[2] * ye[p] * conj(X["47,"][p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~dddD"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * conj(X["47,"][p, 0, q, r]),
    loop * loop * CKM[1, s] * yd[s] * conj(X["47,"][p, 1, q, r]),
    loop * loop * CKM[2, s] * yd[s] * conj(X["47,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["l~dddH"][p, q, r, s]] += (
    loop * loop * CKM[0, s] * yd[s] * ye[p] * conj(X["47,"][p, 0, q, r]),
    loop * loop * CKM[1, s] * yd[s] * ye[p] * conj(X["47,"][p, 1, q, r]),
    loop * loop * CKM[2, s] * yd[s] * ye[p] * conj(X["47,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["47,"][G["e~qddH~"][p, q, r, s]] += (
    loop * loop * CKM[0, q] * CKM[0, s] * yd[q] * yd[s] * conj(X["47,"][p, 0, 0, r]),
    loop * loop * CKM[0, s] * CKM[1, q] * yd[q] * yd[s] * conj(X["47,"][p, 0, 1, r]),
    loop * loop * CKM[0, s] * CKM[2, q] * yd[q] * yd[s] * conj(X["47,"][p, 0, 2, r]),
    loop * loop * CKM[0, q] * CKM[1, s] * yd[q] * yd[s] * conj(X["47,"][p, 1, 0, r]),
    loop * loop * CKM[1, q] * CKM[1, s] * yd[q] * yd[s] * conj(X["47,"][p, 1, 1, r]),
    loop * loop * CKM[1, s] * CKM[2, q] * yd[q] * yd[s] * conj(X["47,"][p, 1, 2, r]),
    loop * loop * CKM[0, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["47,"][p, 2, 0, r]),
    loop * loop * CKM[1, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["47,"][p, 2, 1, r]),
    loop * loop * CKM[2, q] * CKM[2, s] * yd[q] * yd[s] * conj(X["47,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[q, 0] * yd[0] * conj(X["48,"][p, 0, r, s]),
    loop * CKM[q, 1] * yd[1] * conj(X["48,"][p, 1, r, s]),
    loop * CKM[q, 2] * yd[2] * conj(X["48,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[q, 0] * yd[0] * conj(X["48,"][p, r, 0, s]),
    loop * CKM[q, 1] * yd[1] * conj(X["48,"][p, r, 1, s]),
    loop * CKM[q, 2] * yd[2] * conj(X["48,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[q, 0] * yd[0] * conj(X["48,"][p, r, s, 0]),
    loop * CKM[q, 1] * yd[1] * conj(X["48,"][p, r, s, 1]),
    loop * CKM[q, 2] * yd[2] * conj(X["48,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["48,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~dddD"][p, q, r, s]] += (
    loop * conj(X["48,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    loop * ye[p] * conj(X["48,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    loop * CKM[0, q] * yd[q] * conj(X["48,"][p, 0, r, s]),
    loop * CKM[1, q] * yd[q] * conj(X["48,"][p, 1, r, s]),
    loop * CKM[2, q] * yd[q] * conj(X["48,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["48,"][p, 0, q, r]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["48,"][p, 0, q, r]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["48,"][p, 0, q, r]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["48,"][p, 1, q, r]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["48,"][p, 1, q, r]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["48,"][p, 1, q, r]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["48,"][p, 2, q, r]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["48,"][p, 2, q, r]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["48,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, 0, q, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, 0, q, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, 0, q, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, 1, q, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, 1, q, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, 1, q, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, 2, q, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, 2, q, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[0, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[0, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[0, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 2, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 2, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["48,"][p, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["48,"][p, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["48,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * (ye[p]) ** (2) * conj(X["48,"][p, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * (ye[p]) ** (2) * conj(X["48,"][p, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * (ye[p]) ** (2) * conj(X["48,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * ye[p] * yu[r] * conj(X["48,"][p, 0, q, s]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * ye[p] * yu[r] * conj(X["48,"][p, 1, q, s]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * ye[p] * yu[r] * conj(X["48,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["48,"][p, q, 0, r]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["48,"][p, q, 0, r]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["48,"][p, q, 0, r]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["48,"][p, q, 1, r]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["48,"][p, q, 1, r]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["48,"][p, q, 1, r]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["48,"][p, q, 2, r]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["48,"][p, q, 2, r]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["48,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, 0, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, 0, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, 1, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, 2, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, 2, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, 2, r]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[0, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[0, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[0, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 0, r]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 1, r]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 2, r]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 2, r]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["48,"][p, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["48,"][p, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["48,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * (ye[p]) ** (2) * conj(X["48,"][p, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * (ye[p]) ** (2) * conj(X["48,"][p, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * (ye[p]) ** (2) * conj(X["48,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * ye[p] * yu[r] * conj(X["48,"][p, q, 0, s]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * ye[p] * yu[r] * conj(X["48,"][p, q, 1, s]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * ye[p] * yu[r] * conj(X["48,"][p, q, 2, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, 2, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, 0] * CKM[0, s] * yd[0] * yd[s] * conj(X["48,"][p, q, r, 0]),
    (loop) ** (2) * CKM[1, 0] * CKM[1, s] * yd[0] * yd[s] * conj(X["48,"][p, q, r, 0]),
    (loop) ** (2) * CKM[2, 0] * CKM[2, s] * yd[0] * yd[s] * conj(X["48,"][p, q, r, 0]),
    (loop) ** (2) * CKM[0, 1] * CKM[0, s] * yd[1] * yd[s] * conj(X["48,"][p, q, r, 1]),
    (loop) ** (2) * CKM[1, 1] * CKM[1, s] * yd[1] * yd[s] * conj(X["48,"][p, q, r, 1]),
    (loop) ** (2) * CKM[2, 1] * CKM[2, s] * yd[1] * yd[s] * conj(X["48,"][p, q, r, 1]),
    (loop) ** (2) * CKM[0, 2] * CKM[0, s] * yd[2] * yd[s] * conj(X["48,"][p, q, r, 2]),
    (loop) ** (2) * CKM[1, 2] * CKM[1, s] * yd[2] * yd[s] * conj(X["48,"][p, q, r, 2]),
    (loop) ** (2) * CKM[2, 2] * CKM[2, s] * yd[2] * yd[s] * conj(X["48,"][p, q, r, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, r, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, r, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, r, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, r, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, r, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, r, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[s]
    * ye[p]
    * conj(X["48,"][p, q, r, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, q]
    * CKM[0, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 0]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, q]
    * CKM[0, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 1]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, q]
    * CKM[0, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, 2]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 0, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[1, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, q]
    * CKM[1, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 0]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[1, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, q]
    * CKM[1, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 1]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[1, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, q]
    * CKM[1, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, 2]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 1, r, 2]),
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[0, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[1, s]
    * CKM[2, q]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[2, q]
    * CKM[2, s]
    * yd[0]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, r, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[0, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[1, s]
    * CKM[2, q]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[2, q]
    * CKM[2, s]
    * yd[1]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, r, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[0, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, r, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[1, s]
    * CKM[2, q]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, r, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[2, q]
    * CKM[2, s]
    * yd[2]
    * yd[q]
    * yd[s]
    * conj(X["48,"][p, 2, r, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["48,"][p, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["48,"][p, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["48,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * (ye[p]) ** (2) * conj(X["48,"][p, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * (ye[p]) ** (2) * conj(X["48,"][p, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * (ye[p]) ** (2) * conj(X["48,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * ye[p] * yu[r] * conj(X["48,"][p, q, s, 0]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * ye[p] * yu[r] * conj(X["48,"][p, q, s, 1]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * ye[p] * yu[r] * conj(X["48,"][p, q, s, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, s, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["48,"][p, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["48,"][p, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["48,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * (ye[p]) ** (2) * conj(X["48,"][p, 0, r, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * (ye[p]) ** (2) * conj(X["48,"][p, 1, r, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * (ye[p]) ** (2) * conj(X["48,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * ye[p] * yu[r] * conj(X["48,"][p, 0, q, s]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * ye[p] * yu[r] * conj(X["48,"][p, 1, q, s]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * ye[p] * yu[r] * conj(X["48,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 0, q, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 1, q, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, q, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["48,"][p, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["48,"][p, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["48,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * (ye[p]) ** (2) * conj(X["48,"][p, r, 0, s]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * (ye[p]) ** (2) * conj(X["48,"][p, r, 1, s]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * (ye[p]) ** (2) * conj(X["48,"][p, r, 2, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * ye[p] * yu[r] * conj(X["48,"][p, q, 0, s]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * ye[p] * yu[r] * conj(X["48,"][p, q, 1, s]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * ye[p] * yu[r] * conj(X["48,"][p, q, 2, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, 0, s]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, q, 0, s]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, 0, s]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, q, 1, s]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, 1, s]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, 1, s]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, 2, s]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, 2, s]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, 2, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 0, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 0, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 0, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 1, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 1, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 1, 2, q]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, 0, q]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, 1, q]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * ye[p] * conj(X["48,"][p, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * ye[p] * conj(X["48,"][p, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * ye[p] * conj(X["48,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[q, 0] * yd[0] * (ye[p]) ** (2) * conj(X["48,"][p, r, s, 0]),
    (loop) ** (2) * CKM[q, 1] * yd[1] * (ye[p]) ** (2) * conj(X["48,"][p, r, s, 1]),
    (loop) ** (2) * CKM[q, 2] * yd[2] * (ye[p]) ** (2) * conj(X["48,"][p, r, s, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[r, 0] * yd[0] * ye[p] * yu[r] * conj(X["48,"][p, q, s, 0]),
    (loop) ** (2) * CKM[r, 1] * yd[1] * ye[p] * yu[r] * conj(X["48,"][p, q, s, 1]),
    (loop) ** (2) * CKM[r, 2] * yd[2] * ye[p] * yu[r] * conj(X["48,"][p, q, s, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, 0]
    * CKM[r, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, s, 0]),
    (loop) ** (2)
    * CKM[1, 0]
    * CKM[r, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, q, s, 0]),
    (loop) ** (2)
    * CKM[2, 0]
    * CKM[r, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, s, 0]),
    (loop) ** (2)
    * CKM[0, 1]
    * CKM[r, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, q, s, 1]),
    (loop) ** (2)
    * CKM[1, 1]
    * CKM[r, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, s, 1]),
    (loop) ** (2)
    * CKM[2, 1]
    * CKM[r, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, s, 1]),
    (loop) ** (2)
    * CKM[0, 2]
    * CKM[r, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, s, 2]),
    (loop) ** (2)
    * CKM[1, 2]
    * CKM[r, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, q, s, 2]),
    (loop) ** (2)
    * CKM[2, 2]
    * CKM[r, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, q, s, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 0]
    * (yd[0]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 0, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 0]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 0, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 0]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 0, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 1]
    * yd[0]
    * yd[1]
    * ye[p]
    * conj(X["48,"][p, 1, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 1]
    * (yd[1]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 1, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 1]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 1, q, 2]),
    (loop) ** (2)
    * CKM[r, 0]
    * CKM[s, 2]
    * yd[0]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, q, 0]),
    (loop) ** (2)
    * CKM[r, 1]
    * CKM[s, 2]
    * yd[1]
    * yd[2]
    * ye[p]
    * conj(X["48,"][p, 2, q, 1]),
    (loop) ** (2)
    * CKM[r, 2]
    * CKM[s, 2]
    * (yd[2]) ** (2)
    * ye[p]
    * conj(X["48,"][p, 2, q, 2]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (2) * conj(X["48,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2) * (ye[p]) ** (3) * conj(X["48,"][p, q, r, s]),
)

LOOP_LEVEL_MATCHING["48,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, q] * yd[q] * (ye[p]) ** (2) * conj(X["48,"][p, 0, r, s]),
    (loop) ** (2) * CKM[1, q] * yd[q] * (ye[p]) ** (2) * conj(X["48,"][p, 1, r, s]),
    (loop) ** (2) * CKM[2, q] * yd[q] * (ye[p]) ** (2) * conj(X["48,"][p, 2, r, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[0] * conj(X["49,"][0, 0, p, q, r, s]),
    loop * ye[1] * conj(X["49,"][1, 1, p, q, r, s]),
    loop * ye[2] * conj(X["49,"][2, 2, p, q, r, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["e~dddD"][p, q, r, s]] += (
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[0] * conj(X["49,"][0, 0, p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[0] * conj(X["49,"][0, 0, p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[0] * conj(X["49,"][0, 0, p, 2, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[1] * conj(X["49,"][1, 1, p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[1] * conj(X["49,"][1, 1, p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[1] * conj(X["49,"][1, 1, p, 2, q, r]),
    (loop) ** (2) * CKM[0, s] * yd[s] * ye[2] * conj(X["49,"][2, 2, p, 0, q, r]),
    (loop) ** (2) * CKM[1, s] * yd[s] * ye[2] * conj(X["49,"][2, 2, p, 1, q, r]),
    (loop) ** (2) * CKM[2, s] * yd[s] * ye[2] * conj(X["49,"][2, 2, p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["49,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["49,"][0, 0, p, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["49,"][0, 0, p, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[0]
    * ye[p]
    * conj(X["49,"][0, 0, p, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["49,"][1, 1, p, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["49,"][1, 1, p, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[1]
    * ye[p]
    * conj(X["49,"][1, 1, p, 2, q, r]),
    (loop) ** (2)
    * CKM[0, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["49,"][2, 2, p, 0, q, r]),
    (loop) ** (2)
    * CKM[1, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["49,"][2, 2, p, 1, q, r]),
    (loop) ** (2)
    * CKM[2, s]
    * yd[s]
    * ye[2]
    * ye[p]
    * conj(X["49,"][2, 2, p, 2, q, r]),
)

LOOP_LEVEL_MATCHING["49,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * ye[0]
    * conj(X["49,"][0, 0, p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * ye[0]
    * conj(X["49,"][0, 0, p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[0]
    * conj(X["49,"][0, 0, p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[0]
    * conj(X["49,"][0, 0, p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[0]
    * conj(X["49,"][0, 0, p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[0]
    * conj(X["49,"][0, 0, p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[0]
    * conj(X["49,"][0, 0, p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[0]
    * conj(X["49,"][0, 0, p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[0]
    * conj(X["49,"][0, 0, p, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * ye[1]
    * conj(X["49,"][1, 1, p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * ye[1]
    * conj(X["49,"][1, 1, p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[1]
    * conj(X["49,"][1, 1, p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[1]
    * conj(X["49,"][1, 1, p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[1]
    * conj(X["49,"][1, 1, p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[1]
    * conj(X["49,"][1, 1, p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[1]
    * conj(X["49,"][1, 1, p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[1]
    * conj(X["49,"][1, 1, p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[1]
    * conj(X["49,"][1, 1, p, 2, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[0, s]
    * yd[q]
    * yd[s]
    * ye[2]
    * conj(X["49,"][2, 2, p, 0, 0, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[1, q]
    * yd[q]
    * yd[s]
    * ye[2]
    * conj(X["49,"][2, 2, p, 0, 1, r]),
    (loop) ** (2)
    * CKM[0, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[2]
    * conj(X["49,"][2, 2, p, 0, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[2]
    * conj(X["49,"][2, 2, p, 1, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[1, s]
    * yd[q]
    * yd[s]
    * ye[2]
    * conj(X["49,"][2, 2, p, 1, 1, r]),
    (loop) ** (2)
    * CKM[1, s]
    * CKM[2, q]
    * yd[q]
    * yd[s]
    * ye[2]
    * conj(X["49,"][2, 2, p, 1, 2, r]),
    (loop) ** (2)
    * CKM[0, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[2]
    * conj(X["49,"][2, 2, p, 2, 0, r]),
    (loop) ** (2)
    * CKM[1, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[2]
    * conj(X["49,"][2, 2, p, 2, 1, r]),
    (loop) ** (2)
    * CKM[2, q]
    * CKM[2, s]
    * yd[q]
    * yd[s]
    * ye[2]
    * conj(X["49,"][2, 2, p, 2, 2, r]),
)

LOOP_LEVEL_MATCHING["49,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * ye[p] * conj(X["49,"][0, 0, p, q, r, s]),
    (loop) ** (2) * ye[1] * ye[p] * conj(X["49,"][1, 1, p, q, r, s]),
    (loop) ** (2) * ye[2] * ye[p] * conj(X["49,"][2, 2, p, q, r, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * (ye[p]) ** (2) * conj(X["49,"][0, 0, p, q, r, s]),
    (loop) ** (2) * ye[1] * (ye[p]) ** (2) * conj(X["49,"][1, 1, p, q, r, s]),
    (loop) ** (2) * ye[2] * (ye[p]) ** (2) * conj(X["49,"][2, 2, p, q, r, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[0] * ye[p] * yu[r] * conj(X["49,"][0, 0, p, r, q, s]),
    (loop) ** (2) * ye[1] * ye[p] * yu[r] * conj(X["49,"][1, 1, p, r, q, s]),
    (loop) ** (2) * ye[2] * ye[p] * yu[r] * conj(X["49,"][2, 2, p, r, q, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[0]
    * ye[p]
    * conj(X["49,"][0, 0, p, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[0]
    * ye[p]
    * conj(X["49,"][0, 0, p, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[0]
    * ye[p]
    * conj(X["49,"][0, 0, p, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[1]
    * ye[p]
    * conj(X["49,"][1, 1, p, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[1]
    * ye[p]
    * conj(X["49,"][1, 1, p, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[1]
    * ye[p]
    * conj(X["49,"][1, 1, p, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * ye[2]
    * ye[p]
    * conj(X["49,"][2, 2, p, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * ye[2]
    * ye[p]
    * conj(X["49,"][2, 2, p, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * ye[2]
    * ye[p]
    * conj(X["49,"][2, 2, p, 2, q, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[0]
    * ye[p]
    * conj(X["49,"][0, 0, p, r, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[0]
    * ye[p]
    * conj(X["49,"][0, 0, p, r, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[0]
    * ye[p]
    * conj(X["49,"][0, 0, p, r, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[1]
    * ye[p]
    * conj(X["49,"][1, 1, p, r, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[1]
    * ye[p]
    * conj(X["49,"][1, 1, p, r, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[1]
    * ye[p]
    * conj(X["49,"][1, 1, p, r, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * ye[2]
    * ye[p]
    * conj(X["49,"][2, 2, p, r, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * ye[2]
    * ye[p]
    * conj(X["49,"][2, 2, p, r, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * ye[2]
    * ye[p]
    * conj(X["49,"][2, 2, p, r, 2, q]),
)

LOOP_LEVEL_MATCHING["49,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["49,"][p, 0, 0, q, r, s]),
    loop * conj(X["49,"][p, 1, 1, q, r, s]),
    loop * conj(X["49,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["49,"][p, 0, 0, q, r, s]),
    loop * ye[p] * conj(X["49,"][p, 1, 1, q, r, s]),
    loop * ye[p] * conj(X["49,"][p, 2, 2, q, r, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["49,"][p, 0, 0, r, q, s]),
    loop * yu[r] * conj(X["49,"][p, 1, 1, r, q, s]),
    loop * yu[r] * conj(X["49,"][p, 2, 2, r, q, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["49,"][p, 0, 0, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["49,"][p, 0, 0, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["49,"][p, 0, 0, 2, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["49,"][p, 1, 1, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["49,"][p, 1, 1, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["49,"][p, 1, 1, 2, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["49,"][p, 2, 2, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["49,"][p, 2, 2, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["49,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["49,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["49,"][p, 0, 0, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["49,"][p, 0, 0, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["49,"][p, 0, 0, r, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["49,"][p, 1, 1, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["49,"][p, 1, 1, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["49,"][p, 1, 1, r, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["49,"][p, 2, 2, r, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["49,"][p, 2, 2, r, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["49,"][p, 2, 2, r, 2, q]),
)

LOOP_LEVEL_MATCHING["50,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[0] * conj(X["50,"][p, 0, r, 0, q, s]),
    loop * yu[1] * conj(X["50,"][p, 1, r, 1, q, s]),
    loop * yu[2] * conj(X["50,"][p, 2, r, 2, q, s]),
)

LOOP_LEVEL_MATCHING["50,"][G["l~qdDd"][p, q, r, s]] += (
    (loop) ** (2) * yu[0] * yu[q] * conj(X["50,"][p, 0, q, 0, r, s]),
    (loop) ** (2) * yu[1] * yu[q] * conj(X["50,"][p, 1, q, 1, r, s]),
    (loop) ** (2) * yu[2] * yu[q] * conj(X["50,"][p, 2, q, 2, r, s]),
)

LOOP_LEVEL_MATCHING["50,"][G["e~qddH~"][p, q, r, s]] += (
    (loop) ** (2) * ye[p] * yu[0] * yu[q] * conj(X["50,"][p, 0, q, 0, r, s]),
    (loop) ** (2) * ye[p] * yu[1] * yu[q] * conj(X["50,"][p, 1, q, 1, r, s]),
    (loop) ** (2) * ye[p] * yu[2] * yu[q] * conj(X["50,"][p, 2, q, 2, r, s]),
)

LOOP_LEVEL_MATCHING["50,"][G["l~dudH~"][p, q, r, s]] += (
    (loop) ** (2) * yu[0] * (yu[r]) ** (2) * conj(X["50,"][p, 0, r, 0, q, s]),
    (loop) ** (2) * yu[1] * (yu[r]) ** (2) * conj(X["50,"][p, 1, r, 1, q, s]),
    (loop) ** (2) * yu[2] * (yu[r]) ** (2) * conj(X["50,"][p, 2, r, 2, q, s]),
)

LOOP_LEVEL_MATCHING["50,"][G["l~dddH"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * (yu[0]) ** (2)
    * conj(X["50,"][p, 0, 0, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[0]
    * yu[1]
    * conj(X["50,"][p, 0, 1, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[0]
    * yu[2]
    * conj(X["50,"][p, 0, 2, 0, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[0]
    * yu[1]
    * conj(X["50,"][p, 1, 0, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * (yu[1]) ** (2)
    * conj(X["50,"][p, 1, 1, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * yu[1]
    * yu[2]
    * conj(X["50,"][p, 1, 2, 1, q, s]),
    (loop) ** (2)
    * CKM[r, 0]
    * yd[0]
    * yu[0]
    * yu[2]
    * conj(X["50,"][p, 2, 0, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 1]
    * yd[1]
    * yu[1]
    * yu[2]
    * conj(X["50,"][p, 2, 1, 2, q, s]),
    (loop) ** (2)
    * CKM[r, 2]
    * yd[2]
    * (yu[2]) ** (2)
    * conj(X["50,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["50,"][G["l~dqqH~"][p, q, r, s]] += (
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * yu[0]
    * yu[r]
    * conj(X["50,"][p, 0, r, 0, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * yu[0]
    * yu[r]
    * conj(X["50,"][p, 0, r, 0, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * yu[0]
    * yu[r]
    * conj(X["50,"][p, 0, r, 0, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * yu[1]
    * yu[r]
    * conj(X["50,"][p, 1, r, 1, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * yu[1]
    * yu[r]
    * conj(X["50,"][p, 1, r, 1, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * yu[1]
    * yu[r]
    * conj(X["50,"][p, 1, r, 1, 2, q]),
    (loop) ** (2)
    * CKM[s, 0]
    * yd[0]
    * yu[2]
    * yu[r]
    * conj(X["50,"][p, 2, r, 2, 0, q]),
    (loop) ** (2)
    * CKM[s, 1]
    * yd[1]
    * yu[2]
    * yu[r]
    * conj(X["50,"][p, 2, r, 2, 1, q]),
    (loop) ** (2)
    * CKM[s, 2]
    * yd[2]
    * yu[2]
    * yu[r]
    * conj(X["50,"][p, 2, r, 2, 2, q]),
)

LOOP_LEVEL_MATCHING["50,"][G["l~qdDd"][p, q, r, s]] += (
    loop * conj(X["50,"][p, q, 0, 0, r, s]),
    loop * conj(X["50,"][p, q, 1, 1, r, s]),
    loop * conj(X["50,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["50,"][G["e~qddH~"][p, q, r, s]] += (
    loop * ye[p] * conj(X["50,"][p, q, 0, 0, r, s]),
    loop * ye[p] * conj(X["50,"][p, q, 1, 1, r, s]),
    loop * ye[p] * conj(X["50,"][p, q, 2, 2, r, s]),
)

LOOP_LEVEL_MATCHING["50,"][G["l~dudH~"][p, q, r, s]] += (
    loop * yu[r] * conj(X["50,"][p, r, 0, 0, q, s]),
    loop * yu[r] * conj(X["50,"][p, r, 1, 1, q, s]),
    loop * yu[r] * conj(X["50,"][p, r, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["50,"][G["l~dddH"][p, q, r, s]] += (
    loop * CKM[r, 0] * yd[0] * conj(X["50,"][p, 0, 0, 0, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["50,"][p, 0, 1, 1, q, s]),
    loop * CKM[r, 0] * yd[0] * conj(X["50,"][p, 0, 2, 2, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["50,"][p, 1, 0, 0, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["50,"][p, 1, 1, 1, q, s]),
    loop * CKM[r, 1] * yd[1] * conj(X["50,"][p, 1, 2, 2, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["50,"][p, 2, 0, 0, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["50,"][p, 2, 1, 1, q, s]),
    loop * CKM[r, 2] * yd[2] * conj(X["50,"][p, 2, 2, 2, q, s]),
)

LOOP_LEVEL_MATCHING["50,"][G["l~dqqH~"][p, q, r, s]] += (
    loop * CKM[s, 0] * yd[0] * conj(X["50,"][p, r, 0, 0, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["50,"][p, r, 0, 0, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["50,"][p, r, 0, 0, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["50,"][p, r, 1, 1, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["50,"][p, r, 1, 1, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["50,"][p, r, 1, 1, 2, q]),
    loop * CKM[s, 0] * yd[0] * conj(X["50,"][p, r, 2, 2, 0, q]),
    loop * CKM[s, 1] * yd[1] * conj(X["50,"][p, r, 2, 2, 1, q]),
    loop * CKM[s, 2] * yd[2] * conj(X["50,"][p, r, 2, 2, 2, q]),
)
