import ply.yacc as yacc
from lex import tokens
from operations import *

start = 'program'


def p_input_id(p):
    '''input : INPUT ID
              | input COMMA ID'''
    if p[1] == "INPUT":
        p[0] = input(p[2])
    else:
        p[1].add_id(p[3])
        p[0] = p[1]


def p_output(p):
    '''output : OUTPUT ID
              | output COMMA ID'''
    if p[1] == "OUTPUT":
        p[0] = output(p[2])
    else:
        p[1].add_id(p[3])
        p[0] = p[1]

def p_var(p):
    '''
    var : VAR ID
        | var COMMA ID
    '''
    if p[1] == "VAR":
        p[0] = vars(p[2])
    else:
        p[1].add_id(p[3])
        p[0] = p[1]

def p_xor(p):
    '''
    xor : XOR ID ID
    '''
    p[0] = op("XOR", [p[2], p[3]])

def p_or(p):
    '''
    or : OR ID ID
    '''
    p[0] = op("OR", [p[2], p[3]])

def p_and(p):
    '''
    and : AND ID ID
    '''
    p[0] = op("AND", [p[2], p[3]])


def p_equ(p):
    '''
    equ : ID EQUAL xor
         | ID EQUAL or
         | ID EQUAL and
    '''
    p[0] = equ(p[1], p[3])


def p_program(p):
    '''
    program : input output var IN equ
             | program equ
    '''
    if type(p[1]) == type(input("test")):
        p[0] = program(p[1], p[2], p[3], p[5])
    else:
        p[1].add_equ(p[2])
        p[0] = p[1]


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

data = '''
INPUT a, b, c_in
OUTPUT s, c_out
VAR
a, b, c_in, s, c_out,
_t_1, _l_2, _l_3
IN
t_1 = XOR a b
s = XOR t_1 c_in
c_out = OR _l_2 _l_3
_l_2 = AND a b
_l_3 = AND t_1 c_in
'''



result = parser.parse(data)
print(result)
