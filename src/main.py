# coding=utf-8
"""
docstring
"""
import re

from split_int_num import split_int_num
from src.caeser_code import encrypt_caesar, decrypt_caesar
from src.square_eq import square_eq
from switch_camel_snake import switch_camel_snake

from src.InputValueError import InputValueError

if __name__ == '__main__':
    # print('________________________')
    # print('task 1')
    # numbers = [1234441, 645748611, 0, 1]
    # for num in numbers:
    #     print(f'Входное число: {num}')
    #     print(f'Результат: {split_int_num(num)}')
    # print('________________________')
    #
    # print('________________________')
    # print('task 2')
    # names = ['my_first_func', 'MyFirstFunc', '00йцу', '_st_s', '']
    # for name in names:
    #     print(f'Входное имя: {name}')
    #     try:
    #         print(f'Результат: {switch_camel_snake(name)}')
    #     except InputValueError:
    #         print(f'Некорректное имя: {name}, имя не соответствует требованиям к входным данным.')
    # print('________________________')
    #
    # print('________________________')
    # print('task 3')
    # eqs = ["x**2- 11*x + 28 = 0",
    #        "x**2 -11x + 28 = 0",
    #        "-11x + 28 = 0",
    #        "x**2 + 28 = 0",
    #        "x**2 -11x = 0",
    #        "x**2 -11x = 124",
    #        "213x**2 -124 = 0"]
    # for eq in eqs:
    #     print(f"Входное уравнение: '{eq}' \nРезультат: {square_eq(eq)} \n")
    # print('________________________')
    #
    # print('________________________')
    print('task 4')
    print("Перед преобразованием из строки удаляются пробелы и знаки препинания, "
          "для увеличения стойкости шифротекста")
    encrypt_strings = ["Hello, World!", "somestring", "zuzu"]
    key = 3
    for enc_string in encrypt_strings:
        print(f'Входная строка: "{enc_string}"')
        transformed_input = re.sub(r'[^\w]', "", enc_string.lower())
        print(f'Преобразованная для шифрования строка: "{transformed_input}"')
        encript_sting = encrypt_caesar(transformed_input, key)
        print(f'Результат шифрования: "{encript_sting}"')
        print(f'Результат дешифрования: "{decrypt_caesar(encript_sting, key)}"')
    print('________________________')
