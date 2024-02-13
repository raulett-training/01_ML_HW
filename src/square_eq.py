# coding=utf-8
"""
TODO docstring
"""

import numpy as np

import re

from src.InputValueError import InputValueError


def square_eq(eq_string: str) -> tuple:
    """
    Write a function that takes a quadratic equation with integer coofitient as input (in one line) and returns its roots,
    or reports that there are none.
    examples:
    x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7
    The input is a string of the form:
    x**2- 11*x + 28 = 0
    x**2 -11x + 28 = 0
    -11x + 28 = 0
    x**2 + 28 = 0
    x**2 -11x = 0
    x**2 -11x = 124
    The output is a pair of real or complex roots.
    """
    sq_eq_pattern = r"^([-|+]?\s?\d*x\**2)?\s?([-|+]\s?[\d]*\*?x)?\s?([-|+]\s?\d*)?\s?=\s([-|+]?\d+)$"
    """
    pattern matches to examples:
    x**2- 11*x + 28 = 0
    x**2 -11x + 28 = 0
    -11x + 28 = 0
    x**2 + 28 = 0
    x**2 -11x = 0
    x**2 -11x = 124
    """
    if re.match(sq_eq_pattern, eq_string):
        coeff = np.zeros(4)
        for i, eq_member in enumerate(re.findall(sq_eq_pattern, eq_string)[0]):
            if eq_member:
                parsed_coeff = re.search(r'([-|+]?\s?\d*)', eq_member)[0]
                if not parsed_coeff:
                    coeff[i] = 1
                else:
                    coeff[i] = int(''.join(re.search(r'([-|+]?\s?\d*)', eq_member)[0].split()))
            else:
                coeff[i] = 0
        if coeff[3] != 0:
            coeff[2] -= coeff[3]
        return np.roots(coeff[:3])
    else:
        raise InputValueError

