"""
extractors.py
-------------
Module containing functions to extract data from RISC-V instructions.
"""
from tables import regs
from tables import i_by_codes


def get_instruction(instruction: bytes, opcode: int, i_format: dict, i_type: str) -> str:
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
    return (imm) >> 20


def get_r_type_funct7(instruction: bytes) -> int:
    m = bytes([]).fromhex("FE000000")  # mask for funct7 into bytes
    f7 = bitwise_and_bytes(instruction, m)
    return (f7) >> 25


def get_funct3(instruction: bytes) -> int:
    m = bytes([]).fromhex("00007000")  # mask for funct3 into bytes
    f3 = bitwise_and_bytes(instruction, m)
    return (f3) >> 12  # don't forget shift


def get_opcode(instruction: bytes) -> int:
    m = bytes([]).fromhex("0000007F")  # mask for opcode into bytes
    oc_bytes = bitwise_and_bytes(instruction, m)
    return oc_bytes  # no need to shift bois


def get_rs1(instruction: bytes) -> int:
    m = bytes([]).fromhex("000F8000")  # mask for rs1 into bytes
    rs1 = bitwise_and_bytes(instruction, m)
    rs1 = (rs1) >> 15
    rs1_translated = translate_register((rs1))
    return rs1_translated


def get_rs2(instruction: bytes) -> int:
    m = bytes([]).fromhex("01F00000")  # mask for rs2 into bytes
    rs2 = bitwise_and_bytes(instruction, m)
    rs2 = (rs2) >> 20
    rs2_translated = translate_register((rs2))
    return rs2_translated


def get_rd(instruction: bytes) -> int:
    m = bytes([]).fromhex("00000F80")  # mask for rd into bytes
    rd = bitwise_and_bytes(instruction, m)
    rd = (rd) >> 7
    rd_translated = translate_register((rd))
    return rd_translated


def get_s_type_imm(instruction: bytes) -> int:
    imm_11_5_m = bytes([]).fromhex("FE000000")  # mask for imm_11_5 into bytes
    imm_4_0_m = bytes([]).fromhex("00000F80")  # mask for imm_4_0 into bytes

    imm_11_5_m = bitwise_and_bytes(instruction, imm_11_5_m) >> 20
    imm_4_0_m = bitwise_and_bytes(instruction, imm_4_0_m) >> 7
    imm = imm_11_5_m | imm_4_0_m
    return imm


def get_sb_type_imm(instruction: bytes) -> int:
    pass


def get_u_type_imm(instruction: bytes) -> int:
    pass


def get_uj_type_imm(instruction: bytes) -> int:
    pass


def translate_register(reg: int) -> str:
    return regs[reg]


def bitwise_and_bytes(a, b):
    result_int = int.from_bytes(a, byteorder="big", signed=True) & int.from_bytes(
        b, byteorder="big", signed=True
    )
    return result_int
