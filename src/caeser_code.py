# coding=utf-8
"""
docstring
"""
import re


def encrypt_caesar(input_str: str, key: int) -> str:
    """
    Function to encript caeser code
    :param key: значение ключа шифрования простой замены. Ключ в функции decript и encrypt должен быть одинаковым
    :param input_str: Входная строка. Принимается только строк из букв. другие символы недопустимы
    :return: str
    """
    return ''.join([chr((ord(letter) - ord('a') + key) % (ord('z') - ord('a') + 1) + ord('a')) for letter in input_str])


def decrypt_caesar(input_str: str, key: int) -> str:
    """
    Function to decrypt caeser code
    :param key: значение ключа шифрования простой замены. Ключ в функции decript и encrypt должен быть одинаковым
    :param input_str: str
    :return: str
    """
    return ''.join([chr((ord(letter) - ord('a') - key) % (ord('z') - ord('a') + 1) + ord('a')) for letter in input_str])
