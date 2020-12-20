import math
def multiplexer_generator(dict_value):
    size_mul = 0
    for elem in list(dict_value.keys()):
        if elem!="default" and elem!=0 and math.ceil(math.log2(elem)) > size_mul:
            size_mul = math.ceil(math.log2(elem))
    commande = "mux"+str(size_mul)+"bit<32>("
    for i in range(2**size_mul):
        if i in list(dict_value.keys()):
            commande += " "+ str(dict_value[i]) + ","
        else:
            commande += " " + str(dict_value["default"]) + ","
    commande += " sel)"
    return commande


mul_op = {0: "CALL", 23: "LOAD1", 21: "STORE", 58: "opx_res", 12: "UI_OP", 20: "UI_OP", 28: "UI_OP", 6: "BRANCH", 30: "BRANCH", 38: "BRANCH", 46: "BRANCH", 14: "BRANCH", 22: "BRANCH", 54: "BRANCH",  "default": "I_OP"}
print(multiplexer_generator(mul_op))
opx_res = {52:"BREAK", 13:"JUMP", 5: "JUMP", 18: "RI_OP", 26: "RI_OP", 58:"RI_OP", "default": "R_OP"}
print(multiplexer_generator(opx_res))
pc_en = {10:1, 11:1, "default":0}
print(multiplexer_generator(pc_en))
rf_wren = {4:1, 5:1, 7:1, 10:1, 12:1, 13:1, "default":0}
print(multiplexer_generator(rf_wren))
sel_addr = {3:1, 6:1, "default":0}
print(multiplexer_generator(sel_addr))
sel_b = {5:1, 9:1, "default":0}
print(multiplexer_generator(sel_b))
sel_rC = {5:1, 12:1, "default":0}
print(multiplexer_generator(sel_rC))
read = {1:1, 6:1, "default":0}
print(multiplexer_generator(read))
op_alu_op = {58:"op_alu_opx", 14:"[].0.1.1.0.0.1", 22:"[].0.1.1.0.1.0", 30: "[].0.1.1.0.1.1", 38:"[].0.1.1.1.0.0", 46: "[].0.1.1.1.0.1", 54: "[].0.1.1.1.1.0", 12:"[].1.0.0.0.0.1", 20:"[].1.0.0.0.1.0", 28:"[].1.0.0.0.1.1", "default":"[].0.0.0.0.0.0"}
print(multiplexer_generator(op_alu_op))
op_alu_opx = {57:"[].0.0.1.0.0.0", 8:"[].0.1.1.0.0.1", 16:"[].0.1.1.0.1.0", 6:"[].1.0.0.0.0.0", 14:"[].1.0.0.0.0.1", 22:"[].1.0.0.0.1.0", 30:"[].1.0.0.0.1.1", 19:"[].1.1.0.0.1.0", 27: "[].1.1.0.0.1.1", 59:"[].1.1.0.1.1.1", 18:"[].1.1.0.0.1.0", 26:"[].1.1.0.0.1.1", 58:"[].1.1.0.1.1.1", "default":"[].0.0.0.0.0.0"}
print(multiplexer_generator(op_alu_opx))
imm_signed = {4:1, 3:1, 6:1, "default":0}
print(multiplexer_generator(imm_signed))
