#Aqui se escribira el codigo del primer avance Analisis Lexico
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
}


tokens = (
    #Operadores basicos
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    #Operadores de asignacion
    'ASSIGN', 'ADICTASSI', 'ADMINUS', 'ADTIME', 'ADDIVIDE','ADMOOD', 'ADEXP'
     #Operadores logicos
    'ANDE', 'ORE', 'NOTE'
     #Operadores de comparacion
     'SAME', 'NOTSAME', 'GREATERTHAN', 'GREATEROREQUAL', 'LESSTHAN', 'LESSOREQUAL'
     #SIMBOLOS
     'PERIOD', 'COLON' , 'OPENKEY', 'CLOSEBRACE', 'OPENPAREN', 'CLOSEPARE',
    'OPENBRA', 'CLOSEBRA', 'COMMA'


) + tuple(reserved.values())
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'

t_ASSIGN = r'='
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



