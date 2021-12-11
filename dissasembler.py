"""
dissasembler.py
---------------
Module containing functions for disassembling RISC-V instructions.

Author: Oscar Jaimes
Last Updated: 11-12-2021
"""


from io import BufferedReader
from tables import op_codes
from tables import regs


def disassemble(fstream: BufferedReader):
    instructions = []
    cur_i = fstream.read(4)  # 4 bytes @ a time bois
    while cur_i:
        i_dis = disassemble_instruction(cur_i)
        instructions.append(i_dis)
        cur_i = fstream.read(4)
    return instructions


def disassemble_instruction(instruction: bytes):
    return instruction


def get_opcode(instruction: bytes):
    m = 0b1111111
    return m & i


def get_type(instruction):
    pass
