import ply.yacc as yacc
from lex import tokens
from operations import *

start = 'program'


def p_input(p):
    '''input : INPUT
              | INPUT ID
              | input COMMA ID'''
    if p[1] == "INPUT":
        p[0] = Input()
        if len(p) >=3 and p.slice[2].type == "ID":
            p[0].add_id(p[2])
    else:
        p[1].add_id(p[3])
        p[0] = p[1]


def p_output(p):
    '''output : OUTPUT
              | OUTPUT ID
              | output COMMA ID'''
    if p[1] == "OUTPUT":
        p[0] = Output()
        if len(p) >= 3 and p.slice[2].type == "ID":
            p[0].add_id(p[2])
    else:
        p[1].add_id(p[3])
        p[0] = p[1]

def p_vars(p):
    '''
    vars : VAR var
        | vars COMMA var
    '''
    if isinstance(p[2], Var):
        p[0] = Vars(p[2])
    else:
        p[1].add_var(p[3])
        p[0] = p[1]


def p_exp(p):
    '''
    exp : NOT arg
        | REG var
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
    if len(p)>=3:
        p[0] = Exp(p[1], p[2:])
    else:
        p[0] = Exp(None, [p[1]])

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
        p[0] = Var(p[1], 1)
    else:
        bitlist = []
        for ch in p[1]:
            bitlist.append(int(ch))
        p[0] = bitlist


def p_var(p):
    '''
    var : ID
         | ID COLON int
    '''
    if len(p)>=3:
        p[0] = Var(p[1], p[3][0])
    else:
        p[0] = Var(p[1], 1)

def p_int(p):
    '''
    int : CONST
    '''
    p[0] = [int(p[1])]

def p_program(p):
    '''
    program : input output vars IN equ
             | program equ
    '''
    if isinstance(p[1], Input):
        p[0] = Program(p[1], p[2], p[3], p[5])
    else:
        p[1].add_equ(p[2])
        p[0] = p[1]


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()