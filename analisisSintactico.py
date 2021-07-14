import ply.yacc as yacc

from analisisLexico import tokens

#Agregando sintaxis para una expresion Tatiana Yepez
def p_sentencia(p) :
    ''' sentencia :  callMethods
                    | callFunction COLON
                    | varDeclaration
                    | controlExpression
                    | declareteFunction


       '''
def p_expression(p):
    '''expression :  conditionalEspecifico
                     | inicializarOp
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
                      | boolean
                      '''
def p_operadorLogical(p) :
    '''operadorLogical : AND
                        | OR
                        | NOT '''

#Oscar Lucas
def p_sentencias_if(p): #Javascript es muy flexible con operaciones matematicas: condicion == 0 no entra caso contrario si entra.
    '''sentencias_if : IF LPAREN expression operadorLogical expression  RPAREN cuerpo_de_sentencias
                    | IF LPAREN expression RPAREN cuerpo_de_sentencias
    '''


def p_sentencias_if_else(p):
    '''sentencias_if_else : IF LPAREN expression operadorLogical expression  RPAREN cuerpo_de_sentencias ELSE cuerpo_de_sentencias
                          | IF LPAREN expression RPAREN cuerpo_de_sentencias ELSE cuerpo_de_sentencias
    '''
def p_cuerpo_de_sentencias(p):
    '''cuerpo_de_sentencias : LBLOCK sentencia RBLOCK
                            | LBLOCK RBLOCK
                            '''

def p_sentencias_while(p):
    '''sentencias_while : WHILE LPAREN  expression RPAREN cuerpo_de_sentencias
                        | WHILE LPAREN  expression operadorLogical expression RPAREN cuerpo_de_sentencias

    '''

def p_impresion(p):
    '''impresion : ALERT LPAREN valores_de_impresion RPAREN COLON

    '''
def p_valores_de_impresion(p):
    '''valores_de_impresion : inicializarOp
                              | javaScript_param
                              | callFunction
                              | estructuras_datos
                              | return_ops


    '''
