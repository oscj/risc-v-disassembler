addi    sp, sp, -16
sw      ra, 12(sp)                      # 4-byte Folded Spill
sw      s0, 8(sp)                       # 4-byte Folded Spill
addi    s0, sp, 16
sw      a0, -12(s0)
lw      a0, -12(s0)
mul     a0, a0, a0
lw      s0, 8(sp)                       # 4-byte Folded Reload
lw      ra, 12(sp)                      # 4-byte Folded Reload
addi    sp, sp, 16
ret