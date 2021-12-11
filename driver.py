#!/usr/local/bin/python3
"""
driver.py
---------
Main driver for dissasembling RISC-V binary code.

Author: Oscar Jaimes
Last Updated: 11/12/2021
"""
import sys
import dissasembler as ds

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./dissasembler.py <file>")
        exit(1)

    fstr = sys.argv[1]

    try:
        with open(fstr, "rb") as f:
            res = ds.disassemble(f)
            for res in res:
                print(res)

    except FileNotFoundError:
        print("File not found")
        exit(1)
