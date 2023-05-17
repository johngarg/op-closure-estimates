#!/usr/bin/env python3

import sympy as sym
from sympy import conjugate as conj
from math import pi
import itertools

from tables import C, G
from limits import VEV_VAL
from constants import CKM

X = {} # C_11, C_12, ...

LOOP_LEVEL_MATCHING = {
    "11,": {},
    "12,": {},
    "13,": {},
}

loop = 1/(16*pi**2)
# RUNNING MASSES AT m_t taken from 2009.04851 (see also 0712.1419)
yd = [2.56e-3 / VEV_VAL, 50.90e-3 / VEV_VAL, 2.702 / VEV_VAL]
yu = [1.18e-3 / VEV_VAL, 0.594 / VEV_VAL, 161.98 / VEV_VAL]
ye = [0.48583e-6 / VEV_VAL, 102.347e-3 / VEV_VAL, 1.73850 / VEV_VAL]

for k in LOOP_LEVEL_MATCHING:
    X[k] = sym.tensor.Array(sym.symarray(f"C_{k}", (3,3,3,3)))

for p, q, r, s in list(itertools.product(*[[0, 1, 2]] * 4)):
    LOOP_LEVEL_MATCHING["11,"][C["qqql"][p,q,r,s]] = (
        loop*conj(CKM[0, s])*yd[0]*X["11,"][p, q, r, 0],
        loop*conj(CKM[1, s])*yd[1]*X["11,"][p, q, r, 1],
        loop*conj(CKM[2, s])*yd[2]*X["11,"][p, q, r, 2]
    )

    LOOP_LEVEL_MATCHING["11,"][C["duql"][p,q,r,s]] = (
        loop * yu[r] * X['11,'][p, q, r, s],
    )

    LOOP_LEVEL_MATCHING["12,"][C["duql"][p,q,r,s]] = (
        loop * conj(CKM[0,q]) * yd[0] * X['12,'][p, r, 0, s],
        loop * conj(CKM[1,q]) * yd[1] * X['12,'][p, r, 1, s],
        loop * conj(CKM[2,q]) * yd[2] * X['12,'][p, r, 2, s],
    )