def p_impresion_vacio(p):
    'impresion_vacio : ALERT LPAREN RPAREN COLON'
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
                         | inicializarOp
                         | boolean
                         | ID

    '''

#Para Boolean

def p_boolean(p):
    '''boolean : TRUE
             | FALSE
        '''
    pass


def p_varType_let(p):
    ''' varType_let : LET
                    | VAR
    '''

def p_varType(p):
    ''' varType :  varType_let
                  | CONST '''
#para declarar variables
def p_varDeclaration(p):
    ''' varDeclaration : varType assign COLON
                    | assign COLON
                    | varType_let ID COLON
                    | varType_let assign COLON
    '''
    pass

def p_assign(p):
    '''assign : ID  EQUAL  estructuras_datos
                |  ID EQUAL javaScript_param
                | ID EQUAL
                 '''


def p_estructuras_datos(p):
    ''' estructuras_datos : arrayDeclare
                            | declararSet
                            | declareMap

    '''

#Llamar metodos de estructuras de datos
def p_callMethods(p):
    ''' callMethods : ID methodArray COLON
                     | ID methodSet COLON
                     | ID methodMap COLON '''


#declarar array
def p_arrayDeclare(p):
    '''arrayDeclare :  LBRACKET  RBRACKET
                       | LBRACKET  arrayValues RBRACKET
                       | NEW ARRAY LPAREN arrayValues RPAREN
                       | NEW ARRAY LPAREN  RPAREN
                     '''


def p_arrayValues(p):
    ''' arrayValues :  javaScript_param
                    | javaScript_param COMMA arrayValues '''




def p_methodArray(p):
    ''' methodArray : PERIOD PUSH LPAREN javaScript_param RPAREN
                      | PERIOD UNSHIFT LPAREN arrayValues RPAREN
                      | PERIOD POP LPAREN  RPAREN '''


def p_declareMap (p) :
    '''declareMap :  NEW MAP LPAREN LBRACKET iterableMap RBRACKET RPAREN
                    | NEW MAP LPAREN  RPAREN
                    '''

def p_iterableMap(p):
    ''' iterableMap : LBRACKET keyValue COMMA keyValue RBRACKET
                      | LBRACKET keyValue COMMA keyValue RBRACKET COMMA iterableMap'''


def p_keyValue(p):
    ''' keyValue : javaScript_param
                  | declararSet
                  | declareMap
                  | arrayDeclare '''



def p_iterableSet(p):
    ''' iterableSet : keyValue
                     | keyValue COMMA iterableSet
                    | '''
#Joyce Rojas
def p_methodMap(p):
    '''methodMap : PERIOD CLEAR LPAREN RPAREN
                   | PERIOD SIZE '''


# Tatiana Yepez para crear las funciones
def p_declareteFunction(p):
    ''' declareteFunction : FUNCTION  ID LPAREN params RPAREN sentencesCmpt
                          | FUNCTION  ID LPAREN RPAREN sentencesCmpt
    '''
    pass

def p_sentencesCmpt(p):
    '''sentencesCmpt : LBLOCK sentencia RBLOCK
                     | LBLOCK RBLOCK
                     | LBLOCK RETURN valores_de_impresion COLON RBLOCK
                     | LBLOCK sentencia RETURN valores_de_impresion COLON RBLOCK   '''
    pass

def p_return_ops(p):
    ''' return_ops : javaScript_param
                    | javaScript_param operadores_mat return_ops '''

def p_operadores_mat(p):
    ''' operadores_mat : PLUS
                        | MINUS
                        | DIVIDE
                        | TIMES

    '''
#Tatiana llamar funciones
def p_callFunction(p):
    '''callFunction : ID LPAREN params RPAREN
                    | ID LPAREN RPAREN
                    
                     '''
    pass

def p_params(p):
    '''params :  javaScript_param
            | javaScript_param COMMA params
               '''
    pass



#Definir argumento
def p_args(p):
    ''' args : javaScript_param
             | javaScript_param COMMA args
     '''




#Joyce Red's - Declarar un set

def p_declararSet(p):
    ''' declararSet : NEW SET LPAREN RPAREN
                    | NEW SET LPAREN LBRACKET iterableSet RBRACKET RPAREN
    '''

    pass





def p_methodSet(p):
    ''' methodSet : PERIOD ADD LPAREN javaScript_param RPAREN
                      | PERIOD DELETE LPAREN javaScript_param RPAREN
                      | PERIOD CLEAR LPAREN RPAREN '''


#REGLAS SEMANTICAS

# Semantica operadores Matematicos Tatiana Yepez

def p_inicializarOp(p):
    ''' inicializarOp : MINUS operacionesMath
                    | PLUS operacionesMath
                    | operacionesMath
                    | numOperadores '''

def p_operacionesMath(p):
    ''' operacionesMath :  suma
                       | resta
                       | multiplicacion
                       | divicion '''

def p_suma(p):
    ''' suma : numOperadores PLUS inicializarOp
           | numOperadores PLUS LPAREN inicializarOp RPAREN
            | numOperadores PLUS suma
            |  numOperadores PLUS LPAREN inicializarOp RPAREN suma
         '''
    pass
def p_resta(p):
    ''' resta : numOperadores MINUS inicializarOp
             | numOperadores MINUS LPAREN inicializarOp RPAREN
             | numOperadores MINUS resta
             | numOperadores MINUS LPAREN inicializarOp RPAREN resta'''


def p_multiplicacion (p):
     ''' multiplicacion : numOperadores TIMES LPAREN inicializarOp RPAREN
                | numOperadores  TIMES  inicializarOp
                | numOperadores  TIMES  multiplicacion
                 '''

def p_divicion (p):
     ''' divicion : numOperadores DIVIDE LPAREN inicializarOp RPAREN
                | numOperadores  DIVIDE inicializarOp
                | numOperadores  DIVIDE divicion '''

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


# Build the parser

parser = yacc.yacc()
#while True:
#    try:
#       s = input('calc > ')
#    except EOFError:
#        break
#   if not s:
#        continue
#    result = parser.parse(s)
#    print(result)
