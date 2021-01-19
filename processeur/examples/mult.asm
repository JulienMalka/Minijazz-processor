addi t1, zero, 0
addi t2, zero, 8
addi t3, zero, 0
loop:
beq t2, t3, end
addi t1, t1, 7
addi t3, t3, 1
br loop
end:
addi t0, t1, 0