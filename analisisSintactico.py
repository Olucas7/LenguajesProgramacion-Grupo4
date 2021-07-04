import ply.yacc as yacc
from analisisLexico import tokens

#Agregando sintaxis para una expresion Tatiana Yepez
def p_sentencia(p) :
    ''' sentencia :  callMethods
                    | varType ID EQUAL callMethods
                    | callFunction
                    | javaScript_param
                    | varDeclaration
                    | controlExpression
                    | impresion
                    | operacionesMath
                    | declareteFunction

                     '''
def p_expression(p):
    '''expression :  ID opConditional ID
                     | ID opConditional NUM
                     | NUM opConditional NUM
                     | operacionesMath

    '''
    pass

def p_controlExpression(p):
    '''controlExpression : sentencias_if
                        | sentencias_if_else
                        | sentencias_while
                        | impresion
                        | impresion_vacio
            '''
    pass

def p_opConditional(p):
    ''' opConditional : ISEQUAL
                      |  IS_NOT_IDENTICAL
                      |  IS_IDENTICAL
                      | GREATER
                      | GREATEREQUAL
                      | LESS
                      | LESSEQUAL
                      '''
def p_operadorLogical(p) :
    '''operadorLogical : AND
                        | OR
                        | NOT '''

#Oscar Lucas
def p_sentencias_if(p):
    '''sentencias_if : IF LPAREN expression operadorLogical expression  RPAREN LBLOCK sentencia RBLOCK
                    | IF LPAREN expression RPAREN LBLOCK sentencia RBLOCK'''

def p_sentencias_if_else(p):
    '''sentencias_if_else : IF LPAREN expression operadorLogical expression  RPAREN LBLOCK sentencia RBLOCK ELSE LBLOCK sentencia RBLOCK
                          | IF LPAREN expression RPAREN LBLOCK sentencia RBLOCK ELSE LBLOCK sentencia RBLOCK '''

def p_sentencias_while(p):
    '''sentencias_while : WHILE LPAREN  expression RPAREN LBLOCK sentencia RBLOCK
                        | WHILE LPAREN  expression operadorLogical expression RPAREN LBLOCK sentencia RBLOCK'''

def p_impresion(p):
    'impresion : ALERT LPAREN expression  RPAREN'
def p_impresion_vacio(p):
    'impresion_vacio : ALERT LPAREN RPAREN'
    p[0] = "Impresion vacia"

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
                         | ID
    '''



#Tatiana Yepez para funciones o parametros vacios
def p_empty(p):
    '''empty : '''
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
                    |   varType ID EQUAL declararSet COLON '''
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


def p_arrayValues(p):
    '''arrayValues :  arrayValue
                    | arrayValue COMMA arrayValue'''
    pass

def p_arrayValue(p):
    ''' arrayValue :  LPAREN expression RPAREN
                      | ID
                      | NUM
                      | STRING
                      | boolean
                      | empty '''

def p_methodArray(p):
    ''' methodArray : PERIOD PUSH LPAREN arrayValue RPAREN
                      | PERIOD UNSHIFT LPAREN arrayValue RPAREN
                      | PERIOD POP LPAREN empty RPAREN '''


def p_declareMap (p) :
    '''declareMap :  NEW MAP LPAREN iterable RPAREN
                    '''

def p_iterable(p):
    '''iterable  : arrayDeclare
                   | declararSet
                   | empty '''
#Joyce Rojas
def p_methodMap(p):
    '''methodMap : PERIOD CLEAR LPAREN RPAREN
                   | PERIOD LENGTH LPAREN RPAREN '''


# Tatiana Yepez para crear las funciones
def p_declareteFunction(p):
    ''' declareteFunction : FUNCTION ID LPAREN params RPAREN
                          | FUNCTION  ID LPAREN params RPAREN sentencesCmpt
                          | varType ID EQUAL FUNCTION LPAREN params RPAREN
                          '''
    pass

def p_sentencesCmpt(p):
    '''sentencesCmpt : LBLOCK sentencia RBLOCK
                     | LBLOCK sentencia RETURN RBLOCK  '''
    pass

#Tatiana llamar funciones
def p_callFunction(p):
    '''callFunction : ID LPAREN params RPAREN  
                    
                     ''' #faltan mas maneras de llamar funciones
    pass

def p_params(p):
    '''params : paramList
               | empty  '''
    pass

def p_param(p):
    ''' param : ID
              | ID LBRACKET RBRACKET
               '''
    pass
def p_paramList(p):
    '''paramList : param
                  | param COMMA paramList '''
    pass

#Definir argumento

def p_args(p):
    ''' args : argslist
            | empty
            | javaScript_param
    '''
    pass
def p_argslist(p):
    ''' argslist : args
                   | args COMMA argslist
    '''
    pass



#Joyce Rojas - Declarar un set

def p_declararSet(p):
    'declararSet : NEW SET LPAREN setValues RPAREN'
    pass

def p_contiene(p):
    'contiene : ID PERIOD HAS LPAREN params RPAREN'
    pass

def p_setValues(p):
    '''setValues :  setValue
                    | setValue COMMA setValue'''
    pass

def p_setValue(p):
    ''' setValue : ID
                 | NUM
                 | STRING
                 | boolean
                 | empty '''
    pass

def p_methodSet(p):
    ''' methodSet : PERIOD ADD LPAREN setValue RPAREN
                      | PERIOD DELETE LPAREN setValue RPAREN
                      | PERIOD CLEAR LPAREN empty RPAREN '''


#REGLAS SEMANTICAS

# Semantica operadores Matematicos Tatiana Yepez
def p_operacionesMath(p):
    ''' operacionesMath :  sumas
                          | sumas operacionesMath
                         | restas
                         | restas operacionesMath'''

def p_sumas(p):
    '''sumas : numOperadores PLUS LPAREN numOperadores RPAREN
            | numOperadores PLUS NUM
            '''

def p_numOperadores(p):
    ''' numOperadores : enteros
                     |  decimales  '''
    pass
def p_enteros(p):
    ''' enteros : NUM
                 | numNegative '''
    pass
def p_numNegative(p):
    '''numNegative : MINUS NUM
                 | '''
    pass
def p_decimales(p):
    '''decimales : enteros PERIOD NUM  '''


def p_restas(p):
    ''' restas : numOperadores MINUS LPAREN numOperadores RPAREN
               | numOperadores  MINUS NUM '''

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
    if not s:
        continue
    result = parser.parse(s)
    print(result)
