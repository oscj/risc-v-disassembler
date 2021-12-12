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

    rs1 = get_rs1(instruction)
    rs2 = get_rs2(instruction)
    rd = get_rd(instruction)
    i_imm = get_i_type_imm(instruction)
    s_imm = get_s_type_imm(instruction)
    sb_imm = get_sb_type_imm(instruction)
    u_imm = get_u_type_imm(instruction)
    uj_imm = get_uj_type_imm(instruction)
    
    if i_type == "I":
        if i[0] == "l": # loads are diff format
            i += f" {rd}, {i_imm}({rs1})"
        else:
            i += f" {rd}, {rs1}, {i_imm}"
            
    elif i_type == "R":
        i += f" {rd}, {rs1}, {rs2}"
        
    elif i_type == "S":
        i += f" {rs2}, {s_imm}({rs1})"
        
    elif i_type == "SB":
        i += f" {rs1}, {rs2}, {sb_imm} "
    
    elif i_type == "U":
        i += f" {rd}, {u_imm}"
    
    elif i_type == "UJ":
        i += f" {rd}, {uj_imm}"
        
    return i
