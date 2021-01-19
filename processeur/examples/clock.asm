addi t0, zero, 0
addi t1, zero, 5
loop:
addi t1, t1, -1
bne t1, zero, loop
next:
addi t0, t0, 1
addi t1, zero, 5
br loop