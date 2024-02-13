# coding=utf-8
"""
TODO дописать readme
"""
import re

import numpy as np
import pytest

from src.caeser_code import encrypt_caesar, decrypt_caesar
from src.split_int_num import split_int_num
from src.square_eq import square_eq
from src.switch_camel_snake import switch_camel_snake
from src.InputValueError import InputValueError


def test_task_1_split_number():
    """
    Function to test the split_int_num function with various input values.
    """
    assert split_int_num(1234441) == '1 234 441'
    assert split_int_num(645748611) == '645 748 611'
    assert split_int_num(0) == '0'
    assert split_int_num(1) == '1'


def test_task_2_camel_snake():
    """
    Function to test the switch_camel_snake function with various input cases.
    """
    assert switch_camel_snake('my_first_func') == 'MyFirstFunc'
    assert switch_camel_snake('MyFirstFunc') == 'my_first_func'
    assert switch_camel_snake('MTestF') == 'm_test_f'
    assert switch_camel_snake('m_test_f') == 'MTestF'
    assert switch_camel_snake('m') == 'M'
    assert switch_camel_snake('M') == 'm'
    with pytest.raises(InputValueError):
        assert switch_camel_snake('') == ''
    with pytest.raises(InputValueError):
        assert switch_camel_snake('_st_s') == '_st_s'
    with pytest.raises(InputValueError):
        assert switch_camel_snake('') == ''


def test_task_3_quadr_eq():
    """
    Function to test the square_eq function with various input cases.
    """
    assert np.array_equal(square_eq("x**2 - 11*x + 28 = 0"), np.roots([1, -11, 28])) is True
    assert np.array_equal(square_eq("x**2- 11*x + 28 = 0"), np.roots([1, -11, 28])) is True
    assert np.array_equal(square_eq("x**2 -11x + 28 = 0"), np.roots([1, -11, 28])) is True
    assert np.array_equal(square_eq("-11x + 28 = 0"), np.roots([0, -11, 28])) is True
    assert np.array_equal(square_eq("x**2 + 28 = 0"), np.roots([1, 0, 28])) is True
    assert np.array_equal(square_eq("x**2 -11x = 0"), np.roots([1, -11, 0])) is True
    assert np.array_equal(square_eq("x**2 -11x = 124"), np.roots([1, -11, -124])) is True
    assert np.array_equal(square_eq("213x**2 -124 = 0"), np.roots([213, 0, -124])) is True


def test_task_4_test_task_5_caesar_encrypt():
    """
    Test for caesar encrypt function.
    :return:
    """
    test_set = ["Hello, World!", "somestring", "zuzu", "Test string for Caesar cipher"]
    result_set = ['khoorzruog', "vrphvwulqj", "cxcx", "whvwvwulqjirufdhvduflskhu"]
    for source, res in zip(test_set, result_set):
        assert encrypt_caesar(re.sub(r'[^\w]', "", source.lower()), 3) == res


def test_task_5_caesar_decrypt():
    """
    Test for caesar encrypt function.
    :return:
    """
    result_set = ["Hello, World!", "somestring", "zuzu", "Test string for Caesar cipher"]
    test_set = ['khoorzruog', "vrphvwulqj", "cxcx", "whvwvwulqjirufdhvduflskhu"]
    for source, res in zip(test_set, result_set):
        assert decrypt_caesar(source, 3) == re.sub(r'[^\w]', "", res.lower())
