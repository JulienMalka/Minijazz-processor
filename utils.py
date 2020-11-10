def convert_int(bit_list):
    out = 0
    for bit in bit_list:
        out = (out << 1) | bit
    return out
