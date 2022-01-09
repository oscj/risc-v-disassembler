# risc-v-disassembler

A disassembler for RISC-V (32I) ISA written in Python.

Had a final for a computer architecture class. This is how I reviewed instruction formats.

1. [Usage](#usage)
1. [Example](#example)
1. [Assembling](#assembling)

### Usage
```
./driver <riscv_binary_file>
```

### Example
```
./driver s_files/sum.bin
```

Where sum.bin contains:
```python
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
│00000000│ 13 01 01 ff 23 26 11 00 ┊ 23 24 81 00 13 04 01 01 │•••×#&•0┊#$×0••••│
│00000010│ 23 2a a4 fe 23 28 b4 fe ┊ 03 25 44 ff 83 25 04 ff │#*××#(××┊•%D××%•×│
│00000020│ 33 05 b5 00 03 24 81 00 ┊ 83 20 c1 00 13 01 01 01 │3•×0•$×0┊× ×0••••│
│00000030│ 67 80 00 00             ┊                         │g×00    ┊        │
└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘
```

Final Output:
```python
addi sp, sp, -16
sw ra, 12(sp)
sw s0, 8(sp)
addi s0, sp, 16
sw a0, -12(s0)
sw a1, -16(s0)
lw a0, -12(s0)
lw a1, -16(s0)
add a0, a0, a1
lw s0, 8(sp)
lw ra, 12(sp)
addi sp, sp, 16
jalr zero, ra, 0
```

### Assembling
In order to disassemble a RISC-V binary program, one must first have a RISC-V binary program. To obtain my RISC-V binary programs, I used the [RARS RISC-V Simulator](https://github.com/TheThirdOne/rars)

It comes with a CLI, which uses the following command to assembly a RISC-V assembly file:

```bash
rars <risc_v_assembly_file> a dump .text Binary <output_binary_file>
```

