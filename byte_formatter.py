"""
byte_formatter.py
-----------------
Module containing functions for performing various operations on array of bytes.

Author: Oscar Jaimes
Last Updated: 11/12/2021
"""


def int_from_bytes(b: bytes) -> int:
    i = int.from_bytes(b, byteorder="big")
    return i


def reverse_bytes(b: bytes) -> bytes:
    return b[::-1]
