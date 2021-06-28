import ply.yacc as yacc
from analisisLexico import tokens

#Oscar Lucas
def p_sentencias(p):
    '''sentencias : impresion
                    | expression'''

def p_sentencias_if(p):
    'sentencias : IF LPAREN logical_expresion RPAREN'
def p_sentencias_if_else(p):
    'sentencias : IF LPAREN logical_expresion RPAREN sentencias ELSE sentencias'
def p_sentencias_while(p):
    'sentencias : WHILE LPAREN logical_expresion RPAREN block'
def p_impresion(p):
    'impresion : ALERT LPAREN expression RPAREN'
def p_impresion_vacio(p):
    'impresion : ALERT LPAREN RPAREN'
    p[0] = "Impresion vacia"
def p_expression_plus(p):
    'expression : expression PLUS term'
def p_expression_times(p):
    'expression : expression TIMES term'
def p_expression_divide(p):
    'expression : expression DIVIDE term'
def p_expression_mod(p):
    'expression : expression MOD term'

def p_expression_var(p):
    'expression : VAR ID'
def p_expression_const(p):
    'expression : CONST ID'

def p_expression_logical(p):
    'expression : logical_expresion'
    p[0] = p[1]
def p_expression_greater(p):
    'logical_expresion : expression GREATER term'
def p_expression_less(p):
    'logical_expresion : expression LESS term'
def p_expression_isequal(p):
    'logical_expresion : expression ISEQUAL term'
def p_expression_is_not_identical(p):
    'logical_expresion : expression IS_NOT_IDENTICAL term'
def p_expression_is_identical(p):
    'logical_expresion : expression IS_IDENTICAL term'
def p_expression_block(p):
    'expression : block'
def p_block(p):
    'block : LBLOCK sentencias RBLOCK'
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


#Tatiana Yepez, parametros

def p_javaScript_param(p):
    '''javaScript_param : STRING
                         | NUM
                         | boolean
                         | declareteFunction
                         | p_callFunction


    '''
#Tatiana Yepez para funciones o parametros vacios
def p_empty(p):
    '''empty :'''
    pass
#Para Boolean

def p_boolean(p):
    '''boolean : TRUE
             | FALSE
        '''
    pass

def p_varType(p):
    ''' varType : LET
                | CONST
                | VAR
                 | empty '''

#para declarar variables
def p_varDeclaration(p):
    '''varDeclaration : varType ID  EQUAL  arrayDeclare COLON
                    |   varType ID EQUAL declareMap COLON
                    |   varType ID EQUAL declareSet COLON '''
    pass

#Llamar metodos de estructuras de datos
def p_callMethods(p):
    '''callMethods : ID methodArray COLON
                     | ID methodSet COLON
                     | ID methodMap COLON'''

#declarar array
def p_arrayDeclare(p):
    '''arrayDeclare :  LBRACKET arrayValues RBRACKET
                       | NEW ARRAY LPAREN arrayValues RPAREN
                     '''

    pass

def p_arrayValues(p):
    '''arrayValues :  arrayValue
                    | arrayValue COMMA arrayValue'''
    pass

def p_arrayValue(p):
    ''' arrayValue :  LPAREN expression RPAREN
                      | ID
                      | var
                      | NUM
                      | STRING
                      | boolean
                      | empty '''
    pass

def p_methodArray(p):
    ''' methodArray : PERIOD PUSH LPAREN arrayValue RPAREN
                      | PERIOD UNSHIFT LPAREN arrayValue RPAREN
                      | PERIOD POP LPAREN empty RPAREN '''


def p_declareMap (p) :
    '''declareMap :  NEW MAP LPAREN iterable RPAREN
                    '''

def p_iterable(p):
    '''iterable  : arrayDeclare
                   | setDeclare
                   | empty '''
#Joyce Rojas
def p_methodMap(p):
    '''methodMap : PERIOD CLEAR LPAREN RPAREN
                   | PERIOD LENGTH LPAREN RPAREN '''

#Tatiana Yepez para declaracion de variables
def p_declaration(p):
    '''declaration : varDeclaration
                    |declareteFunction
                    | callFunction
    '''
    pass

# Tatiana Yepez para crear las funciones
def p_declareteFunction(p):
    '''' declareteFunction: FUNCTION ID LPAREN params RPAREN
                          | FUNCTION  ID LPAREN params RPAREN sentencesCmpt '''
    pass

def p_sentencesCmpt(p):
    '''sentencesCmpt : LBLOCK expresion RBLOCK
                     | LBLOCK expresion RETURN RBLOCK  '''
    pass

#Tatiana llamar funciones
def p_callFunction(p):
    '''callFunction : ID LPAREN params RPAREN  
                    
                     ''' #faltan mas maneras de llamar funciones
    pass

def p_params(p):
    '''params: paramList
               | empty  '''
    pass

def p_param(p):
    ''' param: ID
              | ID LBRACKET RBRACKET
               '''
    pass
def paramList(p):
    '''paramList : param
                  | param COMMA param_list '''
    pass

#Definir argumento

def p_args(p):
    ''' args: argslist
            | empty
    '''
    pass
def p_argslist(p):
    '''argslist : argslist COMMA expression
                             | expression
    '''
    pass

# para constructores
def p_constructor(p):
    '''constructor : ID LPAREN RPAREN
                    | ID LPAREN args RPAREN
    '''
    pass

#Joyce Rojas - Declarar un set

def declararSet(p):
    'declararSet: NEW SET LPAREN setValues RPAREN'
    pass

def p_contiene(p):
    'contiene: ID PERIOD HAS LPAREN parametros RPAREN'
    return

def p_setValues(p):
    '''setValues :  setValue
                    | setValue COMMA setValue'''
    pass

def p_setValue(p):
    ''' setValue :    ID
                      | var
                      | NUM
                      | STRING
                      | boolean
                      | empty '''
    pass

def p_methodSet(p):
    ''' methodSet : PERIOD ADD LPAREN setValue RPAREN
                      | PERIOD DELETE LPAREN setValue RPAREN
                      | PERIOD CLEAR LPAREN empty RPAREN '''




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
