import ply.yacc as yacc
from lex import tokens
from operations import *

start = 'program'


def p_input(p):
    '''input : INPUT ID
              | input COMMA ID'''
    if p[1] == "INPUT":
        p[0] = Input(p[2])
    else:
        p[1].add_id(p[3])
        p[0] = p[1]


def p_output(p):
    '''output : OUTPUT ID
              | output COMMA ID'''
    if p[1] == "OUTPUT":
        p[0] = Output(p[2])
    else:
        p[1].add_id(p[3])
        p[0] = p[1]

def p_vars(p):
    '''
    vars : VAR var
        | vars COMMA var
    '''
    if type(p[2]) == type(Var("test")):
        p[0] = Vars(p[2])
    else:
        p[1].add_var(p[3])
        p[0] = p[1]


def p_exp(p):
    '''
    exp : NOT arg
        | REG ID
        | arg
        | AND arg arg
        | OR arg arg
        | NAND arg arg
        | XOR arg arg
        | MUX arg arg arg
        | ROM int int arg
        | RAM int int arg arg arg arg
        | CONCAT arg arg
        | SELECT int arg
        | SLICE int int arg'''
    p[0] = Exp(p[1], p[2:])

def p_equ(p):
    '''
    equ : ID EQUAL exp
    '''
    p[0] = Equ(p[1], p[3])

def p_arg(p):
    '''
    arg : CONST
        | ID
    '''
    if p.slice[1].type == "ID":
        p[0] = Var(p[1])
    else:
        p[0] = p[1]

def p_var(p):
    '''
    var : ID
         | ID COLON int
    '''
    p[0] = Var(p[1])

def p_int(p):
    '''
    int : CONST
    '''
    p[0] = int(p[1])

def p_program(p):
    '''
    program : input output vars IN equ
             | program equ
    '''
    if type(p[1]) == type(Input("test")):
        p[0] = Program(p[1], p[2], p[3], p[5])
    else:
        p[1].add_equ(p[2])
        p[0] = p[1]


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

data = '''
INPUT ra, we, wa, c
OUTPUT o
VAR
  _l_10_22, _l_10_35, _l_10_48, _l_10_61, _l_11_21, _l_11_34, _l_11_47, 
  _l_11_60, _l_12_20 : 3, _l_12_33 : 2, _l_12_46 : 1, _l_13_19 : 3, _l_13_32 : 2, 
  _l_13_45 : 1, _l_14_18 : 3, _l_14_31 : 2, _l_14_44 : 1, _l_16 : 4, 
  _l_9_23, _l_9_36, _l_9_49, _l_9_62, c : 4, o : 4, ra : 2, wa : 2, we
IN
o = RAM 2 4 ra we wa _l_16
_l_16 = CONCAT _l_11_21 _l_14_18
_l_9_23 = SELECT 0 o
_l_10_22 = SELECT 0 c
_l_11_21 = OR _l_9_23 _l_10_22
_l_12_20 = SLICE 1 3 o
_l_13_19 = SLICE 1 3 c
_l_14_18 = CONCAT _l_11_34 _l_14_31
_l_9_36 = SELECT 0 _l_12_20
_l_10_35 = SELECT 0 _l_13_19
_l_11_34 = OR _l_9_36 _l_10_35
_l_12_33 = SLICE 1 2 _l_12_20
_l_13_32 = SLICE 1 2 _l_13_19
_l_14_31 = CONCAT _l_11_47 _l_14_44
_l_9_49 = SELECT 0 _l_12_33
_l_10_48 = SELECT 0 _l_13_32
_l_11_47 = OR _l_9_49 _l_10_48
_l_12_46 = SLICE 1 1 _l_12_33
_l_13_45 = SLICE 1 1 _l_13_32
_l_14_44 = _l_11_60
_l_9_62 = SELECT 0 _l_12_46
_l_10_61 = SELECT 0 _l_13_45
_l_11_60 = OR _l_9_62 _l_10_61
'''



result = parser.parse(data)
print(result)
