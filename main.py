# coding=utf-8
"""
docstring
"""

from split_int_num import split_int_num


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
    pass


if __name__ == '__main__':
    print(split_int_num(1234441))
    print(split_int_num(645748611))
    print(split_int_num(0))
