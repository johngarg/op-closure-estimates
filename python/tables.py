#!/usr/bin/env python3

from collections import defaultdict
from fractions import Fraction
import itertools
import sympy as sym
import numpy as np
from math import sqrt

WCXF = {
    "qqql": {
        (1, 1, 1, 1),
        (1, 1, 1, 2),
        (1, 1, 1, 3),
        (1, 1, 2, 1),
        (1, 1, 2, 2),
        (1, 1, 2, 3),
        (1, 1, 3, 1),
        (1, 1, 3, 2),
        (1, 1, 3, 3),
        (1, 2, 1, 1),
        (1, 2, 1, 2),
        (1, 2, 1, 3),
        (1, 2, 2, 1),
        (1, 2, 2, 2),
        (1, 2, 2, 3),
        (1, 2, 3, 1),
        (1, 2, 3, 2),
        (1, 2, 3, 3),
        (1, 3, 1, 1),
        (1, 3, 1, 2),
        (1, 3, 1, 3),
        (1, 3, 2, 1),
        (1, 3, 2, 2),
        (1, 3, 2, 3),
        (1, 3, 3, 1),
        (1, 3, 3, 2),
        (1, 3, 3, 3),
        (2, 1, 2, 1),
        (2, 1, 2, 2),
        (2, 1, 2, 3),
        (2, 1, 3, 1),
        (2, 1, 3, 2),
        (2, 1, 3, 3),
        (2, 2, 2, 1),
        (2, 2, 2, 2),
        (2, 2, 2, 3),
        (2, 2, 3, 1),
        (2, 2, 3, 2),
        (2, 2, 3, 3),
        (2, 3, 1, 1),
        (2, 3, 1, 2),
        (2, 3, 1, 3),
        (2, 3, 2, 1),
        (2, 3, 2, 2),
        (2, 3, 2, 3),
        (2, 3, 3, 1),
        (2, 3, 3, 2),
        (2, 3, 3, 3),
        (3, 1, 3, 1),
        (3, 1, 3, 2),
        (3, 1, 3, 3),
        (3, 2, 3, 1),
        (3, 2, 3, 2),
        (3, 2, 3, 3),
        (3, 3, 3, 1),
        (3, 3, 3, 2),
        (3, 3, 3, 3),
    },
    "qque": {
        (1, 1, 1, 1),
        (1, 1, 1, 2),
        (1, 1, 1, 3),
        (1, 1, 2, 1),
        (1, 1, 2, 2),
        (1, 1, 2, 3),
        (1, 1, 3, 1),
        (1, 1, 3, 2),
        (1, 1, 3, 3),
        (1, 2, 1, 1),
        (1, 2, 1, 2),
        (1, 2, 1, 3),
        (1, 2, 2, 1),
        (1, 2, 2, 2),
        (1, 2, 2, 3),
        (1, 2, 3, 1),
        (1, 2, 3, 2),
        (1, 2, 3, 3),
        (1, 3, 1, 1),
        (1, 3, 1, 2),
        (1, 3, 1, 3),
        (1, 3, 2, 1),
        (1, 3, 2, 2),
        (1, 3, 2, 3),
        (1, 3, 3, 1),
        (1, 3, 3, 2),
        (1, 3, 3, 3),
        (2, 2, 1, 1),
        (2, 2, 1, 2),
        (2, 2, 1, 3),
        (2, 2, 2, 1),
        (2, 2, 2, 2),
        (2, 2, 2, 3),
        (2, 2, 3, 1),
        (2, 2, 3, 2),
        (2, 2, 3, 3),
        (2, 3, 1, 1),
        (2, 3, 1, 2),
        (2, 3, 1, 3),
        (2, 3, 2, 1),
        (2, 3, 2, 2),
        (2, 3, 2, 3),
        (2, 3, 3, 1),
        (2, 3, 3, 2),
        (2, 3, 3, 3),
        (3, 3, 1, 1),
        (3, 3, 1, 2),
        (3, 3, 1, 3),
        (3, 3, 2, 1),
        (3, 3, 2, 2),
        (3, 3, 2, 3),
        (3, 3, 3, 1),
        (3, 3, 3, 2),
        (3, 3, 3, 3),
    },
}

# Limits
PROCESSES = {
    "p->pi0e+",
    "p->pi0mu+",
    "p->eta0e+",
    "p->eta0mu+",
    "p->K0e+",
    "p->K0mu+",
    "p->pi+nu",
    "p->K+nu",
    "n->pi0nu",
    "n->eta0nu",
    "n->K0nu",
    "n->K+e-",
    "n->K+mu-",
    "n->pi-e+",
    "n->pi-mu+",
    "n->pi+e-",
    "n->pi+mu-",
}

