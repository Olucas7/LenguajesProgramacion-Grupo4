import ply.lex as lex

# Aqui se escribira el codigo del primer avance Analisis Lexico
# palabras reservadas principales
reserved = {
    'await': 'AWAIT',
    'break': 'BREAK',
    'case': 'CASE',
    'catch': 'CATCH',
    'class': 'CLASS',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'debugger': 'DEBUGGER',
    'default': 'DEFAULT',
    'delete': 'DELETE',
    'do': 'DO',
    'else': 'ELSE',
    'export': 'EXPORT',
    'extends': 'EXTENDS',
    'finally': 'FINALLY',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    'import': 'IMPORT',
    'in': 'IN',
    'instanceof': 'INSTANCEOF',
    'new': 'NEW',
    'return': 'RETURN',
    'super': 'SUPER',
    'switch': 'SWITCH',
    'this': 'THIS',
    'throw': 'THROW',
    'try': 'TRY',
    'typeof': 'TYPEOF',
    'var': 'VAR',
    'void': 'VOID',
    'while': 'WHILE',
    'with': 'WITH',
    'yield': 'YIELD'
}
# tokens
tokens = (
             'NUMBER',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'MOD',
             'ID'
             # Operadores de asignacion
             'ASSIGN', 'ADICTASSI', 'ADMINUS', 'ADTIME', 'ADDIVIDE', 'ADMOOD', 'ADEXP'
             # Operadores logicos
             'ANDE', 'ORE', 'NOTE'
             # Operadores de comparacion
             'SAME', 'NOTSAME',
             'GREATERTHAN', 'GREATEROREQUAL', 'LESSTHAN', 'LESSOREQUAL'
             # SIMBOLOS
             'PERIOD', 'COLON', 'OPENKEY', 'CLOSEBRACE', 'OPENPAREN','CLOSEPARE',
             'OPENBRA', 'CLOSEBRA', 'COMMA'
         ) + tuple(reserved.values())
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'
_ASSIGN = r'='

t_ADICTASSI = r'++'
t_ADMINUS = r'-='
t_ADTIME =  r'*='
t_ADDIVIDE= r'/='
t_ADMOOD = r'%='
t_ADEXP = r'**=='

t_ANDE = r'&&'
t_ORE = r'||'
t_NOTE = r'!'

t_SAME = r'=='
t_NOTSAME = r'!='
t_GREATERTHAN = r'>'
t_GREATEROREQUAL = r'>='
t_LESSTHAN = r'<'
t_LESSOREQUAL = r'<='

t_PERIOD = r'\.'
t_COLON = r';'
t_OPENKEY = r'{'
t_CLOSEBRACE = r'}'
t_OPENPAREN = r'\('
t_CLOSEPARE = r'\)'
t_OPENBRA = r'\['
t_CLOSEBRA = r'\]'
t_COMMA = r','

# funciones

def t_ID(t):
    r'[a-zA-Z_]\w+'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
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
def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
# Build the lexer
lexer = lex.lex()
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")