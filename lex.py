import ply.lex as lex

reserved = [
    "AND",
    "CONCAT",
    "IN",
    "INPUT",
    "MUX",
    "NAND",
    "NOT",
    "OR",
    "OUTPUT",
    "RAM",
    "REG",
    "ROM",
    "SELECT",
    "SLICE",
    "VAR",
    "XOR"
]

tokens = [
    "CONST",
    "ID",
    "EQUAL",
    "COMMA",
    "COLON"
         ] + reserved


# Regular expression rules for simple tokens
t_CONST = r'[0-9]+'
t_COMMA = r','
t_EQUAL = r'='
t_COLON = r':'

def t_ID(t):
    r'_?[A-Z a-z](_?[A-Za-z0-9])*'
    if t.value in reserved:
        t.type = t.value
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

data = '''
INPUT 
OUTPUT o
VAR
  _l_2, c, o
IN
c = NOT _l_2
o = REG c
_l_2 = REG o
 '''


lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)