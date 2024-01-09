#!/usr/bin/env python3

from matchingtools.core import (
    TensorBuilder,
    FieldBuilder,
    Op,
    OpSum,
    D,
    number_op,
    tensor_op,
    flavor_tensor_op,
    boson,
    fermion,
    kdelta,
    sigma4,
    sigma4bar,
)

from matchingtools.extras.Lorentz import rules_Lorentz, epsDown, epsDownDot, epsUp, epsUpDot
from matchingtools.integration import ComplexScalar, integrate, VectorLikeFermion, MajoranaFermion
from matchingtools.transformations import apply_rule, apply_rules, simplify
from matchingtools.output import Writer

from matchingtools.extras.SM import (
    phi,
    phic,
    lL,
    lLc,
    qL,
    qLc,
    eR,
    eRc,
    dR,
    dRc,
    uR,
    uRc,
)

from matchingtools.extras.SU2 import epsSU2, rules_SU2, sigmaSU2
from matchingtools.extras.SU3 import epsSU3, rules_SU3

from string import ascii_lowercase

# can be created on the fly
x = TensorBuilder("x")
xc = TensorBuilder("xc")
y = TensorBuilder("y")
yc = TensorBuilder("yc")
z = TensorBuilder("z")
zc = TensorBuilder("zc")
w = TensorBuilder("w")
wc = TensorBuilder("wc")

yp = TensorBuilder("yp")
ypc = TensorBuilder("ypc")
lam = TensorBuilder("lam")


omega2 = FieldBuilder("omega2", 1, boson)
omega2c = FieldBuilder("omega2c", 1, boson)

UL = FieldBuilder("UL", 1.5, fermion)
ULc = FieldBuilder("ULc", 1.5, fermion)
UR = FieldBuilder("UR", 1.5, fermion)
URc = FieldBuilder("URc", 1.5, fermion)

NL = FieldBuilder("NL", 1.5, fermion)
NLc = FieldBuilder("NLc", 1.5, fermion)

heavy_omega2 = ComplexScalar("omega2", "omega2c", 1, has_flavor=False)
heavy_U = VectorLikeFermion("U", "UL", "UR", "ULc", "URc", 3, has_flavor=False)
heavy_N = MajoranaFermion("NL", "NLc", 2, has_flavor=False)

heavy_fields = [heavy_omega2, heavy_U, heavy_N]

# Add extra terms for symmetry by hand
interaction_lagrangian = -OpSum(
    # Yukawas
    Op(xc(40, 41), dR(0, 30, 40), dR(1, 31, 41), omega2(32), epsSU3(30, 31, 32), epsDownDot(0, 1)),
    Op(x(40, 41), dRc(0, 30, 40), dRc(1, 31, 41), omega2c(32), epsSU3(30, 31, 32), epsDown(0, 1)),
    #
    Op(y(50), URc(0, 30, 40), phi(21), qL(0, 30, 22, 50), epsSU2(21, 20), sigmaSU2(40, 20, 22)),
    Op(yc(50), UR(0, 30, 40), phic(21), qLc(0, 30, 22, 50), epsSU2(21, 20), sigmaSU2(40, 20, 22)),
    #
    Op(z(50), phi(21), NL(0, 40), lL(1, 22, 50), epsSU2(21, 20), sigmaSU2(40, 20, 22), epsUp(0, 1)),
    Op(zc(50), phic(21), NLc(0, 40), lLc(1, 22, 50), epsSU2(21, 20), sigmaSU2(40, 20, 22), epsUpDot(0, 1)),
    #
    Op(w(), NL(0, 40), UL(1, 30, 40), omega2c(30), epsUp(0, 1)),
    Op(wc(), NLc(0, 40), ULc(1, 30, 40), omega2(30), epsUpDot(0, 1)),
    #
    Op(yp(), URc(0, 30, 40), NL(0, 40), omega2(30)),
    Op(ypc(), UR(0, 30, 40), NLc(0, 40), omega2c(30)),
    #
    Op(lam(), omega2c(30), omega2(30), phic(20), phi(20))
)

max_dim = 10
effective_lagrangian = integrate(heavy_fields, interaction_lagrangian, max_dim)

OlqddHH = flavor_tensor_op("OlqddHH")

def_rule = [
    (
        Op(
            lL(747,1308,-1), qL(1310,1339,1121,-2), dR(1350,1380,-3), dR(1351,1381,-4), phi(1413), phi(1465),
            epsSU3(1380,1381,1339),
            epsDownDot(1350,1351),
            epsUp(747,1310),
            epsSU2(1413,1121),
            epsSU2(1465,1308),
        ),
        OpSum(OlqddHH(-1, -2, -3, -4)),
    ),
    (
        Op(
            lL(747,1308,-1), qL(1310,1339,1121,-2), dR(1350,1380,-3), dR(1351,1381,-4), phi(1413), phi(1465),
            epsSU3(1380,1381,1339),
            epsDownDot(1350,1351),
            epsUp(1310,747),
            epsSU2(1413,1121),
            epsSU2(1465,1308),
        ),
        OpSum(number_op(-1) * OlqddHH(-1, -2, -3, -4)),
    )
]

extra_SU2_identities = [
    (Op(phi(0), epsSU2(0, 1), phi(1)),
     OpSum()),
    (Op(phic(0), epsSU2(0, 1), phic(1)),
     OpSum()),
    (Op(sigmaSU2(0, -1, 1), sigmaSU2(0, 1, -2)),
     OpSum(number_op(3) * Op(kdelta(-1, -2)))),
    (Op(sigmaSU2(0, -1, -2), sigmaSU2(0, -3, -4)),
     OpSum(number_op(2) * Op(kdelta(-1, -4), kdelta(-3, -2)),
           -Op(kdelta(-1, -2), kdelta(-3, -4)))),
]

extra_Lorentz_identities = [
    (Op(sigma4(0,-1,-2), sigma4(0,-3,-4)),
     OpSum(number_op(2) * Op(epsDown(-1, -3), epsDownDot(-2, -4)))
     ),
    (Op(epsDown(0,-1), epsUp(0,-2)),
     OpSum(Op(kdelta(-1, -2)))
     ),
    # (Op(epsUp(-1,-2)),
    #  OpSum(number_op(-1) * Op(epsUp(-2, -1)))
    #  ),
    (Op(epsDownDot(0,-1), epsUpDot(0,-2)),
     OpSum(Op(kdelta(-1, -2)))
     ),
    (Op(epsDownDot(-1,0), epsUpDot(0,-2)),
     OpSum(number_op(-1) * Op(kdelta(-1, -2)))
     ),
    (Op(epsDown(-1,0), epsUp(0,-2)),
     OpSum(number_op(-1) * Op(kdelta(-1, -2)))
     ),
]

rules = rules_SU3 + extra_SU2_identities + extra_Lorentz_identities + def_rule
max_iterations = 2
transf_eff_lag = apply_rules(effective_lagrangian, rules, max_iterations)


lag_writer = Writer(transf_eff_lag, op_names=["OlqddHH"])
lag_writer.write_text_file("/Users/johngargalionis/Desktop/eff_lag.txt")
