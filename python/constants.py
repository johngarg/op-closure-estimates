#!/usr/bin/env python3

import sympy as sym
from math import sqrt


def build_ckm():
    lamb, A, rho, eta = 0.22500, 0.826, 0.159, 0.348

    ckm = sym.Matrix(
        [
            [1 - 0.5 * lamb ** 2, lamb, A * lamb ** 3 * (rho - 1j * eta)],
            [-lamb, 1 - 0.5 * lamb ** 2, A * lamb ** 2],
            [A * lamb ** 3 * (1 - rho - 1j * eta), -A * lamb ** 2, 1],
        ]
    )
    return ckm


CKM = build_ckm()

MASSES = {
    "n": 0.9395654205,
    "p": 0.93827208816,
    "pi0": 0.1349768,
    "pi+": 0.13957039,
    "pi-": 0.13957039,
    "K0": 0.497611,
    "K+": 0.493677,
    "eta0": 0.547862,
}

GF = 1.1663787e-5
VEV_VAL = 1 / sqrt(2 * sqrt(2) * GF)
