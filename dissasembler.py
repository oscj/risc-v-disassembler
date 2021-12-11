"""
dissasembler.py
---------------
Module containing functions for disassembling RISC-V instructions.

Author: Oscar Jaimes
Last Updated: 11-12-2021
"""


import byte_formatter as bf
from io import BufferedReader
from bw_byte_ops import *

# lookup tables
from tables import i_formats
from tables import i_type_by_oc
from tables import i_by_codes
from tables import regs


def disassemble(buff_reader: BufferedReader):
    instructions = []
    cur_i = buff_reader.read(4)
    while cur_i:
        cur_i = bf.reverse_bytes(cur_i)  # reverse bytes for endianness
        i_dis = disassemble_instruction(cur_i)
        instructions.append(i_dis)
        cur_i = buff_reader.read(4)
        
    return instructions


def disassemble_instruction(instruction: bytes) -> str:
    oc = get_opcode(instruction)
    i_type = i_type_by_oc[oc]
    i_format = i_formats[i_type]
    i = get_instruction(instruction, oc, i_format, i_type)
    return i


def get_instruction(
    instruction: bytes, opcode: int, i_format: dict, i_type: str
) -> str:
    i = ""
    init = i_by_codes[opcode]

    if type(init) == str:
        i = init
        return i

    funct3 = get_funct3(instruction)
    second = init[funct3]

    if type(second) == str:
        i = second
        return i

    if "funct7" in i_format:
        funct7 = get_r_type_funct7(instruction)
        third = second[funct7]
        return third
    else:
        imm = get_i_type_imm(instruction)
        third = second[imm]
        return third


def get_i_type_imm(instruction: bytes) -> int:
    m = bytes([]).fromhex("FFF00000")  # mask for funct7 into bytes
    imm = bitwise_and_bytes(instruction, m)
    return bf.int_from_bytes(imm) >> 20


def get_r_type_funct7(instruction: bytes) -> int:
    m = bytes([]).fromhex("FE000000")  # mask for funct7 into bytes
    f7 = bitwise_and_bytes(instruction, m)
    return bf.int_from_bytes(f7) >> 25


def get_funct3(instruction: bytes) -> int:
    m = bytes([]).fromhex("00007000")  # mask for funct3 into bytes
    f3 = bitwise_and_bytes(instruction, m)
    return bf.int_from_bytes(f3) >> 12  # don't forget shift


def get_opcode(instruction: bytes) -> int:
    m = bytes([]).fromhex("0000007F")  # mask for opcode into bytes
    oc_bytes = bitwise_and_bytes(instruction, m)
    return bf.int_from_bytes(oc_bytes)


def translate_register(reg: int) -> str:
    return regs[reg]
