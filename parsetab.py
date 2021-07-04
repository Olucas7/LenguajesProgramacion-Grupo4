
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ALERT AND ARRAY BREAK CASE CATCH CLASS CLEAR COLON COMMA CONST CONTINUE DEBUGGER DEFAULT DELETE DIVIDE DIV_EQUAL DO ELSE EQUAL EXPORT EXTENDS FALSE FINALLY FOR FUNCTION GREATER GREATEREQUAL HAS ID IF IMPORT IN INSTANCEOF ISEQUAL IS_IDENTICAL IS_NOT_IDENTICAL LBLOCK LBRACKET LENGTH LESS LESSEQUAL LET LPAREN MAP MINUS MINUS_EQUAL MOD MOD_EQUAL MUL_EQUAL NEW NOT NUM OR PERIOD PLUS PLUS_EQUAL POP PRINT PUSH RBLOCK RBRACKET RETURN RPAREN SET STRING SWITCH THIS THROW TIMES TRUE TRY TWOPOINTS TYPEOF UNSHIFT VAR WHILE WITH YIELD sentencia :  callMethods\n                    | varType ID EQUAL callMethods\n                    | callFunction\n                    | javaScript_param\n                    | varDeclaration\n                    | controlExpression\n                    | impresion\n                    | operacionesMath\n                    | declareteFunction\n\n                     expression :  ID opConditional ID\n                     | ID opConditional NUM\n                     | NUM opConditional NUM\n                     | operacionesMath\n\n    controlExpression : sentencias_if\n                        | sentencias_if_else\n                        | sentencias_while\n                        | impresion\n                        | impresion_vacio\n             opConditional : ISEQUAL\n                      |  IS_NOT_IDENTICAL\n                      |  IS_IDENTICAL\n                      | GREATER\n                      | GREATEREQUAL\n                      | LESS\n                      | LESSEQUAL\n                      operadorLogical : AND\n                        | OR\n                        | NOT sentencias_if : IF LPAREN expression operadorLogical expression  RPAREN LBLOCK sentencia RBLOCK\n                    | IF LPAREN expression RPAREN LBLOCK sentencia RBLOCKsentencias_if_else : IF LPAREN expression operadorLogical expression  RPAREN LBLOCK sentencia RBLOCK ELSE LBLOCK sentencia RBLOCK\n                          | IF LPAREN expression RPAREN LBLOCK sentencia RBLOCK ELSE LBLOCK sentencia RBLOCK sentencias_while : WHILE LPAREN  expression RPAREN LBLOCK sentencia RBLOCK\n                        | WHILE LPAREN  expression operadorLogical expression RPAREN LBLOCK sentencia RBLOCKimpresion : ALERT LPAREN expression  RPARENimpresion_vacio : ALERT LPAREN RPARENjavaScript_param : STRING\n                         | NUM\n                         | boolean\n                         | ID\n    empty : boolean : TRUE\n             | FALSE\n         varType : LET\n                | CONST\n                | VAR\n                 | empty varDeclaration : varType ID  EQUAL  arrayDeclare COLON\n                    |   varType ID EQUAL declareMap COLON\n                    |   varType ID EQUAL declararSet COLON callMethods : ID methodArray COLON\n                     | ID methodSet COLON\n                     | ID methodMap COLONarrayDeclare :  LBRACKET arrayValues RBRACKET\n                       | NEW ARRAY LPAREN arrayValues RPAREN\n                     arrayValues :  arrayValue\n                    | arrayValue COMMA arrayValue arrayValue :  LPAREN expression RPAREN\n                      | ID\n                      | NUM\n                      | STRING\n                      | boolean\n                      | empty  methodArray : PERIOD PUSH LPAREN arrayValue RPAREN\n                      | PERIOD UNSHIFT LPAREN arrayValue RPAREN\n                      | PERIOD POP LPAREN empty RPAREN declareMap :  NEW MAP LPAREN iterable RPAREN\n                    iterable  : arrayDeclare\n                   | declararSet\n                   | empty methodMap : PERIOD CLEAR LPAREN RPAREN\n                   | PERIOD LENGTH LPAREN RPAREN  declareteFunction : FUNCTION ID LPAREN params RPAREN\n                          | FUNCTION  ID LPAREN params RPAREN sentencesCmpt\n                          | varType ID EQUAL FUNCTION LPAREN params RPAREN\n                          sentencesCmpt : LBLOCK sentencia RBLOCK\n                     | LBLOCK sentencia RETURN RBLOCK  callFunction : ID LPAREN params RPAREN  \n                    \n                     params : paramList\n               | empty   param : ID\n              | ID LBRACKET RBRACKET\n               paramList : param\n                  | param COMMA paramList  args : argslist\n            | empty\n            | javaScript_param\n     argslist : args\n                   | args COMMA argslist\n    declararSet : NEW SET LPAREN setValues RPARENcontiene : ID PERIOD HAS LPAREN params RPARENsetValues :  setValue\n                    | setValue COMMA setValue setValue : ID\n                 | NUM\n                 | STRING\n                 | boolean\n                 | empty  methodSet : PERIOD ADD LPAREN setValue RPAREN\n                      | PERIOD DELETE LPAREN setValue RPAREN\n                      | PERIOD CLEAR LPAREN empty RPAREN  operacionesMath :  sumas\n                          | sumas operacionesMath\n                         | restas\n                         | restas operacionesMathsumas : numOperadores PLUS LPAREN numOperadores RPAREN\n            | numOperadores PLUS NUM\n             numOperadores : enteros\n                     |  decimales   enteros : NUM\n                 | numNegative numNegative : MINUS NUM\n                 | decimales : enteros PERIOD NUM   restas : numOperadores MINUS LPAREN numOperadores RPAREN\n               | numOperadores  MINUS NUM '
    
