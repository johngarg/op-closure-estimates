#!/usr/bin/env python3

import sympy as sym
from sympy import conjugate as conj
from math import pi
import itertools

from tables import C, G
from constants import CKM, VEV_VAL

X = {}  # C_11, C_12, ...

LOOP_LEVEL_MATCHING = {}
# Fill all dimension-8 operators
for i in range(11, 25):
    LOOP_LEVEL_MATCHING[str(i) + ","] = {}
    X[str(i) + ","] = sym.tensor.Array(sym.symarray(f"C_{i},", (3, 3, 3, 3)))

loop = 1 / (16 * pi ** 2)
# RUNNING MASSES AT m_t taken from 2009.04851 (see also 0712.1419)
yd = [2.56e-3 / VEV_VAL, 50.90e-3 / VEV_VAL, 2.702 / VEV_VAL]
yu = [1.18e-3 / VEV_VAL, 0.594 / VEV_VAL, 161.98 / VEV_VAL]
ye = [0.48583e-6 / VEV_VAL, 102.347e-3 / VEV_VAL, 1.73850 / VEV_VAL]


# TODO 5, 8, 9, 10, 34, 38, 44 are implicitely conjugated! This needs to be
# dealt with in the LaTeX export
for p, q, r, s in list(itertools.product(*[[0, 1, 2]] * 4)):
    LOOP_LEVEL_MATCHING["11,"][C["duql"][s, r, q, p]] = (
        loop * yu[r] * X["11,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["11,"][C["qqql"][s, p, q, r]] = (
        loop * conj(CKM[s, 0]) * yd[0] * X["11,"][p, q, r, 0],
        loop * conj(CKM[s, 1]) * yd[1] * X["11,"][p, q, r, 1],
        loop * conj(CKM[s, 2]) * yd[2] * X["11,"][p, q, r, 2],
    )

    LOOP_LEVEL_MATCHING["12,"][C["duql"][s, r, q, p]] = (
        loop * conj(CKM[q, 0]) * yd[0] * X["12,"][p, r, 0, s],
        loop * conj(CKM[q, 1]) * yd[1] * X["12,"][p, r, 1, s],
        loop * conj(CKM[q, 2]) * yd[2] * X["12,"][p, r, 2, s],
    )

    LOOP_LEVEL_MATCHING["13,"][C["duql"][s, r, q, p]] = (
        loop * yu[q] * X["13,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["13,"][C["duue"][s, q, r, p]] = (
        loop * ye[p] * X["13,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["14,"][C["qqql"][s, p, q, r]] = (
        (loop) ** (2) * yu[r] * yu[s] * X["14,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["14,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * CKM[s, 0] * yd[s] * yu[q] * X["14,"][p, 0, q, r],
        (loop) ** (2) * CKM[s, 1] * yd[s] * yu[q] * X["14,"][p, 1, q, r],
        (loop) ** (2) * CKM[s, 2] * yd[s] * yu[q] * X["14,"][p, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["14,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * CKM[s, 0] * yd[s] * yu[0] * X["14,"][p, q, 0, r],
        (loop) ** (2) * CKM[s, 1] * yd[s] * yu[1] * X["14,"][p, q, 1, r],
        (loop) ** (2) * CKM[s, 2] * yd[s] * yu[2] * X["14,"][p, q, 2, r],
    )

    LOOP_LEVEL_MATCHING["14,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * ye[p] * yu[r] * X["14,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["14,"][C["duue"][s, q, r, p]] = (
        (loop) ** (2) * CKM[s, 0] * yd[s] * ye[p] * X["14,"][p, 0, q, r],
        (loop) ** (2) * CKM[s, 1] * yd[s] * ye[p] * X["14,"][p, 1, q, r],
        (loop) ** (2) * CKM[s, 2] * yd[s] * ye[p] * X["14,"][p, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["15,"][C["duue"][s, q, r, p]] = (
        (loop) ** (2) * yu[q] * yu[r] * X["15,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["15,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[s] * X["15,"][p, q, s, 0],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[s] * X["15,"][p, q, s, 1],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[s] * X["15,"][p, q, s, 2],
    )

    LOOP_LEVEL_MATCHING["15,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * ye[p] * yu[r] * X["15,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["15,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[s] * X["15,"][p, q, r, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[s] * X["15,"][p, q, r, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[s] * X["15,"][p, q, r, 2],
    )

    LOOP_LEVEL_MATCHING["15,"][C["qqql"][s, p, q, r]] = (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * ye[p] * X["15,"][p, q, r, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * ye[p] * X["15,"][p, q, r, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * ye[p] * X["15,"][p, q, r, 2],
    )

    LOOP_LEVEL_MATCHING["16,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * conj(CKM[q, 0]) * yd[0] * yu[r] * X["16,"][p, r, 0, s],
        (loop) ** (2) * conj(CKM[q, 1]) * yd[1] * yu[r] * X["16,"][p, r, 1, s],
        (loop) ** (2) * conj(CKM[q, 2]) * yd[2] * yu[r] * X["16,"][p, r, 2, s],
    )

    LOOP_LEVEL_MATCHING["16,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[r] * X["16,"][p, q, 0, s],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[r] * X["16,"][p, q, 1, s],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[r] * X["16,"][p, q, 2, s],
    )

    LOOP_LEVEL_MATCHING["16,"][C["qqql"][s, p, q, r]] = (
        (loop) ** (2)
        * conj(CKM[r, 0])
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["16,"][p, q, 0, 0],
        (loop) ** (2)
        * conj(CKM[r, 0])
        * conj(CKM[s, 1])
        * yd[0]
        * yd[1]
        * X["16,"][p, q, 0, 1],
        (loop) ** (2)
        * conj(CKM[r, 0])
        * conj(CKM[s, 2])
        * yd[0]
        * yd[2]
        * X["16,"][p, q, 0, 2],
        (loop) ** (2)
        * conj(CKM[r, 1])
        * conj(CKM[s, 0])
        * yd[0]
        * yd[1]
        * X["16,"][p, q, 1, 0],
        (loop) ** (2)
        * conj(CKM[r, 1])
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["16,"][p, q, 1, 1],
        (loop) ** (2)
        * conj(CKM[r, 1])
        * conj(CKM[s, 2])
        * yd[1]
        * yd[2]
        * X["16,"][p, q, 1, 2],
        (loop) ** (2)
        * conj(CKM[r, 2])
        * conj(CKM[s, 0])
        * yd[0]
        * yd[2]
        * X["16,"][p, q, 2, 0],
        (loop) ** (2)
        * conj(CKM[r, 2])
        * conj(CKM[s, 1])
        * yd[1]
        * yd[2]
        * X["16,"][p, q, 2, 1],
        (loop) ** (2)
        * conj(CKM[r, 2])
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["16,"][p, q, 2, 2],
    )

    LOOP_LEVEL_MATCHING["16,"][C["qqql"][s, p, q, r]] = (
        (loop) ** (2)
        * conj(CKM[r, 0])
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["16,"][p, q, 0, 0],
        (loop) ** (2)
        * conj(CKM[r, 1])
        * conj(CKM[s, 0])
        * yd[0]
        * yd[1]
        * X["16,"][p, q, 0, 1],
        (loop) ** (2)
        * conj(CKM[r, 2])
        * conj(CKM[s, 0])
        * yd[0]
        * yd[2]
        * X["16,"][p, q, 0, 2],
        (loop) ** (2)
        * conj(CKM[r, 0])
        * conj(CKM[s, 1])
        * yd[0]
        * yd[1]
        * X["16,"][p, q, 1, 0],
        (loop) ** (2)
        * conj(CKM[r, 1])
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["16,"][p, q, 1, 1],
        (loop) ** (2)
        * conj(CKM[r, 2])
        * conj(CKM[s, 1])
        * yd[1]
        * yd[2]
        * X["16,"][p, q, 1, 2],
        (loop) ** (2)
        * conj(CKM[r, 0])
        * conj(CKM[s, 2])
        * yd[0]
        * yd[2]
        * X["16,"][p, q, 2, 0],
        (loop) ** (2)
        * conj(CKM[r, 1])
        * conj(CKM[s, 2])
        * yd[1]
        * yd[2]
        * X["16,"][p, q, 2, 1],
        (loop) ** (2)
        * conj(CKM[r, 2])
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["16,"][p, q, 2, 2],
    )

    LOOP_LEVEL_MATCHING["17,"][C["qque"][s, p, q, r]] = (
        loop * yu[r] * X["17,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["17,"][C["duue"][s, q, r, p]] = (
        loop * CKM[s, 0] * yd[s] * X["17,"][p, 0, q, r],
        loop * CKM[s, 1] * yd[s] * X["17,"][p, 1, q, r],
        loop * CKM[s, 2] * yd[s] * X["17,"][p, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["18,"][C["qqql"][s, p, q, r]] = (
        (loop) ** (2) * (yu[s]) ** (2) * X["18,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["18,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * CKM[s, 0] * yd[s] * yu[r] * X["18,"][p, 0, q, r],
        (loop) ** (2) * CKM[s, 1] * yd[s] * yu[r] * X["18,"][p, 1, q, r],
        (loop) ** (2) * CKM[s, 2] * yd[s] * yu[r] * X["18,"][p, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["18,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * ye[p] * yu[s] * X["18,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["18,"][C["qqql"][s, p, q, r]] = (
        (loop) ** (2)
        * CKM[0, 0]
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["18,"][p, 0, q, r],
        (loop) ** (2)
        * CKM[1, 0]
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["18,"][p, 0, q, r],
        (loop) ** (2)
        * CKM[2, 0]
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["18,"][p, 0, q, r],
        (loop) ** (2)
        * CKM[0, 1]
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["18,"][p, 1, q, r],
        (loop) ** (2)
        * CKM[1, 1]
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["18,"][p, 1, q, r],
        (loop) ** (2)
        * CKM[2, 1]
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["18,"][p, 1, q, r],
        (loop) ** (2)
        * CKM[0, 2]
        * conj(CKM[s, 0])
        * (yd[0]) ** (2)
        * X["18,"][p, 2, q, r],
        (loop) ** (2)
        * CKM[1, 2]
        * conj(CKM[s, 1])
        * (yd[1]) ** (2)
        * X["18,"][p, 2, q, r],
        (loop) ** (2)
        * CKM[2, 2]
        * conj(CKM[s, 2])
        * (yd[2]) ** (2)
        * X["18,"][p, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["18,"][C["qqql"][s, p, q, r]] = (
        (loop) ** (2) * (ye[p]) ** (2) * X["18,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["18,"][C["qqql"][s, p, q, r]] = (loop * X["18,"][p, q, r, s],)

    LOOP_LEVEL_MATCHING["19,"][C["qqql"][s, p, q, r]] = (
        loop * yu[s] * X["19,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["19,"][C["duql"][s, r, q, p]] = (
        loop * CKM[s, 0] * yd[s] * X["19,"][p, 0, q, r],
        loop * CKM[s, 1] * yd[s] * X["19,"][p, 1, q, r],
        loop * CKM[s, 2] * yd[s] * X["19,"][p, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["19,"][C["qque"][s, p, q, r]] = (
        loop * ye[p] * X["19,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["20,"][C["qque"][s, p, q, r]] = (
        loop * yu[s] * X["20,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["20,"][C["qqql"][s, p, q, r]] = (
        loop * ye[p] * X["20,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["21,"][C["duue"][s, q, r, p]] = (
        loop * yu[r] * X["21,"][p, r, q, s],
    )

    LOOP_LEVEL_MATCHING["21,"][C["qque"][s, p, q, r]] = (
        loop * conj(CKM[r, 0]) * yd[0] * X["21,"][p, q, s, 0],
        loop * conj(CKM[r, 1]) * yd[1] * X["21,"][p, q, s, 1],
        loop * conj(CKM[r, 2]) * yd[2] * X["21,"][p, q, s, 2],
    )

    LOOP_LEVEL_MATCHING["21,"][C["duql"][s, r, q, p]] = (
        loop * ye[p] * X["21,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["22,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * yu[r] * yu[s] * X["22,"][p, q, s, r],
    )

    LOOP_LEVEL_MATCHING["22,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * (yu[s]) ** (2) * X["22,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["22,"][C["qqql"][s, p, q, r]] = (
        (loop) ** (2) * ye[p] * yu[s] * X["22,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["22,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * (yu[r]) ** (2) * X["22,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["22,"][C["duue"][s, q, r, p]] = (
        (loop) ** (2) * CKM[s, 0] * yd[s] * yu[r] * X["22,"][p, 0, r, q],
        (loop) ** (2) * CKM[s, 1] * yd[s] * yu[r] * X["22,"][p, 1, r, q],
        (loop) ** (2) * CKM[s, 2] * yd[s] * yu[r] * X["22,"][p, 2, r, q],
    )

    LOOP_LEVEL_MATCHING["22,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2)
        * CKM[0, 0]
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["22,"][p, 0, q, s],
        (loop) ** (2)
        * CKM[1, 0]
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["22,"][p, 0, q, s],
        (loop) ** (2)
        * CKM[2, 0]
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["22,"][p, 0, q, s],
        (loop) ** (2)
        * CKM[0, 1]
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["22,"][p, 1, q, s],
        (loop) ** (2)
        * CKM[1, 1]
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["22,"][p, 1, q, s],
        (loop) ** (2)
        * CKM[2, 1]
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["22,"][p, 1, q, s],
        (loop) ** (2)
        * CKM[0, 2]
        * conj(CKM[r, 0])
        * (yd[0]) ** (2)
        * X["22,"][p, 2, q, s],
        (loop) ** (2)
        * CKM[1, 2]
        * conj(CKM[r, 1])
        * (yd[1]) ** (2)
        * X["22,"][p, 2, q, s],
        (loop) ** (2)
        * CKM[2, 2]
        * conj(CKM[r, 2])
        * (yd[2]) ** (2)
        * X["22,"][p, 2, q, s],
    )

    LOOP_LEVEL_MATCHING["22,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * CKM[s, 0] * yd[s] * ye[p] * X["22,"][p, 0, q, r],
        (loop) ** (2) * CKM[s, 1] * yd[s] * ye[p] * X["22,"][p, 1, q, r],
        (loop) ** (2) * CKM[s, 2] * yd[s] * ye[p] * X["22,"][p, 2, q, r],
    )

    LOOP_LEVEL_MATCHING["22,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * (ye[p]) ** (2) * X["22,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["22,"][C["qque"][s, p, q, r]] = (loop * X["22,"][p, q, r, s],)

    LOOP_LEVEL_MATCHING["23,"][C["duue"][s, q, r, p]] = (
        (loop) ** (2) * (yu[r]) ** (2) * X["23,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["23,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * yu[q] * X["23,"][p, q, s, 0],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * yu[q] * X["23,"][p, q, s, 1],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * yu[q] * X["23,"][p, q, s, 2],
    )

    LOOP_LEVEL_MATCHING["23,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * ye[p] * yu[q] * X["23,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["23,"][C["duue"][s, q, r, p]] = (
        (loop) ** (2)
        * CKM[s, 0]
        * conj(CKM[0, 0])
        * yd[0]
        * yd[s]
        * X["23,"][p, q, r, 0],
        (loop) ** (2)
        * CKM[s, 1]
        * conj(CKM[1, 0])
        * yd[0]
        * yd[s]
        * X["23,"][p, q, r, 0],
        (loop) ** (2)
        * CKM[s, 2]
        * conj(CKM[2, 0])
        * yd[0]
        * yd[s]
        * X["23,"][p, q, r, 0],
        (loop) ** (2)
        * CKM[s, 0]
        * conj(CKM[0, 1])
        * yd[1]
        * yd[s]
        * X["23,"][p, q, r, 1],
        (loop) ** (2)
        * CKM[s, 1]
        * conj(CKM[1, 1])
        * yd[1]
        * yd[s]
        * X["23,"][p, q, r, 1],
        (loop) ** (2)
        * CKM[s, 2]
        * conj(CKM[2, 1])
        * yd[1]
        * yd[s]
        * X["23,"][p, q, r, 1],
        (loop) ** (2)
        * CKM[s, 0]
        * conj(CKM[0, 2])
        * yd[2]
        * yd[s]
        * X["23,"][p, q, r, 2],
        (loop) ** (2)
        * CKM[s, 1]
        * conj(CKM[1, 2])
        * yd[2]
        * yd[s]
        * X["23,"][p, q, r, 2],
        (loop) ** (2)
        * CKM[s, 2]
        * conj(CKM[2, 2])
        * yd[2]
        * yd[s]
        * X["23,"][p, q, r, 2],
    )

    LOOP_LEVEL_MATCHING["23,"][C["duue"][s, q, r, p]] = (
        (loop) ** (2) * (ye[p]) ** (2) * X["23,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["23,"][C["duue"][s, q, r, p]] = (loop * X["23,"][p, q, r, s],)

    LOOP_LEVEL_MATCHING["24,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * yu[q] * yu[r] * X["24,"][p, r, q, s],
    )

    LOOP_LEVEL_MATCHING["24,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * (yu[r]) ** (2) * X["24,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["24,"][C["qqql"][s, p, q, r]] = (
        (loop) ** (2) * conj(CKM[s, 0]) * yd[0] * yu[r] * X["24,"][p, q, r, 0],
        (loop) ** (2) * conj(CKM[s, 1]) * yd[1] * yu[r] * X["24,"][p, q, r, 1],
        (loop) ** (2) * conj(CKM[s, 2]) * yd[2] * yu[r] * X["24,"][p, q, r, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * (yu[q]) ** (2) * X["24,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["24,"][C["duue"][s, q, r, p]] = (
        (loop) ** (2) * ye[p] * yu[r] * X["24,"][p, r, q, s],
    )

    LOOP_LEVEL_MATCHING["24,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2)
        * CKM[s, 0]
        * conj(CKM[q, 0])
        * yd[0]
        * yd[s]
        * X["24,"][p, 0, r, 0],
        (loop) ** (2)
        * CKM[s, 0]
        * conj(CKM[q, 1])
        * yd[1]
        * yd[s]
        * X["24,"][p, 0, r, 1],
        (loop) ** (2)
        * CKM[s, 0]
        * conj(CKM[q, 2])
        * yd[2]
        * yd[s]
        * X["24,"][p, 0, r, 2],
        (loop) ** (2)
        * CKM[s, 1]
        * conj(CKM[q, 0])
        * yd[0]
        * yd[s]
        * X["24,"][p, 1, r, 0],
        (loop) ** (2)
        * CKM[s, 1]
        * conj(CKM[q, 1])
        * yd[1]
        * yd[s]
        * X["24,"][p, 1, r, 1],
        (loop) ** (2)
        * CKM[s, 1]
        * conj(CKM[q, 2])
        * yd[2]
        * yd[s]
        * X["24,"][p, 1, r, 2],
        (loop) ** (2)
        * CKM[s, 2]
        * conj(CKM[q, 0])
        * yd[0]
        * yd[s]
        * X["24,"][p, 2, r, 0],
        (loop) ** (2)
        * CKM[s, 2]
        * conj(CKM[q, 1])
        * yd[1]
        * yd[s]
        * X["24,"][p, 2, r, 1],
        (loop) ** (2)
        * CKM[s, 2]
        * conj(CKM[q, 2])
        * yd[2]
        * yd[s]
        * X["24,"][p, 2, r, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2)
        * CKM[s, 0]
        * conj(CKM[0, 0])
        * yd[0]
        * yd[s]
        * X["24,"][p, q, r, 0],
        (loop) ** (2)
        * CKM[s, 1]
        * conj(CKM[1, 0])
        * yd[0]
        * yd[s]
        * X["24,"][p, q, r, 0],
        (loop) ** (2)
        * CKM[s, 2]
        * conj(CKM[2, 0])
        * yd[0]
        * yd[s]
        * X["24,"][p, q, r, 0],
        (loop) ** (2)
        * CKM[s, 0]
        * conj(CKM[0, 1])
        * yd[1]
        * yd[s]
        * X["24,"][p, q, r, 1],
        (loop) ** (2)
        * CKM[s, 1]
        * conj(CKM[1, 1])
        * yd[1]
        * yd[s]
        * X["24,"][p, q, r, 1],
        (loop) ** (2)
        * CKM[s, 2]
        * conj(CKM[2, 1])
        * yd[1]
        * yd[s]
        * X["24,"][p, q, r, 1],
        (loop) ** (2)
        * CKM[s, 0]
        * conj(CKM[0, 2])
        * yd[2]
        * yd[s]
        * X["24,"][p, q, r, 2],
        (loop) ** (2)
        * CKM[s, 1]
        * conj(CKM[1, 2])
        * yd[2]
        * yd[s]
        * X["24,"][p, q, r, 2],
        (loop) ** (2)
        * CKM[s, 2]
        * conj(CKM[2, 2])
        * yd[2]
        * yd[s]
        * X["24,"][p, q, r, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][C["qque"][s, p, q, r]] = (
        (loop) ** (2) * conj(CKM[r, 0]) * yd[0] * ye[p] * X["24,"][p, q, s, 0],
        (loop) ** (2) * conj(CKM[r, 1]) * yd[1] * ye[p] * X["24,"][p, q, s, 1],
        (loop) ** (2) * conj(CKM[r, 2]) * yd[2] * ye[p] * X["24,"][p, q, s, 2],
    )

    LOOP_LEVEL_MATCHING["24,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2)
        * CKM[0, 0]
        * conj(CKM[q, 0])
        * (yd[0]) ** (2)
        * X["24,"][p, 0, r, s],
        (loop) ** (2)
        * CKM[1, 0]
        * conj(CKM[q, 1])
        * (yd[1]) ** (2)
        * X["24,"][p, 0, r, s],
        (loop) ** (2)
        * CKM[2, 0]
        * conj(CKM[q, 2])
        * (yd[2]) ** (2)
        * X["24,"][p, 0, r, s],
        (loop) ** (2)
        * CKM[0, 1]
        * conj(CKM[q, 0])
        * (yd[0]) ** (2)
        * X["24,"][p, 1, r, s],
        (loop) ** (2)
        * CKM[1, 1]
        * conj(CKM[q, 1])
        * (yd[1]) ** (2)
        * X["24,"][p, 1, r, s],
        (loop) ** (2)
        * CKM[2, 1]
        * conj(CKM[q, 2])
        * (yd[2]) ** (2)
        * X["24,"][p, 1, r, s],
        (loop) ** (2)
        * CKM[0, 2]
        * conj(CKM[q, 0])
        * (yd[0]) ** (2)
        * X["24,"][p, 2, r, s],
        (loop) ** (2)
        * CKM[1, 2]
        * conj(CKM[q, 1])
        * (yd[1]) ** (2)
        * X["24,"][p, 2, r, s],
        (loop) ** (2)
        * CKM[2, 2]
        * conj(CKM[q, 2])
        * (yd[2]) ** (2)
        * X["24,"][p, 2, r, s],
    )

    LOOP_LEVEL_MATCHING["24,"][C["duql"][s, r, q, p]] = (
        (loop) ** (2) * (ye[p]) ** (2) * X["24,"][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["24,"][C["duql"][s, r, q, p]] = (loop * X["24,"][p, q, r, s],)
