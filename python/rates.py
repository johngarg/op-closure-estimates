#!/usr/bin/env python3

"""All units are in GeV. Rates calculated using the indirect BchPT method for comparison."""

from math import pi, fabs
from collections import defaultdict
from typing import Mapping

D = 0.8
F = 0.5

## B-L=0 expressions
def gamma_BL0_nepi(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.694522 * ((1. + D + F))**(2) * (lam)**(-4) * ((fabs((0.01 * coeffs['_duu^S,LL_1111'] + 0.01 * coeffs['_duu^S,RL_1111'])))**(2) + (fabs((0.01 * coeffs['_duu^S,LR_1111'] + 0.01 * coeffs['_duu^S,RR_1111'])))**(2))

def gamma_BL0_peeta(coeffs: Mapping[str, float], lam: float) -> float:
    return (lam)**(-4) * (0.31753 * (fabs(((0.01 + -0.00333333 * D + 0.01 * F) * coeffs['_duu^S,LL_1111'] + (-0.00333333 + -0.00333333 * D + 0.01 * F) * coeffs['_duu^S,RL_1111'])))**(2) + 0.31753 * (fabs(((-0.00333333 + -0.00333333 * D + 0.01 * F) * coeffs['_duu^S,LR_1111'] + (0.01 + -0.00333333 * D + 0.01 * F) * coeffs['_duu^S,RR_1111'])))**(2))

def gamma_BL0_pepi(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.231507 * ((1. + D + F))**(2) * (lam)**(-4) * ((fabs((0.01 * coeffs['_duu^S,LL_1111'] + 0.01 * coeffs['_duu^S,RL_1111'])))**(2) + (fabs((0.01 * coeffs['_duu^S,LR_1111'] + 0.01 * coeffs['_duu^S,RR_1111'])))**(2))

def gamma_BL0_nnueta(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.31753 * (lam)**(-4) * (fabs(((-0.00333333 + -0.00333333 * D + 0.01 * F) * coeffs['_dud^S,RL_1111'] + (0.01 + -0.00333333 * D + 0.01 * F) * coeffs['_udd^S,LL_1111'])))**(2)

def gamma_BL0_nnupi(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.231507 * ((1. + D + F))**(2) * (lam)**(-4) * (fabs((0.01 * coeffs['_dud^S,RL_1111'] + 0.01 * coeffs['_udd^S,LL_1111'])))**(2)

def gamma_BL0_pnupi(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.463015 * ((1. + D + F))**(2) * (lam)**(-4) * (fabs((0.01 * coeffs['_dud^S,RL_1111'] + 0.01 * coeffs['_udd^S,LL_1111'])))**(2)

def gamma_BL0_peK(coeffs: Mapping[str, float], lam: float) -> float:
    return (lam)**(-4) * (0.254328 * (fabs(((0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs['_duu^S,LL_2111'] + (-0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs['_duu^S,RL_2111'])))**(2) + 0.254328 * (fabs(((-0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs['_duu^S,LR_2111'] + (0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs['_duu^S,RR_2111'])))**(2))

def gamma_BL0_nnuK(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.254328 * (lam)**(-4) * (fabs(((0.01 + 0.00254329 * D + 0.00762987 * F) * coeffs['_dud^S,RL_1121'] + (-0.01 + -0.00267131 * D + 0.00775789 * F) * coeffs['_dud^S,RL_2111'] + 0.01 * coeffs['_udd^S,LL_1121'] + 0.00254329 * D * coeffs['_udd^S,LL_1121'] + 0.00762987 * F * coeffs['_udd^S,LL_1121'] + 0.01 * coeffs['_udd^S,LL_1211'] + -0.00267131 * D * coeffs['_udd^S,LL_1211'] + 0.00775789 * F * coeffs['_udd^S,LL_1211'])))**(2)

def gamma_BL0_pnuK(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.254328 * (lam)**(-4) * (fabs(((0.01 + 0.00254329 * D + 0.00762987 * F) * coeffs['_dud^S,RL_1121'] + (0.0052146 * D + -0.000128018 * F) * coeffs['_dud^S,RL_2111'] + 0.01 * coeffs['_udd^S,LL_1121'] + 0.00254329 * D * coeffs['_udd^S,LL_1121'] + 0.00762987 * F * coeffs['_udd^S,LL_1121'] + 0.0052146 * D * coeffs['_udd^S,LL_1211'] + -0.000128018 * F * coeffs['_udd^S,LL_1211'])))**(2)

## B-L=2 expressions
def gamma_BL2_nnueta(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.31753 * (lam)**(-4) * (fabs(((-0.00333333 + -0.00333333 * D + 0.01 * F) * coeffs['_udd^S,LR_1111'] + (0.01 + -0.00333333 * D + 0.01 * F) * coeffs['_udd^S,RR_1111'])))**(2)

def gamma_BL2_nnupi(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.231507 * ((1. + D + F))**(2) * (lam)**(-4) * (fabs((0.01 * coeffs['_udd^S,LR_1111'] + 0.01 * coeffs['_udd^S,RR_1111'])))**(2)

def gamma_BL2_pnupi(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.463015 * ((1. + D + F))**(2) * (lam)**(-4) * (fabs((0.01 * coeffs['_udd^S,LR_1111'] + 0.01 * coeffs['_udd^S,RR_1111'])))**(2)

def gamma_BL2_nnuK(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.254328 * (lam)**(-4) * (fabs(((-0.01 + -0.00267131 * D + 0.00775789 * F) * coeffs['_udd^S,LR_1112'] + (0.01 + 0.00254329 * D + 0.00762987 * F) * coeffs['_udd^S,LR_1211'] + 0.01 * coeffs['_udd^S,RR_1112'] + -0.00267131 * D * coeffs['_udd^S,RR_1112'] + 0.00775789 * F * coeffs['_udd^S,RR_1112'] + 0.01 * coeffs['_udd^S,RR_1211'] + 0.00254329 * D * coeffs['_udd^S,RR_1211'] + 0.00762987 * F * coeffs['_udd^S,RR_1211'])))**(2)

def gamma_BL2_pnuK(coeffs: Mapping[str, float], lam: float) -> float:
    return 0.254328 * (lam)**(-4) * (fabs(((0.0052146 * D + -0.000128018 * F) * coeffs['_udd^S,LR_1112'] + (0.01 + 0.00254329 * D + 0.00762987 * F) * coeffs['_udd^S,LR_1211'] + 0.0052146 * D * coeffs['_udd^S,RR_1112'] + -0.000128018 * F * coeffs['_udd^S,RR_1112'] + 0.01 * coeffs['_udd^S,RR_1211'] + 0.00254329 * D * coeffs['_udd^S,RR_1211'] + 0.00762987 * F * coeffs['_udd^S,RR_1211'])))**(2)

def gamma_BL2_neK(coeffs: Mapping[str, float], lam: float) -> float:
    return (0.254328 * (lam)**(-4) * (fabs((0.01 + -0.00788591 * D + 0.00788591 * F) * coeffs['_ddd,S^RL_1211']))**(2) + 0.254328 * (lam)**(-4) * (fabs(((-0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs['_ddd,S^LR_1211'] + (0.01 + 0.00788591 * D + -0.00788591 * F) * coeffs['_ddd^S,RR_1211'])))**(2))
