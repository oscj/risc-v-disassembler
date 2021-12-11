"""
tables.py
----------
Lookup tables for RISC-V RV32I ISA
"""
i_formats = {
    "R": {
        "funct7": 0xFE000000,
        "rs2": 0x01F00000,
        "rs1": 0x000F8000,
        "funct3": 0x00007000,
        "rd": 0x00000F80,
        "op_code": 0x0000007F,
    },
    "I": {
        "imm": 0xFFF00000,
        "rs1": 0x000F8000,
        "funct3": 0x00007000,
        "rd": 0x00000F80,
        "op_code": 0x0000007F,
    },
    "S": {
        "imm_11_5": 0xFE000000,
        "rs2": 0x01F00000,
        "rs1": 0x000F8000,
        "funct3": 0x00007000,
        "imm_4_0": 0x00000F80,
        "op_code": 0x0000007F,
    },
    "SB": {
        "imm_12_10_5": 0xFE000000,
        "rs2": 0x01F00000,
        "rs1": 0x000F8000,
        "funct3": 0x00007000,
        "imm_4_1_11": 0x00000F80,
        "op_code": 0x0000007F,
        "op_code": 0x0000007F,
    },
    "U": {
        "imm_31_12": 0xFFFFF000,
        "rd": 0x00000F80,
        "op_code": 0x0000007F,
    },
    "UJ": {
        "imm_20_10_1_11_10_12": 0xFFFFF000,
        "rd": 0x00000F80,
        "op_code": 0x0000007F,
    },
}

i_type_by_oc = {
    0x3: "I",  # lb, lh, lw, lbu, lhu
    0xF: "I",  # fence, fence.i
    0x13: "I",  # addi, slli, slti, sltiu, xori, srli, srai, ori, andi
    0x17: "U",  # auipc
    0x23: "S",  # sb, sh, sw
    0x33: "R",  # add, sub, sll, slt, sltu, xor, srl, sra, or, and
    0x37: "U",  # lui
    0x63: "SB",  # beq, bne, blt, bge, bltu, bgeu
    0x67: "I",  # jalr
    0x6F: "UJ",  # jal
    0x73: "I",  # ecall, ebreak, CSRRW, CSRRS, CSRRC, CSRRWI, CSRRSI, CSRRCI
}

i_by_codes = (
    {  # outer is opcode, first inner is funct3, second is funct7 (or immediate)
        0x3: {
            0x0: "lb",
            0x1: "lh",
            0x2: "lw",
            0x4: "lbu",
            0x5: "lhu",
        },
        0xF: {
            0x0: "fence",
            0x1: "fence.i",
        },
        0x13: {
            0x0: "addi",
            0x1: "slli",
            0x2: "slti",
            0x3: "sltiu",
            0x4: "xori",
            0x5: {  # funct7
                0x00: "srli",
                0x20: "sali",
            },
            0x6: "ori",
            0x7: "andi",
        },
        0x17: "auipc",  # just opcode
        0x23: {
            0x0: "sb",
            0x1: "sh",
            0x2: "sw",
        },
        0x33: {
            0x0: {  # funct7
                0x00: "add",
                0x20: "sub",
            },
            0x1: "sll",
            0x2: "slt",
            0x3: "sltu",
            0x4: "xor",
            0x5: {  # funct7
                0x00: "srl",
                0x20: "sra",
            },
            0x6: "or",
            0x7: "and",
        },
        0x37: "lui",  # just opcode
        0x63: {
            0x0: "beq",
            0x1: "bne",
            0x4: "blt",
            0x5: "bge",
            0x6: "bltu",
            0x7: "bgeu",
        },
        0x67: "jalr",  # just opcode
        0x6F: "jal",  # just opcode
        0x73: {
            0x0: {
                0x000: "ecall",  # immediate
                0x001: "ebreak",
            },
            0x1: "CSRRW",
            0x2: "CSRRS",
            0x3: "CSRRC",
            0x5: "CSRRWI",
            0x6: "CSRRSI",
            0x7: "CSRRCI",
        },
    }
)


regs = {
    0: "zero",
    1: "ra",
    2: "sp",
    3: "gp",
    4: "tp",
    5: "t0",
    6: "t1",
    7: "t2",
    8: "s0",
    9: "s1",
    10: "a0",
    11: "a1",
    12: "a2",
    13: "a3",
    14: "a4",
    15: "a5",
    16: "a6",
    17: "a7",
    18: "s2",
    19: "s3",
    20: "s4",
    21: "s5",
    22: "s6",
    23: "s7",
    24: "s8",
    25: "s0",
    26: "s10",
    27: "s11",
    28: "t3",
    29: "t4",
    30: "t5",
    31: "t6",
}
