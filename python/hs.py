#!/usr/bin/env python3

"""Results from the Hilbert Series for the ΔB SMEFT up to dimension 10."""

from sympy import Function
from sympy import symbols
from sympy.abc import X

# D = symbolic representation for the derivative
D = symbols("D")

# Treat fields as sympy functions to easily deal with derivatives
H, Hd, L, Ld, Q, Qd = symbols("H Hd L Ld Q Qd", cls=Function)
eb, ebd, ub, ubd, db, dbd = symbols("eb ebd ub ubd db dbd", cls=Function)
G, Gb, W, Wb, B, Bb = symbols("G Gb W Wb B Bb", cls=Function)

H6_ΔB1_ΔL1 = (
    57 * L(X) * Q(X) ** 3
    + 81 * dbd(X) * L(X) * Q(X) * ubd(X)
    - 54 * ebd(X) * Q(X) ** 2 * ubd(X)
    + 81 * dbd(X) * ebd(X) * ubd(X) ** 2
)

H7_ΔBn1_ΔL1 = (
    30 * D * db(X) ** 3 * ebd(X)
    + 24 * db(X) ** 3 * Hd(X) * L(X)
    + -27 * db(X) ** 2 * ebd(X) * H(X) * Qd(X)
    + 54 * D * db(X) ** 2 * L(X) * Qd(X)
    + -81 * db(X) * H(X) * L(X) * Qd(X) ** 2
    + 81 * db(X) ** 2 * H(X) * L(X) * ub(X)
)

H8_ΔB1_ΔL1 = (
    27 * dbd(X) ** 2 * H(X) ** 2 * L(X) * Q(X)
    + 27 * dbd(X) * ebd(X) * H(X) ** 2 * Q(X) ** 2
    + -243 * D * dbd(X) * H(X) * L(X) * Q(X) ** 2
    + 81 * D * ebd(X) * H(X) * Q(X) ** 3
    # + -81 * D ** 2 * L(X) * Q(X) ** 3
    + 138 * H(X) * Hd(X) * L(X) * Q(X) ** 3
    + -135 * D * dbd(X) ** 2 * H(X) * L(X) * ubd(X)
    + -243 * D * dbd(X) * ebd(X) * H(X) * Q(X) * ubd(X)
    # + -162 * D ** 2 * dbd(X) * L(X) * Q(X) * ubd(X)
    + -162 * dbd(X) * H(X) * Hd(X) * L(X) * Q(X) * ubd(X)
    # + 81 * D ** 2 * ebd(X) * Q(X) ** 2 * ubd(X)
    + -81 * ebd(X) * H(X) * Hd(X) * Q(X) ** 2 * ubd(X)
    + 243 * D * Hd(X) * L(X) * Q(X) ** 2 * ubd(X)
    # + -108 * D ** 2 * dbd(X) * ebd(X) * ubd(X) ** 2
    + -81 * dbd(X) * ebd(X) * H(X) * Hd(X) * ubd(X) ** 2
    + -135 * D * dbd(X) * Hd(X) * L(X) * ubd(X) ** 2
    + 135 * D * ebd(X) * Hd(X) * Q(X) * ubd(X) ** 2
    + -27 * Hd(X) ** 2 * L(X) * Q(X) * ubd(X) ** 2
)

# no derivs
H9_ΔB2_ΔL0 = (
    306 * dbd(X) ** 2 * Q(X) ** 4
    + -657 * db(X) ** 3 * Qd(X) ** 2 * ub(X)
    + 468 * db(X) ** 4 * ub(X) ** 2
)

# 12 derivs
H9_ΔBn1_ΔL1 = (
    # 24 * D ** 3 * db(X) ** 3 * ebd(X)
    + 162 * db(X) ** 4 * dbd(X) * ebd(X)
    + -144 * db(X) ** 3 * eb(X) * ebd(X) ** 2
    + 78 * D * db(X) ** 3 * ebd(X) * H(X) * Hd(X)
    # + -138 * D ** 2 * db(X) ** 3 * Hd(X) * L(X)
    + 24 * db(X) ** 3 * H(X) * Hd(X) ** 2 * L(X)
    + -216 * db(X) ** 3 * ebd(X) * L(X) * Ld(X)
    # + 297 * D ** 2 * db(X) ** 2 * ebd(X) * H(X) * Qd(X)
    + -27 * db(X) ** 2 * ebd(X) * H(X) ** 2 * Hd(X) * Qd(X)
    # + 81 * D ** 3 * db(X) ** 2 * L(X) * Qd(X)
    + -729 * db(X) ** 3 * dbd(X) * L(X) * Qd(X)
    + 729 * db(X) ** 2 * eb(X) * ebd(X) * L(X) * Qd(X)
    + -432 * D * db(X) ** 2 * H(X) * Hd(X) * L(X) * Qd(X)
    + -729 * db(X) ** 2 * L(X) ** 2 * Ld(X) * Qd(X)
    + 729 * db(X) ** 3 * ebd(X) * Q(X) * Qd(X)
    + -216 * D * db(X) * ebd(X) * H(X) ** 2 * Qd(X) ** 2
    # + -567 * D ** 2 * db(X) * H(X) * L(X) * Qd(X) ** 2
    + -108 * db(X) * H(X) ** 2 * Hd(X) * L(X) * Qd(X) ** 2
    + -729 * db(X) * eb(X) * L(X) ** 2 * Qd(X) ** 2
    + 2187 * db(X) ** 2 * L(X) * Q(X) * Qd(X) ** 2
    + -24 * ebd(X) * H(X) ** 3 * Qd(X) ** 3
    + 192 * D * H(X) ** 2 * L(X) * Qd(X) ** 3
    + -81 * D * db(X) ** 2 * ebd(X) * H(X) ** 2 * ub(X)
    # + 405 * D ** 2 * db(X) ** 2 * H(X) * L(X) * ub(X)
    + -81 * db(X) ** 2 * H(X) ** 2 * Hd(X) * L(X) * ub(X)
    + -1053 * db(X) ** 2 * eb(X) * L(X) ** 2 * ub(X)
    + 1944 * db(X) ** 3 * L(X) * Q(X) * ub(X)
    + -405 * D * db(X) * H(X) ** 2 * L(X) * Qd(X) * ub(X)
    + 27 * H(X) ** 3 * L(X) * Qd(X) ** 2 * ub(X)
    + -972 * db(X) ** 2 * ebd(X) * Qd(X) ** 2 * ubd(X)
    + 1458 * db(X) * L(X) * Qd(X) ** 3 * ubd(X)
    + -729 * db(X) ** 3 * ebd(X) * ub(X) * ubd(X)
    + 2187 * db(X) ** 2 * L(X) * Qd(X) * ub(X) * ubd(X)
)

# no derivs
H9_ΔB1_ΔL3 = (
    171 * L(X) ** 3 * Q(X) * ubd(X) ** 2 + 72 * ebd(X) * L(X) ** 2 * ubd(X) ** 3
)
