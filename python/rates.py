#!/usr/bin/env python3

"""All units are in GeV. Rates calculated using the indirect BchPT method for comparison."""

from math import pi
from collections import defaultdict
from typing import Mapping
from sympy import Abs

D = 0.8
F = 0.5

## B-L=0 expressions
def gamma_BL0_nepi(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.694522 * ((1. + D + F))**(2) * (lam)**(-4) * ((Abs((0.01 * coeffs[('S,LL_duu', '1111')] + 0.01 * coeffs[('S,RL_duu', '1111')])))**(2) + (Abs((0.01 * coeffs[('S,LR_duu', '1111')] + 0.01 * coeffs[('S,RR_duu', '1111')])))**(2))

def gamma_BL0_peeta(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return (lam)**(-4) * (0.31753 * (Abs(((0.01 + -0.00333333 * D + 0.01 * F) * coeffs[('S,LL_duu', '1111')] + (-0.00333333 + -0.00333333 * D + 0.01 * F) * coeffs[('S,RL_duu', '1111')])))**(2) + 0.31753 * (Abs(((-0.00333333 + -0.00333333 * D + 0.01 * F) * coeffs[('S,LR_duu', '1111')] + (0.01 + -0.00333333 * D + 0.01 * F) * coeffs[('S,RR_duu', '1111')])))**(2))

def gamma_BL0_pepi(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.231507 * ((1. + D + F))**(2) * (lam)**(-4) * ((Abs((0.01 * coeffs[('S,LL_duu', '1111')] + 0.01 * coeffs[('S,RL_duu', '1111')])))**(2) + (Abs((0.01 * coeffs[('S,LR_duu', '1111')] + 0.01 * coeffs[('S,RR_duu', '1111')])))**(2))

def gamma_BL0_nnueta(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.31753 * (lam)**(-4) * (Abs(((-0.00333333 + -0.00333333 * D + 0.01 * F) * coeffs[('S,RL_dud', '1111')] + (0.01 + -0.00333333 * D + 0.01 * F) * coeffs[('S,LL_udd', '1111')])))**(2)

def gamma_BL0_nnupi(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.231507 * ((1. + D + F))**(2) * (lam)**(-4) * (Abs((0.01 * coeffs[('S,RL_dud', '1111')] + 0.01 * coeffs[('S,LL_udd', '1111')])))**(2)

def gamma_BL0_pnupi(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.463015 * ((1. + D + F))**(2) * (lam)**(-4) * (Abs((0.01 * coeffs[('S,RL_dud', '1111')] + 0.01 * coeffs[('S,LL_udd', '1111')])))**(2)

def gamma_BL0_peK(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return (lam)**(-4) * (0.254328 * (Abs(((0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs[('S,LL_duu', '2111')] + (-0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs[('S,RL_duu', '2111')])))**(2) + 0.254328 * (Abs(((-0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs[('S,LR_duu', '2111')] + (0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs[('S,RR_duu', '2111')])))**(2))

def gamma_BL0_nnuK(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.254328 * (lam)**(-4) * (Abs(((0.01 + 0.00254329 * D + 0.00762987 * F) * coeffs[('S,RL_dud', '1121')] + (-0.01 + -0.00267131 * D + 0.00775789 * F) * coeffs[('S,RL_dud', '2111')] + 0.01 * coeffs[('S,LL_udd', '1121')] + 0.00254329 * D * coeffs[('S,LL_udd', '1121')] + 0.00762987 * F * coeffs[('S,LL_udd', '1121')] + 0.01 * coeffs[('S,LL_udd', '1211')] + -0.00267131 * D * coeffs[('S,LL_udd', '1211')] + 0.00775789 * F * coeffs[('S,LL_udd', '1211')])))**(2)

def gamma_BL0_pnuK(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.254328 * (lam)**(-4) * (Abs(((0.01 + 0.00254329 * D + 0.00762987 * F) * coeffs[('S,RL_dud', '1121')] + (0.0052146 * D + -0.000128018 * F) * coeffs[('S,RL_dud', '2111')] + 0.01 * coeffs[('S,LL_udd', '1121')] + 0.00254329 * D * coeffs[('S,LL_udd', '1121')] + 0.00762987 * F * coeffs[('S,LL_udd', '1121')] + 0.0052146 * D * coeffs[('S,LL_udd', '1211')] + -0.000128018 * F * coeffs[('S,LL_udd', '1211')])))**(2)

## B-L=2 expressions
def gamma_BL2_nnueta(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.31753 * (lam)**(-4) * (Abs(((-0.00333333 + -0.00333333 * D + 0.01 * F) * coeffs[('S,LR_udd', '1111')] + (0.01 + -0.00333333 * D + 0.01 * F) * coeffs[('S,RR_udd', '1111')])))**(2)

def gamma_BL2_nnupi(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.231507 * ((1. + D + F))**(2) * (lam)**(-4) * (Abs((0.01 * coeffs[('S,LR_udd', '1111')] + 0.01 * coeffs[('S,RR_udd', '1111')])))**(2)

def gamma_BL2_pnupi(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.463015 * ((1. + D + F))**(2) * (lam)**(-4) * (Abs((0.01 * coeffs[('S,LR_udd', '1111')] + 0.01 * coeffs[('S,RR_udd', '1111')])))**(2)

def gamma_BL2_nnuK(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.254328 * (lam)**(-4) * (Abs(((-0.01 + -0.00267131 * D + 0.00775789 * F) * coeffs[('S,LR_udd', '1112')] + (0.01 + 0.00254329 * D + 0.00762987 * F) * coeffs[('S,LR_udd', '1211')] + 0.01 * coeffs[('S,RR_udd', '1112')] + -0.00267131 * D * coeffs[('S,RR_udd', '1112')] + 0.00775789 * F * coeffs[('S,RR_udd', '1112')] + 0.01 * coeffs[('S,RR_udd', '1211')] + 0.00254329 * D * coeffs[('S,RR_udd', '1211')] + 0.00762987 * F * coeffs[('S,RR_udd', '1211')])))**(2)

def gamma_BL2_pnuK(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return 0.254328 * (lam)**(-4) * (Abs(((0.0052146 * D + -0.000128018 * F) * coeffs[('S,LR_udd', '1112')] + (0.01 + 0.00254329 * D + 0.00762987 * F) * coeffs[('S,LR_udd', '1211')] + 0.0052146 * D * coeffs[('S,RR_udd', '1112')] + -0.000128018 * F * coeffs[('S,RR_udd', '1112')] + 0.01 * coeffs[('S,RR_udd', '1211')] + 0.00254329 * D * coeffs[('S,RR_udd', '1211')] + 0.00762987 * F * coeffs[('S,RR_udd', '1211')])))**(2)

def gamma_BL2_neK(coeffs: Mapping[tuple[str, str], float], lam: float) -> float:
    return (0.254328 * (lam)**(-4) * (Abs((0.01 + -0.00788591 * D + 0.00788591 * F) * coeffs[('S,RL_ddd', '1211')]))**(2) + 0.254328 * (lam)**(-4) * (Abs(((-0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs[('S,LR_ddd', '1211')] + (0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs[('S,RR_ddd', '1211')])))**(2))
