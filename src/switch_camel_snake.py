# coding=utf-8
import re

from src.InputValueError import InputValueError


def switch_camel_snake(input_name: str) -> str:
    """
    задание 2.
    Implement a function that replaces, takes a string of text and changes Snake_Case to CamelCase and vice versa.
    Examples:
    my_first_func -> MyFirstFunc,
    AnotherFunction -> another_function

    :param input_name: accepts the name in snake_case or CamelCase. If the line is not in one style or another,
    throws an "InputValueError" exception
    :return: Returns the name translated into CamelCase or snake_case respectively
    """
    snake_case_pattern = r'^[a-z0-9]+(_[a-z0-9]+)*$'
    camel_case_pattern = r'^([A-Z]{1}[a-z0-9]*)+$'

    if re.match(snake_case_pattern, input_name):
        return ''.join(map(lambda x: x.capitalize(), input_name.split('_')))
    elif re.match(camel_case_pattern, input_name):
        return '_'.join(map(lambda x: x.lower(), re.findall(r'[A-Z]{1}[a-z0-9]*', input_name)))
    else:
        raise InputValueError

