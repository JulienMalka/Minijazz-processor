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



# List of token names.   This is always required
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





# Define a rule so we can track line numbers
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

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)