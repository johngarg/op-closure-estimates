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


# Note: There may be duplicates in the below, but this can be ironed out easily
# in the dataframe.
#
# Note: 5, 8, 9, 10, 34, 38, 44 are implicitely conjugated
for p, q, r, s in list(itertools.product(*[[0, 1, 2]] * 4)):
    LOOP_LEVEL_MATCHING["11,"][G["duql"][p, q, r, s]] += (
        (loop * yu[q] * X["11,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["11,"][G["duql"][p, q, r, s]] += (
        (loop * yu[q] * X["11,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["11,"][G["qqql"][p, q, r, s]] += (
        (
            loop * conj(CKM[r, 0]) * yd[0] * X["11,"][s, p, q, 0],
            loop * conj(CKM[r, 1]) * yd[1] * X["11,"][s, p, q, 1],
            loop * conj(CKM[r, 2]) * yd[2] * X["11,"][s, p, q, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["12,"][G["duql"][p, q, r, s]] += (
        (
            loop * conj(CKM[r, 0]) * yd[0] * X["12,"][s, q, 0, p],
            loop * conj(CKM[r, 1]) * yd[1] * X["12,"][s, q, 1, p],
            loop * conj(CKM[r, 2]) * yd[2] * X["12,"][s, q, 2, p],
        ),
    )

    LOOP_LEVEL_MATCHING["12,"][G["duql"][p, q, r, s]] += (
        (
            loop * conj(CKM[r, 0]) * yd[0] * X["12,"][s, q, p, 0],
            loop * conj(CKM[r, 1]) * yd[1] * X["12,"][s, q, p, 1],
            loop * conj(CKM[r, 2]) * yd[2] * X["12,"][s, q, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["13,"][G["duql"][p, q, r, s]] += (
        (loop * yu[r] * X["13,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["13,"][G["duql"][p, q, r, s]] += (
        (loop * yu[r] * X["13,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["13,"][G["duue"][p, q, r, s]] += (
        (loop * ye[s] * X["13,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["14,"][G["qqql"][p, q, r, s]] += (
        ((loop) ** (2) * yu[q] * yu[r] * X["14,"][s, p, q, r],),
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["14,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["14,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["14,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[0] * X["14,"][s, r, 0, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[1] * X["14,"][s, r, 1, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[2] * X["14,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["14,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[s] * X["14,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["14,"][s, 0, q, r],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["14,"][s, 1, q, r],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["14,"][s, 2, q, r],
        ),
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[0] * X["14,"][s, r, q, 0],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[1] * X["14,"][s, r, q, 1],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[2] * X["14,"][s, r, q, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["14,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[s] * X["14,"][q, r, p, s],),
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["14,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["14,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["14,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["14,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["14,"][s, 0, q, r],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["14,"][s, 1, q, r],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["14,"][s, 2, q, r],
        ),
    )

    LOOP_LEVEL_MATCHING["14,"][G["duue"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["14,"][s, 0, q, r],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["14,"][s, 1, q, r],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["14,"][s, 2, q, r],
        ),
    )

    LOOP_LEVEL_MATCHING["14,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[s] * X["14,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["14,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[s] * X["14,"][q, r, p, s],),
    )

    LOOP_LEVEL_MATCHING["14,"][G["duue"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["14,"][s, 0, q, r],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["14,"][s, 1, q, r],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["14,"][s, 2, q, r],
        ),
    )

    LOOP_LEVEL_MATCHING["15,"][G["duue"][p, q, r, s]] += (
        ((loop) ** (2) * yu[q] * yu[r] * X["15,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[p] * X["15,"][q, r, p, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[p] * X["15,"][q, r, p, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[p] * X["15,"][q, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["15,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * ye[s] * yu[q] * X["15,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["15,"][G["duue"][p, q, r, s]] += (
        ((loop) ** (2) * yu[q] * yu[r] * X["15,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[p] * X["15,"][q, r, p, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[p] * X["15,"][q, r, p, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[p] * X["15,"][q, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["15,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * ye[s] * yu[q] * X["15,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[p] * X["15,"][q, r, p, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[p] * X["15,"][q, r, p, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[p] * X["15,"][q, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[p] * X["15,"][q, r, p, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[p] * X["15,"][q, r, p, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[p] * X["15,"][q, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["15,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[p, 0]) * yd[0] * yu[p] * X["15,"][q, r, s, 0],
            (loop) ** (2) * conj(CKM[p, 1]) * yd[1] * yu[p] * X["15,"][q, r, s, 1],
            (loop) ** (2) * conj(CKM[p, 2]) * yd[2] * yu[p] * X["15,"][q, r, s, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["15,"][G["qqql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * ye[s] * X["15,"][s, p, q, 0],
            (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * ye[s] * X["15,"][s, p, q, 1],
            (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * ye[s] * X["15,"][s, p, q, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["15,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * ye[s] * yu[q] * X["15,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["15,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * ye[s] * yu[q] * X["15,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["15,"][G["qqql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * ye[s] * X["15,"][s, p, q, 0],
            (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * ye[s] * X["15,"][s, p, q, 1],
            (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * ye[s] * X["15,"][s, p, q, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["16,"][s, q, 0, p],
            (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["16,"][s, q, 1, p],
            (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["16,"][s, q, 2, p],
        ),
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["16,"][s, q, p, 0],
            (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["16,"][s, q, p, 1],
            (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["16,"][s, q, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["16,"][s, q, 0, p],
            (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["16,"][s, q, 1, p],
            (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["16,"][s, q, 2, p],
        ),
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[q, 0]) * yd[0] * yu[q] * X["16,"][s, r, 0, p],
            (loop) ** (2) * conj(CKM[q, 1]) * yd[1] * yu[q] * X["16,"][s, r, 1, p],
            (loop) ** (2) * conj(CKM[q, 2]) * yd[2] * yu[q] * X["16,"][s, r, 2, p],
        ),
    )

    LOOP_LEVEL_MATCHING["16,"][G["qqql"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["16,"][s, q, p, 0],
            (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["16,"][s, q, p, 1],
            (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["16,"][s, q, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["16,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[q, 0]) * yd[0] * yu[q] * X["16,"][s, r, p, 0],
            (loop) ** (2) * conj(CKM[q, 1]) * yd[1] * yu[q] * X["16,"][s, r, p, 1],
            (loop) ** (2) * conj(CKM[q, 2]) * yd[2] * yu[q] * X["16,"][s, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["16,"][G["qqql"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["17,"][G["qque"][p, q, r, s]] += (
        (loop * yu[s] * X["17,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["17,"][G["qque"][p, q, r, s]] += (
        (loop * yu[s] * X["17,"][q, r, p, s],),
    )

    LOOP_LEVEL_MATCHING["17,"][G["duue"][p, q, r, s]] += (
        (
            loop * conj(CKM[0, p]) * yd[p] * X["17,"][s, 0, q, r],
            loop * conj(CKM[1, p]) * yd[p] * X["17,"][s, 1, q, r],
            loop * conj(CKM[2, p]) * yd[p] * X["17,"][s, 2, q, r],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[r]) ** (2) * X["18,"][s, p, q, r],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[r]) ** (2) * X["18,"][s, p, q, r],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[r]) ** (2) * X["18,"][s, p, q, r],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[q] * X["18,"][s, r, 0, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[q] * X["18,"][s, r, 1, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[q] * X["18,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * ye[q] * yu[p] * X["18,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        ((loop) ** (2) * (ye[s]) ** (2) * X["18,"][s, p, q, r],),
    )

    LOOP_LEVEL_MATCHING["18,"][G["qqql"][p, q, r, s]] += (
        (loop * X["18,"][s, p, q, r],),
    )

    LOOP_LEVEL_MATCHING["19,"][G["qqql"][p, q, r, s]] += (
        (loop * yu[r] * X["19,"][s, p, q, r],),
    )

    LOOP_LEVEL_MATCHING["19,"][G["duql"][p, q, r, s]] += (
        (
            loop * conj(CKM[0, p]) * yd[p] * X["19,"][s, 0, r, q],
            loop * conj(CKM[1, p]) * yd[p] * X["19,"][s, 1, r, q],
            loop * conj(CKM[2, p]) * yd[p] * X["19,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["19,"][G["duql"][p, q, r, s]] += (
        (
            loop * conj(CKM[0, p]) * yd[p] * X["19,"][s, r, 0, q],
            loop * conj(CKM[1, p]) * yd[p] * X["19,"][s, r, 1, q],
            loop * conj(CKM[2, p]) * yd[p] * X["19,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["19,"][G["qque"][p, q, r, s]] += (
        (loop * ye[q] * X["19,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["20,"][G["qque"][p, q, r, s]] += (
        (loop * yu[p] * X["20,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["20,"][G["qque"][p, q, r, s]] += (
        (loop * yu[p] * X["20,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["20,"][G["qque"][p, q, r, s]] += (
        (loop * yu[p] * X["20,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["20,"][G["qqql"][p, q, r, s]] += (
        (loop * ye[s] * X["20,"][s, p, q, r],),
    )

    LOOP_LEVEL_MATCHING["21,"][G["duue"][p, q, r, s]] += (
        (loop * yu[r] * X["21,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["21,"][G["qque"][p, q, r, s]] += (
        (
            loop * conj(CKM[s, 0]) * yd[0] * X["21,"][q, r, p, 0],
            loop * conj(CKM[s, 1]) * yd[1] * X["21,"][q, r, p, 1],
            loop * conj(CKM[s, 2]) * yd[2] * X["21,"][q, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["21,"][G["duql"][p, q, r, s]] += (
        (loop * ye[s] * X["21,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * yu[p] * yu[s] * X["22,"][q, r, p, s],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * yu[p] * yu[s] * X["22,"][q, r, p, s],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[p]) ** (2) * X["22,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qqql"][p, q, r, s]] += (
        ((loop) ** (2) * ye[s] * yu[r] * X["22,"][s, p, q, r],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * yu[p] * yu[s] * X["22,"][q, r, p, s],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[s]) ** (2) * X["22,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["duue"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["22,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["22,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["22,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * yu[p] * yu[s] * X["22,"][q, r, p, s],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[s]) ** (2) * X["22,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["duue"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["22,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["22,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["22,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["duue"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["22,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["22,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["22,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["22,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["22,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["22,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["duue"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * yu[r] * X["22,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * yu[r] * X["22,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * yu[r] * X["22,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["22,"][s, r, 0, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["22,"][s, r, 1, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["22,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["22,"][s, 0, r, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["22,"][s, 1, r, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["22,"][s, 2, r, q],
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["duql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[0, p]) * yd[p] * ye[s] * X["22,"][s, r, 0, q],
            (loop) ** (2) * conj(CKM[1, p]) * yd[p] * ye[s] * X["22,"][s, r, 1, q],
            (loop) ** (2) * conj(CKM[2, p]) * yd[p] * ye[s] * X["22,"][s, r, 2, q],
        ),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        ((loop) ** (2) * (ye[q]) ** (2) * X["22,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["22,"][G["qque"][p, q, r, s]] += (
        (loop * X["22,"][q, r, s, p],),
    )

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[r]) ** (2) * X["23,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["23,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[r] * X["23,"][q, r, p, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[r] * X["23,"][q, r, p, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[r] * X["23,"][q, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["23,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * ye[s] * yu[r] * X["23,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[r]) ** (2) * X["23,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["23,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[r] * X["23,"][q, p, r, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[r] * X["23,"][q, p, r, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[r] * X["23,"][q, p, r, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["23,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * ye[s] * yu[r] * X["23,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["23,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[r] * X["23,"][q, r, p, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[r] * X["23,"][q, r, p, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[r] * X["23,"][q, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["23,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[r] * X["23,"][q, p, r, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[r] * X["23,"][q, p, r, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[r] * X["23,"][q, p, r, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (
        ((loop) ** (2) * (ye[s]) ** (2) * X["23,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["23,"][G["duue"][p, q, r, s]] += (
        (loop * X["23,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * yu[q] * yu[r] * X["24,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[q]) ** (2) * X["24,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["24,"][G["qqql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["24,"][s, p, q, 0],
            (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["24,"][s, p, q, 1],
            (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["24,"][s, p, q, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * yu[q] * yu[r] * X["24,"][s, q, r, p],),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * (yu[r]) ** (2) * X["24,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duue"][p, q, r, s]] += (
        ((loop) ** (2) * ye[s] * yu[r] * X["24,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["24,"][G["qqql"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["24,"][s, p, q, 0],
            (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["24,"][s, p, q, 1],
            (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["24,"][s, p, q, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["24,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * ye[q] * X["24,"][q, r, p, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * ye[q] * X["24,"][q, r, p, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * ye[q] * X["24,"][q, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (
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
        ),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duue"][p, q, r, s]] += (
        ((loop) ** (2) * ye[s] * yu[r] * X["24,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["24,"][G["qque"][p, q, r, s]] += (
        (
            (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * ye[q] * X["24,"][q, r, p, 0],
            (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * ye[q] * X["24,"][q, r, p, 1],
            (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * ye[q] * X["24,"][q, r, p, 2],
        ),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        ((loop) ** (2) * (ye[s]) ** (2) * X["24,"][s, r, q, p],),
    )

    LOOP_LEVEL_MATCHING["24,"][G["duql"][p, q, r, s]] += (
        (loop * X["24,"][s, r, q, p],),
    )
