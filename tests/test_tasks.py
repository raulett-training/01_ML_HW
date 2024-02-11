# coding=utf-8
"""
TODO docstring
"""
import pytest

from InputValueError import InputValueError
from split_int_num import split_int_num
from switch_camel_snake import switch_camel_snake


def test_task_1():
    """
    Function to test the split_int_num function with various input values.
    """
    assert split_int_num(1234441) == '1 234 441'
    assert split_int_num(645748611) == '645 748 611'
    assert split_int_num(0) == '0'
    assert split_int_num(1) == '1'


def test_task_2():
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
