import ply.yacc as yacc
from Ejemplo_Lexico import tokens
def p_sentencias(p):
    '''sentencias : impresion
                    | expression'''
def p_sentencias_if(p):
    'sentencias : IF LPAREN factor MAYOR factor RPAREN impresion'
def p_impresion(p):
    'impresion : PRINT LPAREN expression RPAREN'
def p_impresion_vacio(p):
    'impresion : PRINT LPAREN RPAREN'
    p[0] = "Impresion vacia"
def p_expression_plus(p):
    'expression : expression PLUS term'
def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]
def p_factor_var(p):
    'factor : ID'
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")
"""
More information on these methods is as follows:
parser.errok(). This resets the parser state so it doesn't think it's in error-recovery mode. This will prevent an error token from being generated and will reset the internal error counters so that the next syntax error will call p_error() again.
parser.token(). This returns the next token on the input stream.
parser.restart(). This discards the entire parsing stack and resets the parser to its initial state.
"""
# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)