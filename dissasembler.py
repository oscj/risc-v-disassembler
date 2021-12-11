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


def disassemble_instruction(instruction: bytes):
    oc = get_opcode(instruction)
    i_type = i_type_by_oc[oc]
    i_format = i_formats[i_type]
    i = get_instruction(oc, i_format)
    
    return instruction

def get_instruction(opcode: int, i_format: dict) -> str:
    return ""

def translate_register(reg: int) -> str:
    return regs[reg]


def get_opcode(instruction: bytes) -> int:
    m = bytes([]).fromhex("0000007F")  # mask for opcode into bytes
    oc_bytes = bitwise_and_bytes(instruction, m)
    return bf.int_from_bytes(oc_bytes)