_lr_action_items = {'ID':([0,3,12,13,14,15,26,40,42,47,48,53,74,88,92,93,94,96,97,101,102,103,104,105,106,107,108,111,113,114,115,117,123,126,155,156,162,164,166,174,191,194,198,207,211,],[4,36,-44,-45,-46,-47,46,57,71,71,71,82,57,127,57,127,127,141,141,150,-19,-20,-21,-22,-23,-24,-25,71,-26,-27,-28,71,57,71,4,4,127,127,141,4,4,4,141,4,4,]),'LET':([0,155,156,174,191,194,207,211,],[12,12,12,12,12,12,12,12,]),'CONST':([0,155,156,174,191,194,207,211,],[13,13,13,13,13,13,13,13,]),'VAR':([0,155,156,174,191,194,207,211,],[14,14,14,14,14,14,14,14,]),'STRING':([0,88,93,94,96,97,155,156,162,164,166,174,191,194,198,207,211,],[16,129,129,129,143,143,16,16,129,129,143,16,16,16,143,16,16,]),'NUM':([0,24,25,32,42,47,48,49,50,52,77,78,79,80,88,93,94,96,97,101,102,103,104,105,106,107,108,109,111,113,114,115,117,126,155,156,158,159,162,164,166,174,191,194,198,207,211,],[17,44,44,51,72,72,72,78,80,81,44,-107,44,-116,128,128,128,142,142,151,-19,-20,-21,-22,-23,-24,-25,152,72,-26,-27,-28,72,72,17,17,-106,-115,128,128,142,17,17,17,142,17,17,]),'ALERT':([0,155,156,174,191,194,207,211,],[23,23,23,23,23,23,23,23,]),'FUNCTION':([0,53,155,156,174,191,194,207,211,],[26,87,26,26,26,26,26,26,26,]),'TRUE':([0,88,93,94,96,97,155,156,162,164,166,174,191,194,198,207,211,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'FALSE':([0,88,93,94,96,97,155,156,162,164,166,174,191,194,198,207,211,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'IF':([0,155,156,174,191,194,207,211,],[29,29,29,29,29,29,29,29,]),'WHILE':([0,155,156,174,191,194,207,211,],[30,30,30,30,30,30,30,30,]),'MINUS':([0,17,24,25,31,33,34,35,42,44,47,48,51,72,77,78,79,80,81,111,113,114,115,117,126,155,156,158,159,174,191,194,207,211,],[32,-110,32,32,50,-108,-109,-111,32,-110,32,32,-112,-110,32,-107,32,-116,-114,32,-26,-27,-28,32,32,32,32,-106,-115,32,32,32,32,32,]),'PERIOD':([0,4,17,24,25,33,35,42,44,47,48,51,72,77,78,79,80,82,111,113,114,115,117,126,155,156,158,159,174,191,194,207,211,],[-113,41,-110,-113,-113,52,-111,-113,-110,-113,-113,-112,-110,-113,-107,-113,-116,41,-113,-26,-27,-28,-113,-113,-113,-113,-106,-115,-113,-113,-113,-113,-113,]),'PLUS':([0,17,24,25,31,33,34,35,42,44,47,48,51,72,78,80,81,111,113,114,115,117,126,155,156,158,159,174,191,194,207,211,],[-113,-110,-113,-113,49,-108,-109,-111,-113,-110,-113,-113,-112,-110,-107,-116,-114,-113,-26,-27,-28,-113,-113,-113,-113,-106,-115,-113,-113,-113,-113,-113,]),'$end':([1,2,4,5,6,7,8,9,10,11,16,17,18,19,20,21,22,24,25,27,28,43,45,54,55,56,70,78,80,83,91,100,120,121,122,153,158,159,173,179,192,193,199,205,206,208,212,214,],[0,-1,-40,-3,-4,-5,-6,-7,-8,-9,-37,-38,-39,-14,-15,-16,-18,-102,-104,-42,-43,-103,-105,-51,-52,-53,-36,-107,-116,-2,-78,-35,-48,-49,-50,-73,-106,-115,-74,-75,-30,-33,-76,-77,-29,-34,-32,-31,]),'RBLOCK':([2,4,5,6,7,8,9,10,11,16,17,18,19,20,21,22,24,25,27,28,43,45,54,55,56,70,78,80,83,91,100,120,121,122,153,158,159,173,176,177,179,190,192,193,199,200,201,203,205,206,208,210,212,213,214,],[-1,-40,-3,-4,-5,-6,-7,-8,-9,-37,-38,-39,-14,-15,-16,-18,-102,-104,-42,-43,-103,-105,-51,-52,-53,-36,-107,-116,-2,-78,-35,-48,-49,-50,-73,-106,-115,-74,192,193,-75,199,-30,-33,-76,205,206,208,-77,-29,-34,212,-32,214,-31,]),'RETURN':([2,4,5,6,7,8,9,10,11,16,17,18,19,20,21,22,24,25,27,28,43,45,54,55,56,70,78,80,83,91,100,120,121,122,153,158,159,173,179,190,192,193,199,205,206,208,212,214,],[-1,-40,-3,-4,-5,-6,-7,-8,-9,-37,-38,-39,-14,-15,-16,-18,-102,-104,-42,-43,-103,-105,-51,-52,-53,-36,-107,-116,-2,-78,-35,-48,-49,-50,-73,-106,-115,-74,-75,200,-30,-33,-76,-77,-29,-34,-32,-31,]),'LPAREN':([4,23,29,30,46,49,50,62,63,64,65,66,67,68,87,88,93,94,132,133,134,162,164,],[40,42,47,48,74,77,79,93,94,95,96,97,98,99,123,126,126,126,164,165,166,126,126,]),'RPAREN':([24,25,27,28,33,34,35,40,42,43,44,45,51,57,58,59,60,61,69,73,74,75,76,77,78,79,80,81,93,94,95,96,97,98,99,110,118,119,123,125,127,128,129,130,131,135,136,137,138,139,140,141,142,143,144,145,146,147,150,151,152,154,157,158,159,160,161,162,163,164,165,166,180,181,182,184,185,186,187,188,189,195,197,198,204,],[-102,-104,-42,-43,-108,-109,-111,-41,70,-103,-110,-105,-112,-81,91,-79,-80,-83,100,-13,-41,112,116,-113,-107,-113,-116,-114,-41,-41,-41,-41,-41,148,149,153,158,159,-41,-56,-59,-60,-61,-62,-63,-82,-84,167,168,169,170,-94,-95,-96,-97,-98,171,172,-10,-11,-12,175,178,-106,-115,179,-54,-41,181,-41,-41,-41,-57,-58,195,196,-68,-69,-70,197,-92,-55,-90,-41,-93,]),'AND':([24,25,43,45,73,75,76,78,80,150,151,152,158,159,],[-102,-104,-103,-105,-13,113,113,-107,-116,-10,-11,-12,-106,-115,]),'OR':([24,25,43,45,73,75,76,78,80,150,151,152,158,159,],[-102,-104,-103,-105,-13,114,114,-107,-116,-10,-11,-12,-106,-115,]),'NOT':([24,25,43,45,73,75,76,78,80,150,151,152,158,159,],[-102,-104,-103,-105,-13,115,115,-107,-116,-10,-11,-12,-106,-115,]),'COMMA':([27,28,57,61,88,125,127,128,129,130,131,135,141,142,143,144,145,164,166,181,189,],[-42,-43,-81,92,-41,162,-59,-60,-61,-62,-63,-82,-94,-95,-96,-97,-98,-41,-41,-58,198,]),'RBRACKET':([27,28,88,90,124,125,127,128,129,130,131,162,180,181,],[-42,-43,-41,135,161,-56,-59,-60,-61,-62,-63,-41,-57,-58,]),'EQUAL':([36,],[53,]),'COLON':([37,38,39,84,85,86,148,149,161,167,168,169,170,171,172,195,196,197,],[54,55,56,120,121,122,-71,-72,-54,-64,-65,-66,-99,-100,-101,-55,-67,-90,]),'PUSH':([41,],[62,]),'UNSHIFT':([41,],[63,]),'POP':([41,],[64,]),'ADD':([41,],[65,]),'DELETE':([41,],[66,]),'CLEAR':([41,],[67,]),'LENGTH':([41,],[68,]),'LBRACKET':([53,57,165,],[88,90,88,]),'NEW':([53,165,],[89,183,]),'ISEQUAL':([71,72,],[102,102,]),'IS_NOT_IDENTICAL':([71,72,],[103,103,]),'IS_IDENTICAL':([71,72,],[104,104,]),'GREATER':([71,72,],[105,105,]),'GREATEREQUAL':([71,72,],[106,106,]),'LESS':([71,72,],[107,107,]),'LESSEQUAL':([71,72,],[108,108,]),'ARRAY':([89,183,],[132,132,]),'MAP':([89,],[133,]),'SET':([89,183,],[134,134,]),'LBLOCK':([112,116,153,175,178,202,209,],[155,156,174,191,194,207,211,]),'ELSE':([192,206,],[202,209,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia':([0,155,156,174,191,194,207,211,],[1,176,177,190,201,203,210,213,]),'callMethods':([0,53,155,156,174,191,194,207,211,],[2,83,2,2,2,2,2,2,2,]),'varType':([0,155,156,174,191,194,207,211,],[3,3,3,3,3,3,3,3,]),'callFunction':([0,155,156,174,191,194,207,211,],[5,5,5,5,5,5,5,5,]),'javaScript_param':([0,155,156,174,191,194,207,211,],[6,6,6,6,6,6,6,6,]),'varDeclaration':([0,155,156,174,191,194,207,211,],[7,7,7,7,7,7,7,7,]),'controlExpression':([0,155,156,174,191,194,207,211,],[8,8,8,8,8,8,8,8,]),'impresion':([0,155,156,174,191,194,207,211,],[9,9,9,9,9,9,9,9,]),'operacionesMath':([0,24,25,42,47,48,111,117,126,155,156,174,191,194,207,211,],[10,43,45,73,73,73,73,73,73,10,10,10,10,10,10,10,]),'declareteFunction':([0,155,156,174,191,194,207,211,],[11,11,11,11,11,11,11,11,]),'empty':([0,40,74,88,93,94,95,96,97,98,123,155,156,162,164,165,166,174,191,194,198,207,211,],[15,60,60,131,131,131,139,145,145,147,60,15,15,131,131,187,145,15,15,15,145,15,15,]),'boolean':([0,88,93,94,96,97,155,156,162,164,166,174,191,194,198,207,211,],[18,130,130,130,144,144,18,18,130,130,144,18,18,18,144,18,18,]),'sentencias_if':([0,155,156,174,191,194,207,211,],[19,19,19,19,19,19,19,19,]),'sentencias_if_else':([0,155,156,174,191,194,207,211,],[20,20,20,20,20,20,20,20,]),'sentencias_while':([0,155,156,174,191,194,207,211,],[21,21,21,21,21,21,21,21,]),'impresion_vacio':([0,155,156,174,191,194,207,211,],[22,22,22,22,22,22,22,22,]),'sumas':([0,24,25,42,47,48,111,117,126,155,156,174,191,194,207,211,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'restas':([0,24,25,42,47,48,111,117,126,155,156,174,191,194,207,211,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'numOperadores':([0,24,25,42,47,48,77,79,111,117,126,155,156,174,191,194,207,211,],[31,31,31,31,31,31,118,119,31,31,31,31,31,31,31,31,31,31,]),'enteros':([0,24,25,42,47,48,77,79,111,117,126,155,156,174,191,194,207,211,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'decimales':([0,24,25,42,47,48,77,79,111,117,126,155,156,174,191,194,207,211,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'numNegative':([0,24,25,42,47,48,77,79,111,117,126,155,156,174,191,194,207,211,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'methodArray':([4,82,],[37,37,]),'methodSet':([4,82,],[38,38,]),'methodMap':([4,82,],[39,39,]),'params':([40,74,123,],[58,110,160,]),'paramList':([40,74,92,123,],[59,59,136,59,]),'param':([40,74,92,123,],[61,61,61,61,]),'expression':([42,47,48,111,117,126,],[69,75,76,154,157,163,]),'arrayDeclare':([53,165,],[84,185,]),'declareMap':([53,],[85,]),'declararSet':([53,165,],[86,186,]),'opConditional':([71,72,],[101,109,]),'operadorLogical':([75,76,],[111,117,]),'arrayValues':([88,164,],[124,182,]),'arrayValue':([88,93,94,162,164,],[125,137,138,180,125,]),'setValue':([96,97,166,198,],[140,146,189,204,]),'sentencesCmpt':([153,],[173,]),'iterable':([165,],[184,]),'setValues':([166,],[188,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencia","S'",1,None,None,None),
  ('sentencia -> callMethods','sentencia',1,'p_sentencia','analisisSintactico.py',6),
  ('sentencia -> varType ID EQUAL callMethods','sentencia',4,'p_sentencia','analisisSintactico.py',7),
  ('sentencia -> callFunction','sentencia',1,'p_sentencia','analisisSintactico.py',8),
  ('sentencia -> javaScript_param','sentencia',1,'p_sentencia','analisisSintactico.py',9),
  ('sentencia -> varDeclaration','sentencia',1,'p_sentencia','analisisSintactico.py',10),
  ('sentencia -> controlExpression','sentencia',1,'p_sentencia','analisisSintactico.py',11),
  ('sentencia -> impresion','sentencia',1,'p_sentencia','analisisSintactico.py',12),
  ('sentencia -> operacionesMath','sentencia',1,'p_sentencia','analisisSintactico.py',13),
  ('sentencia -> declareteFunction','sentencia',1,'p_sentencia','analisisSintactico.py',14),
  ('expression -> ID opConditional ID','expression',3,'p_expression','analisisSintactico.py',18),
  ('expression -> ID opConditional NUM','expression',3,'p_expression','analisisSintactico.py',19),
  ('expression -> NUM opConditional NUM','expression',3,'p_expression','analisisSintactico.py',20),
  ('expression -> operacionesMath','expression',1,'p_expression','analisisSintactico.py',21),
  ('controlExpression -> sentencias_if','controlExpression',1,'p_controlExpression','analisisSintactico.py',27),
  ('controlExpression -> sentencias_if_else','controlExpression',1,'p_controlExpression','analisisSintactico.py',28),
  ('controlExpression -> sentencias_while','controlExpression',1,'p_controlExpression','analisisSintactico.py',29),
  ('controlExpression -> impresion','controlExpression',1,'p_controlExpression','analisisSintactico.py',30),
  ('controlExpression -> impresion_vacio','controlExpression',1,'p_controlExpression','analisisSintactico.py',31),
  ('opConditional -> ISEQUAL','opConditional',1,'p_opConditional','analisisSintactico.py',36),
  ('opConditional -> IS_NOT_IDENTICAL','opConditional',1,'p_opConditional','analisisSintactico.py',37),
  ('opConditional -> IS_IDENTICAL','opConditional',1,'p_opConditional','analisisSintactico.py',38),
  ('opConditional -> GREATER','opConditional',1,'p_opConditional','analisisSintactico.py',39),
  ('opConditional -> GREATEREQUAL','opConditional',1,'p_opConditional','analisisSintactico.py',40),
  ('opConditional -> LESS','opConditional',1,'p_opConditional','analisisSintactico.py',41),
  ('opConditional -> LESSEQUAL','opConditional',1,'p_opConditional','analisisSintactico.py',42),
  ('operadorLogical -> AND','operadorLogical',1,'p_operadorLogical','analisisSintactico.py',45),
  ('operadorLogical -> OR','operadorLogical',1,'p_operadorLogical','analisisSintactico.py',46),
  ('operadorLogical -> NOT','operadorLogical',1,'p_operadorLogical','analisisSintactico.py',47),
  ('sentencias_if -> IF LPAREN expression operadorLogical expression RPAREN LBLOCK sentencia RBLOCK','sentencias_if',9,'p_sentencias_if','analisisSintactico.py',51),
  ('sentencias_if -> IF LPAREN expression RPAREN LBLOCK sentencia RBLOCK','sentencias_if',7,'p_sentencias_if','analisisSintactico.py',52),
  ('sentencias_if_else -> IF LPAREN expression operadorLogical expression RPAREN LBLOCK sentencia RBLOCK ELSE LBLOCK sentencia RBLOCK','sentencias_if_else',13,'p_sentencias_if_else','analisisSintactico.py',55),
  ('sentencias_if_else -> IF LPAREN expression RPAREN LBLOCK sentencia RBLOCK ELSE LBLOCK sentencia RBLOCK','sentencias_if_else',11,'p_sentencias_if_else','analisisSintactico.py',56),
  ('sentencias_while -> WHILE LPAREN expression RPAREN LBLOCK sentencia RBLOCK','sentencias_while',7,'p_sentencias_while','analisisSintactico.py',59),
  ('sentencias_while -> WHILE LPAREN expression operadorLogical expression RPAREN LBLOCK sentencia RBLOCK','sentencias_while',9,'p_sentencias_while','analisisSintactico.py',60),
  ('impresion -> ALERT LPAREN expression RPAREN','impresion',4,'p_impresion','analisisSintactico.py',63),
  ('impresion_vacio -> ALERT LPAREN RPAREN','impresion_vacio',3,'p_impresion_vacio','analisisSintactico.py',65),
  ('javaScript_param -> STRING','javaScript_param',1,'p_javaScript_param','analisisSintactico.py',80),
  ('javaScript_param -> NUM','javaScript_param',1,'p_javaScript_param','analisisSintactico.py',81),
  ('javaScript_param -> boolean','javaScript_param',1,'p_javaScript_param','analisisSintactico.py',82),
  ('javaScript_param -> ID','javaScript_param',1,'p_javaScript_param','analisisSintactico.py',83),
  ('empty -> <empty>','empty',0,'p_empty','analisisSintactico.py',90),
  ('boolean -> TRUE','boolean',1,'p_boolean','analisisSintactico.py',95),
  ('boolean -> FALSE','boolean',1,'p_boolean','analisisSintactico.py',96),
  ('varType -> LET','varType',1,'p_varType','analisisSintactico.py',101),
  ('varType -> CONST','varType',1,'p_varType','analisisSintactico.py',102),
  ('varType -> VAR','varType',1,'p_varType','analisisSintactico.py',103),
  ('varType -> empty','varType',1,'p_varType','analisisSintactico.py',104),
  ('varDeclaration -> varType ID EQUAL arrayDeclare COLON','varDeclaration',5,'p_varDeclaration','analisisSintactico.py',108),
  ('varDeclaration -> varType ID EQUAL declareMap COLON','varDeclaration',5,'p_varDeclaration','analisisSintactico.py',109),
  ('varDeclaration -> varType ID EQUAL declararSet COLON','varDeclaration',5,'p_varDeclaration','analisisSintactico.py',110),
  ('callMethods -> ID methodArray COLON','callMethods',3,'p_callMethods','analisisSintactico.py',115),
  ('callMethods -> ID methodSet COLON','callMethods',3,'p_callMethods','analisisSintactico.py',116),
  ('callMethods -> ID methodMap COLON','callMethods',3,'p_callMethods','analisisSintactico.py',117),
  ('arrayDeclare -> LBRACKET arrayValues RBRACKET','arrayDeclare',3,'p_arrayDeclare','analisisSintactico.py',122),
  ('arrayDeclare -> NEW ARRAY LPAREN arrayValues RPAREN','arrayDeclare',5,'p_arrayDeclare','analisisSintactico.py',123),
  ('arrayValues -> arrayValue','arrayValues',1,'p_arrayValues','analisisSintactico.py',128),
  ('arrayValues -> arrayValue COMMA arrayValue','arrayValues',3,'p_arrayValues','analisisSintactico.py',129),
  ('arrayValue -> LPAREN expression RPAREN','arrayValue',3,'p_arrayValue','analisisSintactico.py',133),
  ('arrayValue -> ID','arrayValue',1,'p_arrayValue','analisisSintactico.py',134),
  ('arrayValue -> NUM','arrayValue',1,'p_arrayValue','analisisSintactico.py',135),
  ('arrayValue -> STRING','arrayValue',1,'p_arrayValue','analisisSintactico.py',136),
  ('arrayValue -> boolean','arrayValue',1,'p_arrayValue','analisisSintactico.py',137),
  ('arrayValue -> empty','arrayValue',1,'p_arrayValue','analisisSintactico.py',138),
  ('methodArray -> PERIOD PUSH LPAREN arrayValue RPAREN','methodArray',5,'p_methodArray','analisisSintactico.py',141),
  ('methodArray -> PERIOD UNSHIFT LPAREN arrayValue RPAREN','methodArray',5,'p_methodArray','analisisSintactico.py',142),
  ('methodArray -> PERIOD POP LPAREN empty RPAREN','methodArray',5,'p_methodArray','analisisSintactico.py',143),
  ('declareMap -> NEW MAP LPAREN iterable RPAREN','declareMap',5,'p_declareMap','analisisSintactico.py',147),
  ('iterable -> arrayDeclare','iterable',1,'p_iterable','analisisSintactico.py',151),
  ('iterable -> declararSet','iterable',1,'p_iterable','analisisSintactico.py',152),
  ('iterable -> empty','iterable',1,'p_iterable','analisisSintactico.py',153),
  ('methodMap -> PERIOD CLEAR LPAREN RPAREN','methodMap',4,'p_methodMap','analisisSintactico.py',156),
  ('methodMap -> PERIOD LENGTH LPAREN RPAREN','methodMap',4,'p_methodMap','analisisSintactico.py',157),
  ('declareteFunction -> FUNCTION ID LPAREN params RPAREN','declareteFunction',5,'p_declareteFunction','analisisSintactico.py',162),
  ('declareteFunction -> FUNCTION ID LPAREN params RPAREN sentencesCmpt','declareteFunction',6,'p_declareteFunction','analisisSintactico.py',163),
  ('declareteFunction -> varType ID EQUAL FUNCTION LPAREN params RPAREN','declareteFunction',7,'p_declareteFunction','analisisSintactico.py',164),
  ('sentencesCmpt -> LBLOCK sentencia RBLOCK','sentencesCmpt',3,'p_sentencesCmpt','analisisSintactico.py',169),
  ('sentencesCmpt -> LBLOCK sentencia RETURN RBLOCK','sentencesCmpt',4,'p_sentencesCmpt','analisisSintactico.py',170),
  ('callFunction -> ID LPAREN params RPAREN','callFunction',4,'p_callFunction','analisisSintactico.py',175),
  ('params -> paramList','params',1,'p_params','analisisSintactico.py',181),
  ('params -> empty','params',1,'p_params','analisisSintactico.py',182),
  ('param -> ID','param',1,'p_param','analisisSintactico.py',186),
  ('param -> ID LBRACKET RBRACKET','param',3,'p_param','analisisSintactico.py',187),
  ('paramList -> param','paramList',1,'p_paramList','analisisSintactico.py',191),
  ('paramList -> param COMMA paramList','paramList',3,'p_paramList','analisisSintactico.py',192),
  ('args -> argslist','args',1,'p_args','analisisSintactico.py',198),
  ('args -> empty','args',1,'p_args','analisisSintactico.py',199),
  ('args -> javaScript_param','args',1,'p_args','analisisSintactico.py',200),
  ('argslist -> args','argslist',1,'p_argslist','analisisSintactico.py',204),
  ('argslist -> args COMMA argslist','argslist',3,'p_argslist','analisisSintactico.py',205),
  ('declararSet -> NEW SET LPAREN setValues RPAREN','declararSet',5,'p_declararSet','analisisSintactico.py',214),
  ('contiene -> ID PERIOD HAS LPAREN params RPAREN','contiene',6,'p_contiene','analisisSintactico.py',218),
  ('setValues -> setValue','setValues',1,'p_setValues','analisisSintactico.py',222),
  ('setValues -> setValue COMMA setValue','setValues',3,'p_setValues','analisisSintactico.py',223),
  ('setValue -> ID','setValue',1,'p_setValue','analisisSintactico.py',227),
  ('setValue -> NUM','setValue',1,'p_setValue','analisisSintactico.py',228),
  ('setValue -> STRING','setValue',1,'p_setValue','analisisSintactico.py',229),
  ('setValue -> boolean','setValue',1,'p_setValue','analisisSintactico.py',230),
  ('setValue -> empty','setValue',1,'p_setValue','analisisSintactico.py',231),
  ('methodSet -> PERIOD ADD LPAREN setValue RPAREN','methodSet',5,'p_methodSet','analisisSintactico.py',235),
  ('methodSet -> PERIOD DELETE LPAREN setValue RPAREN','methodSet',5,'p_methodSet','analisisSintactico.py',236),
  ('methodSet -> PERIOD CLEAR LPAREN empty RPAREN','methodSet',5,'p_methodSet','analisisSintactico.py',237),
  ('operacionesMath -> sumas','operacionesMath',1,'p_operacionesMath','analisisSintactico.py',244),
  ('operacionesMath -> sumas operacionesMath','operacionesMath',2,'p_operacionesMath','analisisSintactico.py',245),
  ('operacionesMath -> restas','operacionesMath',1,'p_operacionesMath','analisisSintactico.py',246),
  ('operacionesMath -> restas operacionesMath','operacionesMath',2,'p_operacionesMath','analisisSintactico.py',247),
  ('sumas -> numOperadores PLUS LPAREN numOperadores RPAREN','sumas',5,'p_sumas','analisisSintactico.py',250),
  ('sumas -> numOperadores PLUS NUM','sumas',3,'p_sumas','analisisSintactico.py',251),
  ('numOperadores -> enteros','numOperadores',1,'p_numOperadores','analisisSintactico.py',255),
  ('numOperadores -> decimales','numOperadores',1,'p_numOperadores','analisisSintactico.py',256),
  ('enteros -> NUM','enteros',1,'p_enteros','analisisSintactico.py',259),
  ('enteros -> numNegative','enteros',1,'p_enteros','analisisSintactico.py',260),
  ('numNegative -> MINUS NUM','numNegative',2,'p_numNegative','analisisSintactico.py',263),
  ('numNegative -> <empty>','numNegative',0,'p_numNegative','analisisSintactico.py',264),
  ('decimales -> enteros PERIOD NUM','decimales',3,'p_decimales','analisisSintactico.py',267),
  ('restas -> numOperadores MINUS LPAREN numOperadores RPAREN','restas',5,'p_restas','analisisSintactico.py',270),
  ('restas -> numOperadores MINUS NUM','restas',3,'p_restas','analisisSintactico.py',271),
]
