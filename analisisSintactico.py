import ply.yacc as yacc

from analisisLexico import tokens

#Agregando sintaxis para una expresion Tatiana Yepez
def p_sentencia(p) :
    ''' sentencia :  callMethods
                    | callFunction COLON
                    | varDeclaration
                    | controlExpression
                    | impresion
                    | declareteFunction
                    | assingOperadores


                     '''
def p_expression(p):
    '''expression :  conditionalEspecifico
                     | inicializarOp
    '''
    pass
def p_assingOperadores(p):
    ''' assingOperadores : varType ID EQUAL inicializarOp  '''

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
                      | boolean
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
#def p_empty(p):
 #   '''empty : '''
  #  pass
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
              '''


#para declarar variables
def p_varDeclaration(p):
    ''' varDeclaration : varType assign
                    | assign
                    | LET ID COLON
                    | VAR ID COLON
                   '''
    pass
def p_assign(p):
    '''assign : ID  EQUAL  arrayDeclare COLON
                    |  ID EQUAL declareMap COLON
                    |  ID EQUAL declararSet COLON
                    |  ID EQUAL javaScript_param COLON'''



#Llamar metodos de estructuras de datos
def p_callMethods(p):
    ''' callMethods : ID methodArray COLON
                     | ID methodSet COLON
                     | ID methodMap COLON'''


#declarar array
def p_arrayDeclare(p):
    '''arrayDeclare :  LBRACKET  arrayValues RBRACKET
                       | LBRACKET  RBRACKET
                       | NEW ARRAY LPAREN arrayValues RPAREN
                       | NEW ARRAY LPAREN  RPAREN
                     '''


def p_arrayValues(p):
    '''arrayValues :  javaScript_param
                    | javaScript_param COMMA arrayValues '''




def p_methodArray(p):
    ''' methodArray : PERIOD PUSH LPAREN javaScript_param RPAREN
                      | PERIOD UNSHIFT LPAREN javaScript_param RPAREN
                      | PERIOD POP LPAREN  RPAREN '''


def p_declareMap (p) :
    '''declareMap :  NEW MAP LPAREN LBRACKET iterable RBRACKET RPAREN
                    | NEW MAP LPAREN  RPAREN
                    '''

def p_iterableMap(p):
    ''' iterableMap : LBRACKET keyValue COMMA keyValue RBRACKET
                      | LBRACKET keyValue COMMA keyValue RBRACKET COMMA iterableMap'''

def p_iterable(p):
    ''' iterable : iterableMap
                   | iterableArray
                   | iterableSet '''
def p_keyValue(p):
    ''' keyValue : javaScript_param
                  | iterableMap
                  | iterableArray
                  | iterableSet
                  | declareMap
                  | arrayDeclare '''

def p_iterableArray(p):
    ''' iterableArray :  arrayDeclare
                       | arrayDeclare COMMA arrayDeclare '''

def p_iterableSet(p):
    ''' iterableSet : declararSet
                     | declararSet COMMA declararSet
                    | '''
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
               '''
    pass

#def p_param(p):
 #   ''' param : ID
  #            | ID LBRACKET RBRACKET
   #           |
    #           '''
    #pass

def p_paramList(p):
    '''paramList : javaScript_param
                  | javaScript_param COMMA paramList '''
    pass

#Definir argumento

def p_args(p):
    ''' args : argslist
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
    '''declararSet : NEW SET LPAREN LBRACKET iterable RBRACKET RPAREN
                    '''

    pass



# def p_setValues(p):
#     '''setValues :  setValue
#                     | setValue COMMA setValue'''
#     pass
#
# def p_setValue(p):
#     ''' setValue : ID
#                  | NUM
#                  | STRING
#                  | boolean
#  '''
#     pass

def p_methodSet(p):
    ''' methodSet : PERIOD ADD LPAREN javaScript_param RPAREN
                      | PERIOD DELETE LPAREN javaScript_param RPAREN
                      | PERIOD CLEAR LPAREN RPAREN '''


#REGLAS SEMANTICAS

# Semantica operadores Matematicos Tatiana Yepez

def p_inicializarOp(p):
    ''' inicializarOp :  PLUS operacionesMath
                        | MINUS operacionesMath
                        | operacionesMath '''

def p_operacionesMath(p):
    ''' operacionesMath :  numOperadores PLUS suma
                         | suma
                          | suma operacionesMath
                         | restas
                         | numOperadores MINUS restas
                         | restas operacionesMath
                         | multiplicacion
                         | numOperadores TIMES multiplicacion
                         | multiplicacion operacionesMath
                         | divicion
                         | numOperadores DIVIDE divicion
                         | divicion operacionesMath'''

def p_suma(p):
    '''suma : numOperadores PLUS LPAREN numOperadores RPAREN
            | numOperadores PLUS NUM
            | numOperadores

            '''
def p_restas(p):
    ''' restas : numOperadores MINUS LPAREN numOperadores RPAREN
               | numOperadores  MINUS NUM
               | numOperadores '''

def p_multiplicacion (p):
    ''' multiplicacion : numOperadores TIMES LPAREN numOperadores RPAREN
               | numOperadores  TIMES NUM
               | numOperadores '''

def p_divicion (p):
    ''' divicion : numOperadores DIVIDE LPAREN numOperadores RPAREN
               | numOperadores  DIVIDE NUM
               | numOperadores '''

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


#Semantica boolean condiciones

def p_coditionalEspecifico(p):
    ''' conditionalEspecifico :  ID opConditional dataCondi
                    |  NUM opConditional NUM
                    | STRING opConditional STRING 
                    '''


def p_dataCondi(p):
    '''dataCondi : STRING
                  | NUM '''

#nivel de estructuras de datos - oscar lucas
def p_setMetodoAdd(p):
    'setMetodoAdd : PERIOD ADD LPAREN javaScript_param RPAREN'
def p_SetMetodoDelete(p):
    'setMetodoDelete :  PERIOD DELETE LPAREN javaScript_param RPAREN'
def p_SetMetodoClear(p):
    'setMetodoClear : PERIOD CLEAR LPAREN RPAREN '

def p_ValueMapMethods(p):
    ''' ValueMapMethods : ID
                 | NUM
                 | STRING
                  '''
    pass
def p_MapMetodoGet(p):
    'mapMetodoGet : PERIOD GET LPAREN ValueMapMethods RPAREN'
def p_MapMetodoSet(p):
    'mapMetodoSet : PERIOD GET LPAREN ValueMapMethods COMMA ValueMapMethods RPAREN'


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
