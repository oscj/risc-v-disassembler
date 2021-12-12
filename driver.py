#!/usr/local/bin/python3
"""
driver.py
---------
Main driver for dissasembling RISC-V binary code.

Author: Oscar Jaimes
"""
import sys
import dissasembler as ds

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./dissasembler.py <binary_riscv_file>")
        exit(1)

    fstr = sys.argv[1]

    try:
        with open(fstr, "rb") as f:
            res = ds.disassemble(f)
            for i in res:
                print(i)
            exit(0)

    except FileNotFoundError:
        print("File not found")
        exit(1)
