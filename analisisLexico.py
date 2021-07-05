import ply.lex as lex


# Aqui se escribira el codigo del primer avance Analisis Lexico
# palabras reservadas principales
reserved = {
    'const' : 'CONST',
    'delete': 'DELETE',
    'else': 'ELSE',
    'function': 'FUNCTION',
    'if': 'IF',
    'new' : 'NEW',
    'return': 'RETURN',
    'var': 'VAR',
    'while': 'WHILE',
    'with': 'WITH',
    'yield': 'YIELD',
    'alert' : 'ALERT',
    'Map' : 'MAP',
    'true': 'TRUE',
    'let' : 'LET',
    'false' : 'FALSE',
    'push' : 'PUSH',
    'pop' : 'POP',
    'add' : 'ADD',
    'clear' : 'CLEAR',
    'length' : 'LENGTH',
    'Array' : 'ARRAY',
    'unshift' : 'UNSHIFT',
     'has' : 'HAS',
     'set' : 'SET',
    'get' : 'GET'
}
# tokens
tokens = (
             'NUM',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'MOD',
             'ID',
             'STRING',
             # Operadores de asignacion
             'EQUAL', 'PLUS_EQUAL', 'MINUS_EQUAL', 'MUL_EQUAL',
             'DIV_EQUAL', 'MOD_EQUAL',
             # Operadores logicos
             'AND', 'OR', 'NOT',
             # Operadores de comparacion
             'ISEQUAL', 'IS_NOT_IDENTICAL',
             'GREATER', 'GREATEREQUAL', 'LESS', 'LESSEQUAL', 'IS_IDENTICAL',
             # SIMBOLOS
             'PERIOD', 'COLON', 'LBLOCK', 'RBLOCK',
             'LBRACKET', 'RBRACKET', 'COMMA', 'TWOPOINTS'
         ) + tuple(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'
t_EQUAL = r'='

#t_PLUS_EQUAL = r'\+='
#t_MINUS_EQUAL = r'-='
#t_MUL_EQUAL = r'\*='
#t_DIV_EQUAL = r'/='
#t_MOD_EQUAL = r'%='



t_ISEQUAL = r'=='
t_IS_NOT_IDENTICAL = r'!='
t_IS_IDENTICAL = r"==="
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_LESS = r'<'
t_LESSEQUAL = r'<='

t_PERIOD = r'\.'
t_COLON = r';'
t_TWOPOINTS = r':'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','

# funciones

def t_AND(t):
    r'\&&'
    return t


def t_OR(t):
    r'\|\|'
    return t

def t_NOT(t):
    r'\!'
    return t


def t_ID(t):
    r'(\$ | _ )[A-z0-9]+ | [A-z]+\w*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t
# A regular expression rule with some action code
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENTS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

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

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
# Build the lexer
lexer = lex.lex()
#linea=" "
#while linea!="":
 #   linea=input(">>")
    #lexer.input(linea)
    #getTokens(lexer)
# Tokenize
#print("Succesfull")

data = ''' 89
"asdasdasd"

'''
# Give the lexer some input
lexer.input(data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
