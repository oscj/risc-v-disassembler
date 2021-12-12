# fib.s - fibonacci function in RISC-V assembly

# Equivalent C Code:
# ------------------
# int fib(int n){
#    if(n == 0 || n == 1){
#        return 1;
#    } 
#    return fib(n - 1) + fib(n - 2);
# }
#

_Z3fibi:                                # @_Z3fibi
        addi    sp, sp, -32
        sw      ra, 28(sp)                      # 4-byte Folded Spill
        sw      s0, 24(sp)                      # 4-byte Folded Spill
        addi    s0, sp, 32
        sw      a0, -16(s0)
        lw      a0, -16(s0)
        mv      a1, zero
        beq     a0, a1, .LBB0_2
        j       .LBB0_1
.LBB0_1:
        lw      a0, -16(s0)
        addi    a1, zero, 1
        bne     a0, a1, .LBB0_3
        j       .LBB0_2
.LBB0_2:
        addi    a0, zero, 1
        sw      a0, -12(s0)
        j       .LBB0_4
.LBB0_3:
        lw      a0, -16(s0)
        addi    a0, a0, -1
        call    _Z3fibi
        sw      a0, -20(s0)                     # 4-byte Folded Spill
        lw      a0, -16(s0)
        addi    a0, a0, -2
        call    _Z3fibi
        mv      a1, a0
        lw      a0, -20(s0)                     # 4-byte Folded Reload
        add     a0, a0, a1
        sw      a0, -12(s0)
        j       .LBB0_4
.LBB0_4:
        lw      a0, -12(s0)
        lw      s0, 24(sp)                      # 4-byte Folded Reload
        lw      ra, 28(sp)                      # 4-byte Folded Reload
        addi    sp, sp, 32
        ret