HALF = Fraction("1/2")
D6_LEFT_OPERATOR_SYMMETRIES = {
    ###############################
    ####### Delta(B-L) = 0 ########
    ###############################
    ############################### S,LL_udd
    ("S,LL_udd", (1, 1, 1, 1)): (HALF, 0, -1, -1),
    ("S,LL_udd", (1, 2, 1, 1)): (0, 1, -1, -1),
    ("S,LL_udd", (1, 1, 2, 1)): (0, 1, -1, -1),
    ############################### S,LL_duu
    ("S,LL_duu", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    # ("S,LL_duu", (1,1,1,2)): (-HALF, 0, -1, -1),
    ("S,LL_duu", (2, 1, 1, 1)): (-1, 1, -1, -1),
    # ("S,LL_duu", (2,1,1,2)): (-1, 1, -1, -1),
    ############################### S,LR_duu
    ("S,LR_duu", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    # ("S,LR_duu", (1,1,1,2)): (-HALF, -1, -1),
    ("S,LR_duu", (2, 1, 1, 1)): (-1, 1, -1, -1),
    # ("S,LR_duu", (2,1,1,2)): (-1, 1, -1, -1),
    ############################### S,RL_duu
    ("S,RL_duu", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    # ("S,RL_duu", (1,1,1,2)): (-HALF, 0, -1, -1),
    ("S,RL_duu", (2, 1, 1, 1)): (-1, 1, -1, -1),
    # ("S,RL_duu", (2,1,1,2)): (-1, 1, -1, -1),
    ############################### S,RL_dud
    ("S,RL_dud", (1, 1, 1, 1)): (HALF, 0, -1, -1),
    ("S,RL_dud", (2, 1, 1, 1)): (0, 1, -1, -1),
    ("S,RL_dud", (1, 1, 2, 1)): (0, 1, -1, -1),
    ############################### S,RL_ddu
    ("S,RL_ddu", (1, 2, 1, 1)): (0, 1, -1, -1),
    ############################### S,RR_duu
    ("S,RR_duu", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    # ("S,RR_duu", (1,1,1,2)): (-HALF, 0, -1, -1),
    ("S,RR_duu", (2, 1, 1, 1)): (-1, 1, -1, -1),
    # ("S,RR_duu", (2,1,1,2)): (-1, 1, -1, -1),
    ###############################
    ####### Delta(B-L) = -2 #######
    ###############################
    ############################### S,LL_ddd
    ("S,LL_ddd", (1, 2, 1, 1)): (1, 1, -1, 1),
    # ("S,LL_ddd", (1,2,2,1)): (1, 1, -1, 1),
    ############################### S,LR_udd
    ("S,LR_udd", (1, 1, 1, 1)): (HALF, 0, -1, 1),
    ("S,LR_udd", (1, 2, 1, 1)): (0, 1, -1, 1),
    ("S,LR_udd", (1, 1, 1, 2)): (0, 1, -1, 1),
    ############################### S,LR_ddu
    ("S,LR_ddu", (1, 2, 1, 1)): (0, 1, -1, 1),
    ############################### S,LR_ddd
    ("S,LR_ddd", (1, 2, 1, 1)): (1, 1, -1, 1),
    # ("S,LR_ddd", (1,2,2,1)): (1, 1, -1, 1)
    ############################### S,RL_ddd
    ("S,RL_ddd", (1, 2, 1, 1)): (1, 1, -1, 1),
    # ("S,RL_ddd", (1,2,2,1)): (1, 1, -1, 1)
    ############################### S,RR_udd
    ("S,RR_udd", (1, 1, 1, 1)): (HALF, 0, -1, 1),
    ("S,RR_udd", (1, 2, 1, 1)): (0, 1, -1, 1),
    ("S,RR_udd", (1, 1, 1, 2)): (0, 1, -1, 1),
    ############################### S,RR_ddd
    ("S,RR_ddd", (1, 2, 1, 1)): (1, 1, -1, 1),
    # ("S,RR_ddd", (1,2,2,1)): (1, 1, -1, 1),
}

D7_LEFT_OPERATOR_SYMMETRIES = {
    ###############################
    ####### Delta(B-L) = 0 ########
    ###############################
    ############################### V,LR_udd
    ("V,LR_udd", (1, 1, 1, 1)): (HALF, 0, -1, -1),
    ("V,LR_udd", (1, 2, 1, 1)): (0, 1, -1, -1),
    ("V,LR_udd", (1, 1, 1, 2)): (0, 1, -1, -1),
    ############################### V,LR_ddu
    ("V,LR_ddu", (1, 1, 1, 1)): (HALF, 0, -1, -1),
    ("V,LR_ddu", (1, 2, 1, 1)): (0, 1, -1, -1),
    ############################### V,RR_ddu
    ("V,RR_ddu", (1, 1, 1, 1)): (HALF, 0, -1, -1),
    ("V,RR_ddu", (1, 2, 1, 1)): (0, 1, -1, -1),
    ############################### V,LR_uud
    ("V,LR_uud", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    # ("V,LR_uud", (1,1,1,2)): (-HALF, 0, -1, -1)
    ("V,LR_uud", (1, 1, 2, 1)): (-1, 1, -1, -1),
    # ("V,LR_uud", (1,1,2,2)): (-1, 1, -1, -1),
    ############################### V,RR_uud
    ("V,RR_uud", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    # ("V,RR_uud", (1,1,1,2)): (-HALF, 0, -1, -1)
    ("V,RR_uud", (1, 1, 2, 1)): (-1, 1, -1, -1),
    # ("V,RR_uud", (1,1,2,2)): (-1, 1, -1, -1),
    ############################### V,LR_udu
    ("V,LR_udu", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    # ("V,LR_udu", (1,1,1,2)): (-HALF, 0, -1, -1),
    ("V,LR_udu", (1, 2, 1, 1)): (-1, 1, -1, -1),
    # ("V,LR_udu", (1,2,1,2)): (-1, 1, -1, -1),
    ############################### V,LL_uud
    ("V,LL_uud", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    # ("V,LL_uud", (1,1,1,2)): (-HALF, 0, -1, -1),
    ("V,LL_uud", (1, 1, 2, 1)): (-1, 1, -1, -1),
    # ("V,LL_uud", (1,1,2,2)): (-1, 1, -1, -1),
    ############################### V,RL_uud
    ("V,RL_uud", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    # ("V,RL_uud", (1,1,1,2)): (-HALF, 0, -1, -1),
    ("V,RL_uud", (1, 1, 2, 1)): (-1, 1, -1, -1),
    # ("V,RL_uud", (1,1,2,2)): (-1, 1, -1, -1),
    ############################### V,RL_udu
    ("V,RL_udu", (1, 1, 1, 1)): (-HALF, 0, -1, -1),
    ("V,RL_udu", (1, 2, 1, 1)): (-1, 1, -1, -1),
    ###############################
    ####### Delta(B-L) = -2 #######
    ###############################
    ############################### V,RL_dud
    ("V,RL_dud", (1, 1, 1, 1)): (HALF, 0, -1, 1),
    ("V,RL_dud", (2, 1, 1, 1)): (0, 1, -1, 1),
    ("V,RL_dud", (1, 1, 1, 2)): (0, 1, -1, 1),
    ############################### V,LL_ddu
    ("V,LL_ddu", (1, 1, 1, 1)): (HALF, 0, -1, 1),
    ("V,LL_ddu", (1, 2, 1, 1)): (0, 1, -1, 1),
    ############################### V,RL_ddu
    ("V,RL_ddu", (1, 1, 1, 1)): (HALF, 0, -1, 1),
    ("V,RL_ddu", (1, 2, 1, 1)): (0, 1, -1, 1),
    ############################### V,LL_ddd
    ## Careful here that lepton index is last!
    ("V,LL_ddd", (1, 1, 1, 1)): (3 * HALF, 0, -1, 1),
    # ("V,LL_ddd", (1,1,1,2)): (3*HALF, 0, -1, 1),
    ("V,LL_ddd", (1, 2, 1, 1)): (1, 1, -1, 1),
    # ("V,LL_ddd", (1,2,1,2)): (1, 1, -1, 1),
    ############################### V,RL_ddd
    ("V,RL_ddd", (1, 1, 1, 1)): (3 * HALF, 0, -1, 1),
    # ("V,RL_ddd", (1,1,2,1)): (3*HALF, 0, -1, 1),
    ("V,RL_ddd", (1, 2, 1, 1)): (1, 1, -1, 1),
    # ("V,RL_ddd", (1,2,2,1)): (1,1, -1, 1),
    ("V,RL_ddd", (1, 1, 1, 2)): (1, 1, -1, 1),
    # ("V,RL_ddd", (1,1,2,2)): (1,1, -1, 1),
    ############################### V,LR_ddd
    ("V,LR_ddd", (1, 1, 1, 1)): (3 * HALF, 0, -1, 1),
    # ("V,LR_ddd", (1,1,2,1)): (3*HALF, 0, -1, 1),
    ("V,LR_ddd", (1, 2, 1, 1)): (1, 1, -1, 1),
    # ("V,LR_ddd", (1,2,2,1)): (1,1, -1, 1),
    ("V,LR_ddd", (1, 1, 1, 2)): (1, 1, -1, 1),
    # ("V,LR_ddd", (1,1,2,2)): (1,1, -1, 1),
    ############################### V,RR_ddd
    ## Careful here that lepton index is last!
    ("V,RR_ddd", (1, 1, 1, 1)): (3 * HALF, 0, -1, 1),
    # ("V,RR_ddd", (1,1,1,2)): (3*HALF, 0, -1, 1),
    ("V,RR_ddd", (1, 2, 1, 1)): (1, 1, -1, 1),
    # ("V,RR_ddd", (1,2,1,2)): (1, 1, -1, 1),
}

ALLOWED_PROCESSES = {
    (-HALF, 0, -1, -1): ["p->pi0e+", "p->eta0e+", "n->pi-e+"],
    (HALF, 0, -1, -1): ["p->pi+nu", "n->pi0nu", "n->eta0nu"],
    (HALF, 0, -1, 1): ["p->pi+nu", "n->pi0nu", "n->eta0nu"],
    (-1, 1, -1, -1): ["p->K0e+"],
    (0, 1, -1, -1): ["p->K+nu", "n->K0nu"],
    (0, 1, -1, 1): ["p->K+nu", "n->K0nu"],
    (1, 1, -1, 1): ["n->K+e-"],
    (3 * HALF, 0, -1, 1): ["n->pi+e-"],
    ## Should not appear
    # (0, -1, -1, -1): ["p->K0e+", "n->K-e+"],
    # (1, -1, -1, -1): ["n->K0nu"],
    # (1, -1, -1, 1): ["n->K0nu"],
}


V = sym.MatrixSymbol("V", 3, 3)
VEV = sym.Symbol("VEV", real=True)
LAMBDA = sym.Symbol("LAMBDA", real=True)
C, K, G = {}, {}, {}
smeft_coefficient_labels = {
    "qqql",  # 1
    "qque",  # 2
    "duue",  # 3
    "duql",  # 4
    "l~dddH",  # conj(5)
    "l~dqqH~",  # conj(8)
    "e~qddH~",  # conj(9)
    "l~dudH~",  # conj(10)
    "l~qdDd",
    "e~dddD",
    "ddqlHH",  # 16
    "eqqqHHH",  # 26
    "luqqHHH",  # 37
    "qqedHHD",
    "qqlqHHD",
    "udqlHHD",
}


def set_symmetry(label, key, zero_expr):
    p, r, s, q = key

    # If the operator coefficient has already been removed, it is redundant and
    # can be expressed in terms of others
    if K[label][p, r, s, q] in removed:
        C[label][p, r, s, q] = removed[K[label][p, r, s, q]]
        return

    # Replace redundant operators, wherever they are in the expression
    zero_expr_replaced = zero_expr.xreplace(removed)
    if zero_expr_replaced == 0:
        C[label][p, r, s, q] = K[label][p, r, s, q]
        return

    to_remove = K[label][p, r, s, q]

    # Make sure that throwing away the coefficient with the _largest_ flavour
    # indices correctly reproduces the wcxf Warsaw basis:
    # https://wcxf.github.io/assets/pdf/SMEFT.Warsaw.pdf
    if label in WCXF:
        assert (p + 1, r + 1, s + 1, q + 1) not in WCXF[label]

    sol = sym.solve(zero_expr_replaced, to_remove)
    assert len(sol) == 1
    removed[to_remove] = sol[0]
    removed_tally[label].append(to_remove)
    assert K[label][p, r, s, q] in removed
    C[label][p, r, s, q] = sol[0]
    return


for label in smeft_coefficient_labels:
    C[label] = sym.symarray(f"K_{label}", (3, 3, 3, 3))
    K[label] = sym.symarray(f"C_{label}", (3, 3, 3, 3))

removed = {}
removed_tally = defaultdict(list)
## Declare (anti)symmetric couplings below.
for p, q, r, s in list(itertools.product(*[[2, 1, 0]] * 4)):
    # Dimension 6 (10.1.2: https://arxiv.org/pdf/1804.05863.pdf)
    lbl = "qque"
    set_symmetry(lbl, (p, q, r, s), K[lbl][p, q, r, s] - K[lbl][q, p, r, s])
    lbl = "qqql"
    set_symmetry(
        lbl,
        (p, r, s, q),
        K[lbl][p, r, s, q]
        + K[lbl][r, p, s, q]
        - K[lbl][s, p, r, q]
        - K[lbl][s, r, p, q],
    )

    # Dimension 7 (Table 2: https://arxiv.org/pdf/1901.10302.pdf and eq. 6)
    # Symmetry here is {2,1}
    lbl = "l~dddH"
    set_symmetry(lbl, (p, q, r, s), K[lbl][p, q, r, s] + K[lbl][p, q, s, r])
    ## These symmetries are now implemented by hand below
    # set_symmetry(
    #     lbl, (p, r, s, q), K[lbl][p, r, s, q] + K[lbl][p, s, q, r] + K[lbl][p, q, r, s]
    # )
    lbl = "e~qddH~"
    set_symmetry(lbl, (p, q, r, s), K[lbl][p, q, r, s] + K[lbl][p, q, s, r])

    lbl = "l~qdDd"
    set_symmetry(lbl, (p, q, r, s), K[lbl][p, q, r, s] - K[lbl][p, q, s, r])
    # Symmetrise on all three quark indices manually
    lbl = "e~dddD"
    Q, R, S = sorted([q, r, s])
    C[lbl][p, q, r, s] = K[lbl][p, Q, R, S]

    # Dimension 8 (Checked with Sym2Int)
    lbl = "ddqlHH"
    set_symmetry(lbl, (p, q, r, s), K[lbl][p, q, r, s] + K[lbl][q, p, r, s])

    # Dimension 9 (From https://arxiv.org/pdf/2007.08125.pdf p. 19)
    lbl = "eqqqHHH"
    set_symmetry(lbl, (p, q, r, s), K[lbl][p, q, r, s] + K[lbl][p, q, s, r])
    ## These symmetries are now implemented by hand below
    # set_symmetry(
    #     lbl, (p, r, s, q), K[lbl][p, r, s, q] + K[lbl][p, s, q, r] + K[lbl][p, q, r, s]
    # )

    lbl = "luqqHHH"
    set_symmetry(lbl, (p, q, r, s), K[lbl][p, q, r, s] + K[lbl][p, q, s, r])
    lbl = "qqedHHD"
    set_symmetry(lbl, (p, q, r, s), K[lbl][p, q, r, s] - K[lbl][q, p, r, s])
    lbl = "qqlqHHD"
    set_symmetry(lbl, (p, q, r, s), K[lbl][p, q, r, s] - K[lbl][q, p, r, s])

## Implement additional symmetries for l~dddH and eqqqHHH
set_symmetry(
    "l~dddH",
    (2, 2, 1, 0),
    K["l~dddH"][2, 0, 2, 1] + K["l~dddH"][2, 1, 0, 2] + K["l~dddH"][2, 2, 1, 0],
)
set_symmetry(
    "l~dddH",
    (1, 2, 1, 0),
    K["l~dddH"][1, 0, 2, 1] + K["l~dddH"][1, 1, 0, 2] + K["l~dddH"][1, 2, 1, 0],
)
set_symmetry(
    "l~dddH",
    (0, 2, 1, 0),
    K["l~dddH"][0, 0, 2, 1] + K["l~dddH"][0, 1, 0, 2] + K["l~dddH"][0, 2, 1, 0],
)

set_symmetry(
    "eqqqHHH",
    (2, 2, 1, 0),
    K["eqqqHHH"][2, 0, 2, 1] + K["eqqqHHH"][2, 1, 0, 2] + K["eqqqHHH"][2, 2, 1, 0],
)
set_symmetry(
    "eqqqHHH",
    (1, 2, 1, 0),
    K["eqqqHHH"][1, 0, 2, 1] + K["eqqqHHH"][1, 1, 0, 2] + K["eqqqHHH"][1, 2, 1, 0],
)
set_symmetry(
    "eqqqHHH",
    (0, 2, 1, 0),
    K["eqqqHHH"][0, 0, 2, 1] + K["eqqqHHH"][0, 1, 0, 2] + K["eqqqHHH"][0, 2, 1, 0],
)

## Convert to array called G
for k, v in C.items():
    G[k] = sym.tensor.Array(v)

# The following is just a convenient way of transcribing the matching
# information into a dictionary. Importantly, the entries in TREE_LEVEL_MATCHING
# will be overcomplete and some will be erroneous, e.g. it will contain
# C_ddqlHH[1,1,1,1] = 0, but this will never be accessed.
TREE_LEVEL_MATCHING_STR = {}
for p, q, r, s in list(itertools.product(*[[0, 1]] * 4)):

    # Delta (B - L) = 0
    TREE_LEVEL_MATCHING_STR[
        ("S,LL_udd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"V[{q}, qp] * V[{r}, rp] * (G['qqql'][rp, qp, {p}, {s}] - G['qqql'][rp, {p}, qp, {s}] + G['qqql'][qp, {p}, rp, {s}]), (qp, 0, 2), (rp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,LL_duu", (p + 1, q + 1, r + 1, s + 1))
    ] = f"V[{p}, pp] * (G['qqql'][{r}, {q}, pp, {s}] - G['qqql'][{r}, pp, {q}, {s}] + G['qqql'][{q}, pp, {r}, {s}]), (pp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,LR_duu", (p + 1, q + 1, r + 1, s + 1))
    ] = f"- V[{p}, pp] * (G['qque'][pp, {q}, {r}, {s}] + G['qque'][{q}, pp, {r}, {s}]), (pp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,RL_duu", (p + 1, q + 1, r + 1, s + 1))
    ] = f"G['duql'][{p}, {q}, {r}, {s}]"

    TREE_LEVEL_MATCHING_STR[
        ("S,RL_dud", (p + 1, q + 1, r + 1, s + 1))
    ] = f"- V[{r}, rp] * G['duql'][{p}, {q}, rp, {s}], (rp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,RL_ddu", (p + 1, q + 1, r + 1, s + 1))
    ] = f"(G['ddqlHH'][{p}, {q}, {r}, {s}] - G['ddqlHH'][{q}, {p}, {r}, {s}]) * VEV**2 / (2 * LAMBDA**2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,RR_duu", (p + 1, q + 1, r + 1, s + 1))
    ] = f"G['duue'][{p}, {q}, {r}, {s}]"

    # Delta (B - L) = -2
    TREE_LEVEL_MATCHING_STR[
        ("S,LL_ddd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"V[{s}, sp] * V[{p}, pp] * V[{q}, qp] * (G['eqqqHHH'][{r}, sp, pp, qp] - G['eqqqHHH'][{r}, sp, qp, pp]) * VEV**3 / (2*sym.sqrt(2)*LAMBDA**3), (sp, 0, 2), (pp, 0, 2), (qp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,LR_udd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"- V[{q}, qp] * G['l~dqqH~'][{r}, {s}, {p}, qp] * VEV / (sym.sqrt(2)*LAMBDA), (qp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,LR_ddu", (p + 1, q + 1, r + 1, s + 1))
    ] = f"V[{p}, pp] * V[{q}, qp] * (G['luqqHHH'][{r}, {s}, pp, qp] - G['luqqHHH'][{r}, {s}, qp, pp]) * VEV**3 / (2*sym.sqrt(2)*LAMBDA**3), (pp, 0, 2), (qp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,LR_ddd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"V[{p}, pp] * V[{q}, qp] * (G['l~dqqH~'][{r}, {s}, qp, pp] - G['l~dqqH~'][{r}, {s}, pp, qp]) * VEV / (sym.sqrt(2)*LAMBDA), (pp, 0, 2), (qp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,RL_ddd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"V[{s}, sp] * (G['e~qddH~'][{r}, sp, {q}, {p}] - G['e~qddH~'][{r}, sp, {p}, {q}]) * VEV / (sym.sqrt(2)*LAMBDA), (sp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("S,RR_udd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"G['l~dudH~'][{r}, {s}, {p}, {q}] * VEV / (sym.sqrt(2)*LAMBDA)"

    TREE_LEVEL_MATCHING_STR[
        ("S,RR_ddd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"G['l~dddH'][{r}, {s}, {p}, {q}] * VEV / (sym.sqrt(2)*LAMBDA)"

    # Dimension 7
    # \Delta(B - L) = 0
    TREE_LEVEL_MATCHING_STR[
        ("V,RL_ddu", (p + 1, q + 1, r + 1, s + 1))
    ] = f"- G['l~qdDd'][{s}, {r}, {p}, {q}]"

    TREE_LEVEL_MATCHING_STR[
        ("V,RL_ddd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"- V[{r}, rp] * G['l~qdDd'][{s}, rp, {p}, {q}], (rp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("V,RR_ddd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"- G['e~dddD'][{s}, {r}, {p}, {q}]"

    # \Delta(B - L) = -2
    TREE_LEVEL_MATCHING_STR[
        ("V,LL_ddu", (p + 1, q + 1, r + 1, s + 1))
    ] = f"V[{p}, pp] * V[{q}, qp] * (G['qqlqHHD'][pp, qp, {r}, {s}] + G['qqlqHHD'][qp, pp, {r}, {s}]) * VEV**2 / (4*LAMBDA**2), (pp, 0, 2), (qp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("V,LL_ddd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"V[{p}, pp] * V[{q}, qp] * V[{s}, sp] * (G['qqlqHHD'][pp, qp, {r}, sp] + G['qqlqHHD'][qp, pp, {r}, sp]) * VEV**2 / (4*LAMBDA**2), (pp, 0, 2), (qp, 0, 2), (sp, 0, 2)"

    TREE_LEVEL_MATCHING_STR[
        ("V,LR_ddd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"(G['qqedHHD'][{p}, {q}, {r}, {s}] + G['qqedHHD'][{q}, {p}, {r}, {s}]) * VEV**2 / (4*LAMBDA**2)"

    TREE_LEVEL_MATCHING_STR[
        ("V,RL_udd", (p + 1, q + 1, r + 1, s + 1))
    ] = f"G['udqlHHD'][{p}, {q}, {r}, {s}] * VEV**2 / (2*LAMBDA**2)"

p, q, r, s, t, r, qp, pp, rp, sp = sym.symbols("p q r s t r qp pp rp sp")
TREE_LEVEL_MATCHING = {}
for k, v in TREE_LEVEL_MATCHING_STR.items():
    # If summation needed, execute
    if v.endswith(", 0, 2)"):
        terms = eval(f"sym.summation({v})").expand().args
        expanded_terms = []
        for term in terms:
            if isinstance(term.expand(), sym.core.add.Add):
                expanded_terms += list(term.expand().args)
            else:
                expanded_terms.append(term)

        TREE_LEVEL_MATCHING[k] = expanded_terms
    elif "] + G" in v or "] - G" in v:  # No summation but (anti)symmetrised
        terms = eval(v).expand().args
        TREE_LEVEL_MATCHING[k] = terms
    else:
        TREE_LEVEL_MATCHING[k] = (eval(v),)


MATRIX_ELEMENTS = {
    ("S,LL_udd", (1, 1, 1, 1)): ("u", "d", "L", "d", "L"),
    ("S,LL_udd", (1, 2, 1, 1)): ("u", "s", "L", "d", "L"),
    ("S,LL_udd", (1, 1, 2, 1)): ("u", "d", "L", "s", "L"),
    ("S,LL_duu", (1, 1, 1, 1)): ("d", "u", "L", "u", "L"),
    ("S,LL_duu", (2, 1, 1, 1)): ("s", "u", "L", "u", "L"),
    ("S,LR_duu", (1, 1, 1, 1)): ("d", "u", "L", "u", "R"),
    ("S,LR_duu", (2, 1, 1, 1)): ("s", "u", "L", "u", "R"),
    ("S,RL_duu", (1, 1, 1, 1)): ("d", "u", "R", "u", "L"),
    ("S,RL_duu", (2, 1, 1, 1)): ("s", "u", "R", "u", "L"),
    ("S,RL_dud", (1, 1, 1, 1)): ("d", "u", "R", "d", "L"),
    ("S,RL_dud", (2, 1, 1, 1)): ("s", "u", "R", "d", "L"),
    ("S,RL_dud", (1, 1, 2, 1)): ("d", "u", "R", "s", "L"),
    ("S,RL_ddu", (1, 2, 1, 1)): ("d", "s", "R", "u", "L"),
    ("S,RR_duu", (1, 1, 1, 1)): ("d", "u", "R", "u", "R"),
    ("S,RR_duu", (2, 1, 1, 1)): ("s", "u", "R", "u", "R"),
    ("S,LL_ddd", (1, 2, 1, 1)): ("d", "s", "L", "d", "L"),
    ("S,LR_udd", (1, 1, 1, 1)): ("u", "d", "L", "d", "R"),
    ("S,LR_udd", (1, 2, 1, 1)): ("u", "s", "L", "d", "R"),
    ("S,LR_udd", (1, 1, 1, 2)): ("u", "d", "L", "s", "R"),
    ("S,LR_ddu", (1, 2, 1, 1)): ("d", "s", "L", "u", "R"),
    ("S,LR_ddd", (1, 2, 1, 1)): ("d", "s", "L", "d", "R"),
    ("S,RL_ddd", (1, 2, 1, 1)): ("d", "s", "R", "d", "L"),
    ("S,RR_udd", (1, 1, 1, 1)): ("u", "d", "R", "d", "R"),
    ("S,RR_udd", (1, 2, 1, 1)): ("u", "s", "R", "d", "R"),
    ("S,RR_udd", (1, 1, 1, 2)): ("u", "d", "R", "s", "R"),
    ("S,RR_ddd", (1, 2, 1, 1)): ("d", "s", "R", "d", "R"),
}

CANONICAL_MATRIX_ELEMENTS = {
    ("pi+", ("u", "d", "L", "d", "L"), "p"): (
        1,
        ("pi+", ("u", "d", "L", "d", "L"), "p"),
    ),
    ("pi0", ("u", "d", "L", "d", "L"), "n"): (
        -sqrt(2),
        ("pi+", ("u", "d", "L", "d", "L"), "p"),
    ),
    ("eta0", ("u", "d", "L", "d", "L"), "n"): (
        1,
        ("eta0", ("u", "d", "L", "u", "L"), "p"),
    ),
    ("K+", ("u", "s", "L", "d", "L"), "p"): (1, ("K+", ("u", "s", "L", "d", "L"), "p")),
    ("K0", ("u", "s", "L", "d", "L"), "n"): (
        -1,
        ("K+", ("d", "s", "L", "u", "L"), "p"),
    ),
    ("K+", ("u", "d", "L", "s", "L"), "p"): (1, ("K+", ("u", "d", "L", "s", "L"), "p")),
    ("K0", ("u", "d", "L", "s", "L"), "n"): (1, ("K+", ("u", "d", "L", "s", "L"), "p")),
    ("pi0", ("d", "u", "L", "u", "L"), "p"): (
        -sqrt(2),
        ("pi+", ("u", "d", "L", "d", "L"), "p"),
    ),
    ("eta0", ("d", "u", "L", "u", "L"), "p"): (
        -1,
        ("eta0", ("u", "d", "L", "u", "L"), "p"),
    ),
    ("pi-", ("d", "u", "L", "u", "L"), "n"): (
        -1,
        ("pi+", ("u", "d", "L", "d", "L"), "p"),
    ),
    ("K0", ("s", "u", "L", "u", "L"), "p"): (
        -1,
        ("K0", ("u", "s", "L", "u", "L"), "p"),
    ),
    ("pi0", ("d", "u", "L", "u", "R"), "p"): (
        -sqrt(2),
        ("pi+", ("u", "d", "L", "d", "R"), "p"),
    ),
    ("eta0", ("d", "u", "L", "u", "R"), "p"): (
        -1,
        ("eta0", ("u", "d", "L", "u", "R"), "p"),
    ),
    ("pi-", ("d", "u", "L", "u", "R"), "n"): (
        -1,
        ("pi+", ("u", "d", "L", "d", "R"), "p"),
    ),
    ("K0", ("s", "u", "L", "u", "R"), "p"): (
        -1,
        ("K0", ("u", "s", "L", "u", "R"), "p"),
    ),
    ("pi0", ("d", "u", "R", "u", "L"), "p"): (
        -sqrt(2),
        ("pi+", ("u", "d", "L", "d", "R"), "p"),
    ),
    ("eta0", ("d", "u", "R", "u", "L"), "p"): (
        -1,
        ("eta0", ("u", "d", "L", "u", "R"), "p"),
    ),
    ("pi-", ("d", "u", "R", "u", "L"), "n"): (
        -1,
        ("pi+", ("u", "d", "L", "d", "R"), "p"),
    ),
    ("K0", ("s", "u", "R", "u", "L"), "p"): (
        -1,
        ("K0", ("u", "s", "L", "u", "R"), "p"),
    ),
    ("pi+", ("d", "u", "R", "d", "L"), "p"): (
        -1,
        ("pi+", ("u", "d", "L", "d", "R"), "p"),
    ),
    ("pi0", ("d", "u", "R", "d", "L"), "n"): (
        sqrt(2),
        ("pi+", ("u", "d", "L", "d", "R"), "p"),
    ),
    ("eta0", ("d", "u", "R", "d", "L"), "n"): (
        -1,
        ("eta0", ("u", "d", "L", "u", "R"), "p"),
    ),
    ("K+", ("s", "u", "R", "d", "L"), "p"): (
        -1,
        ("K+", ("u", "s", "L", "d", "R"), "p"),
    ),
    ("K0", ("s", "u", "R", "d", "L"), "n"): (1, ("K+", ("d", "s", "L", "u", "R"), "p")),
    ("K+", ("d", "u", "R", "s", "L"), "p"): (
        -1,
        ("K+", ("u", "d", "L", "s", "R"), "p"),
    ),
    ("K0", ("d", "u", "R", "s", "L"), "n"): (
        -1,
        ("K+", ("u", "d", "L", "s", "R"), "p"),
    ),
    ("K+", ("d", "s", "R", "u", "L"), "p"): (1, ("K+", ("d", "s", "L", "u", "R"), "p")),
    ("K0", ("d", "s", "R", "u", "L"), "n"): (
        -1,
        ("K+", ("u", "s", "L", "d", "R"), "p"),
    ),
    ("pi0", ("d", "u", "R", "u", "R"), "p"): (
        -sqrt(2),
        ("pi+", ("u", "d", "L", "d", "L"), "p"),
    ),
    ("eta0", ("d", "u", "R", "u", "R"), "p"): (
        -1,
        ("eta0", ("u", "d", "L", "u", "L"), "p"),
    ),
    ("pi-", ("d", "u", "R", "u", "R"), "n"): (
        -1,
        ("pi+", ("u", "d", "L", "d", "L"), "p"),
    ),
    ("K0", ("s", "u", "R", "u", "R"), "p"): (
        -1,
        ("K0", ("u", "s", "L", "u", "L"), "p"),
    ),
    ("K+", ("d", "s", "L", "d", "L"), "n"): (
        -1,
        ("K0", ("u", "s", "L", "u", "L"), "p"),
    ),
    ("pi+", ("u", "d", "L", "d", "R"), "p"): (
        1,
        ("pi+", ("u", "d", "L", "d", "R"), "p"),
    ),
    ("pi0", ("u", "d", "L", "d", "R"), "n"): (
        -sqrt(2),
        ("pi+", ("u", "d", "L", "d", "R"), "p"),
    ),
    ("eta0", ("u", "d", "L", "d", "R"), "n"): (
        1,
        ("eta0", ("u", "d", "L", "u", "R"), "p"),
    ),
    ("K+", ("u", "s", "L", "d", "R"), "p"): (1, ("K+", ("u", "s", "L", "d", "R"), "p")),
    ("K0", ("u", "s", "L", "d", "R"), "n"): (
        -1,
        ("K+", ("d", "s", "L", "u", "R"), "p"),
    ),
    ("K+", ("u", "d", "L", "s", "R"), "p"): (1, ("K+", ("u", "d", "L", "s", "R"), "p")),
    ("K0", ("u", "d", "L", "s", "R"), "n"): (1, ("K+", ("u", "d", "L", "s", "R"), "p")),
    ("K+", ("d", "s", "L", "u", "R"), "p"): (1, ("K+", ("d", "s", "L", "u", "R"), "p")),
    ("K0", ("d", "s", "L", "u", "R"), "n"): (
        -1,
        ("K+", ("u", "s", "L", "d", "R"), "p"),
    ),
    ("K+", ("d", "s", "L", "d", "R"), "n"): (
        -1,
        ("K0", ("u", "s", "L", "u", "R"), "p"),
    ),
    ("K+", ("d", "s", "R", "d", "L"), "n"): (
        -1,
        ("K0", ("u", "s", "L", "u", "R"), "p"),
    ),
    ("pi+", ("u", "d", "R", "d", "R"), "p"): (
        1,
        ("pi+", ("u", "d", "L", "d", "L"), "p"),
    ),
    ("pi0", ("u", "d", "R", "d", "R"), "n"): (
        -sqrt(2),
        ("pi+", ("u", "d", "L", "d", "L"), "p"),
    ),
    ("eta0", ("u", "d", "R", "d", "R"), "n"): (
        1,
        ("eta0", ("u", "d", "L", "u", "L"), "p"),
    ),
    ("K+", ("u", "s", "R", "d", "R"), "p"): (1, ("K+", ("u", "s", "L", "d", "L"), "p")),
    ("K0", ("u", "s", "R", "d", "R"), "n"): (
        -1,
        ("K+", ("d", "s", "L", "u", "L"), "p"),
    ),
    ("K+", ("u", "d", "R", "s", "R"), "p"): (1, ("K+", ("u", "d", "L", "s", "L"), "p")),
    ("K0", ("u", "d", "R", "s", "R"), "n"): (1, ("K+", ("u", "d", "L", "s", "L"), "p")),
    ("K+", ("d", "s", "R", "d", "R"), "n"): (
        -1,
        ("K0", ("u", "s", "L", "u", "L"), "p"),
    ),
}

LATTICE_VALUES = {
    ("pi+", ("u", "d", "L", "d", "L"), "p"): 0.151,
    ("pi+", ("u", "d", "L", "d", "R"), "p"): -0.159,
    ("K0", ("u", "s", "L", "u", "L"), "p"): 0.043,
    ("K0", ("u", "s", "L", "u", "R"), "p"): 0.0854,
    ("K+", ("u", "s", "L", "d", "L"), "p"): 0.0284,
    ("K+", ("u", "s", "L", "d", "R"), "p"): -0.0398,
    ("K+", ("u", "d", "L", "s", "L"), "p"): 0.1006,
    ("K+", ("u", "d", "L", "s", "R"), "p"): -0.109,
    ("K+", ("d", "s", "L", "u", "L"), "p"): -0.0717,
    ("K+", ("d", "s", "L", "u", "R"), "p"): -0.0443,
    ("eta0", ("u", "d", "L", "u", "R"), "p"): 0.006,
    ("eta0", ("u", "d", "L", "u", "L"), "p"): 0.113,
}
