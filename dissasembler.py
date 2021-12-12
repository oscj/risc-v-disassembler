"""
dissasembler.py
---------------
Module containing functions for disassembling RISC-V instructions.

Author: Oscar Jaimes
"""

from io import BufferedReader
from extractors import *
from tables import i_formats
from tables import i_type_by_oc


def disassemble(buff_reader: BufferedReader):
    instructions = []
    cur_i = buff_reader.read(4)
    while cur_i:
        cur_i = cur_i[::-1]  # reverse bytes for endianness
        i_dis = disassemble_instruction(cur_i)
        instructions.append(i_dis)
        cur_i = buff_reader.read(4)

    return instructions


def disassemble_instruction(instruction: bytes) -> str:
    oc = get_opcode(instruction)
    i_type = i_type_by_oc[oc]
    i_format = i_formats[i_type]
    i = get_instruction(instruction, oc, i_format, i_type)

    if i_type == "I":
        rs1 = get_rs1(instruction)
        rd = get_rd(instruction)
        imm = get_i_type_imm(instruction)
        if i[0] == "l":
            i += f" {rd}, {imm}({rs1})"
        else:
            i += f" {rd}, {rs1}, {imm}"

    elif i_type == "R":
        rs1 = get_rs1(instruction)
        rs2 = get_rs2(instruction)
        rd = get_rd(instruction)
        i += f" {rd}, {rs1}, {rs2}"
    elif i_type == "S":
        rs1 = get_rs1(instruction)
        rs2 = get_rs2(instruction)
        imm = get_s_type_imm(instruction)
        i += f" {rs2}, {imm}({rs1})"
    elif i_type == "SB":
        pass
    elif i_type == "U":
        pass
    elif i_type == "UJ":
        pass

    return i
