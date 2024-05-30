
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEMODULOrightPOWERleftCOMPARISONLESS_THANGREATER_THANGREATER_EQUALLESS_EQUALNOT_EQUALrightNOTleftANDORAND ARROW ASSIGN_OP BOOL COLON COMMA COMMENT_END COMMENT_START COMPARISON DIVIDE DOT DOUBLE ELSE FLOAT FOR FUNCTION GREATER_EQUAL GREATER_THAN IDENTIFIER IF IN INT LEFT_BRACE LEFT_BRACKET LEFT_PAREN LESS_EQUAL LESS_THAN MINUS MODULO NEWLINE NOT NOT_EQUAL OR PLUS POWER RETURN RIGHT_BRACE RIGHT_BRACKET RIGHT_PAREN SEMICOLON SPACE STRING TIMES TYPE_BOOL TYPE_DOUBLE TYPE_FLOAT TYPE_INTEGER TYPE_NULL TYPE_STRING TYPE_VOID WHILEF : LEFT_PAREN E RIGHT_PAREN\n         | IDENTIFIER\n         | INT\n         | FLOAT\n         | DOUBLE\n         | STRING\n         | BOOL\n         | NOT E\n         | E COMPARISON E\n         | E LESS_THAN E\n         | E GREATER_THAN E\n         | E LESS_EQUAL E\n         | E GREATER_EQUAL E\n         | E NOT_EQUAL E\n         | E AND E\n         | E OR EE : FE : E PLUS EE : E MINUS EE : E TIMES EE : E DIVIDE EE : E MODULO EE : E POWER EVD : IDENTIFIER COLON TD ASSIGN_OP ETD : TYPE_BOOL \n          | TYPE_DOUBLE\n          | TYPE_FLOAT\n          | TYPE_INTEGER\n          | TYPE_NULL\n          | TYPE_STRING\n          | TYPE_VOIDFD : FUNCTION IDENTIFIER LEFT_PAREN PL RIGHT_PAREN ARROW TD BS : E SEMICOLON\n         | IfS\n         | WS\n         | FS\n         | RS\n         | VD SEMICOLONB : LEFT_BRACKET SL RIGHT_BRACKETSL : S\n          | SL SPL : PL COMMA IDENTIFIER COLON TD\n          | IDENTIFIER COLON TDIfS : IF LEFT_PAREN E RIGHT_PAREN B\n           | IF LEFT_PAREN E RIGHT_PAREN B ELSE BWS : WHILE LEFT_PAREN E RIGHT_PAREN BFS : FOR IDENTIFIER IN IDENTIFIER LEFT_BRACKET SL RIGHT_BRACKETRS : RETURN E SEMICOLON'
    
_lr_action_items = {'LEFT_PAREN':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'IDENTIFIER':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'INT':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'FLOAT':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'DOUBLE':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'STRING':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'BOOL':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'NOT':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,4,5,6,7,8,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[0,-2,-3,-4,-5,-6,-7,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,-18,-19,-20,-21,-22,-23,]),'COMPARISON':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,13,-2,-3,-4,-5,-6,-7,13,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,13,13,13,13,13,13,]),'LESS_THAN':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,14,-2,-3,-4,-5,-6,-7,14,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,14,14,14,14,14,14,]),'GREATER_THAN':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,15,-2,-3,-4,-5,-6,-7,15,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,15,15,15,15,15,15,]),'LESS_EQUAL':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,16,-2,-3,-4,-5,-6,-7,16,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,16,16,16,16,16,16,]),'GREATER_EQUAL':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,17,-2,-3,-4,-5,-6,-7,17,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,17,17,17,17,17,17,]),'NOT_EQUAL':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,18,-2,-3,-4,-5,-6,-7,18,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,18,18,18,18,18,18,]),'AND':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,19,-2,-3,-4,-5,-6,-7,19,-17,19,-1,19,19,19,19,19,19,-15,-16,19,19,19,19,19,19,]),'OR':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,20,-2,-3,-4,-5,-6,-7,20,-17,20,-1,20,20,20,20,20,20,-15,-16,20,20,20,20,20,20,]),'PLUS':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,21,-2,-3,-4,-5,-6,-7,21,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,-18,-19,-20,-21,-22,-23,]),'MINUS':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,22,-2,-3,-4,-5,-6,-7,22,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,-18,-19,-20,-21,-22,-23,]),'TIMES':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,23,-2,-3,-4,-5,-6,-7,23,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,23,23,-20,-21,-22,-23,]),'DIVIDE':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,24,-2,-3,-4,-5,-6,-7,24,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,24,24,-20,-21,-22,-23,]),'MODULO':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,25,-2,-3,-4,-5,-6,-7,25,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,25,25,-20,-21,-22,-23,]),'POWER':([1,3,4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-17,26,-2,-3,-4,-5,-6,-7,26,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,26,26,26,26,26,26,]),'RIGHT_PAREN':([4,5,6,7,8,9,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-2,-3,-4,-5,-6,-7,28,-17,-8,-1,-9,-10,-11,-12,-13,-14,-15,-16,-18,-19,-20,-21,-22,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'F':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[1,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'E':([0,2,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[3,11,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> F","S'",1,None,None,None),
  ('F -> LEFT_PAREN E RIGHT_PAREN','F',3,'p_F','analizador_sintactico.py',22),
  ('F -> IDENTIFIER','F',1,'p_F','analizador_sintactico.py',23),
  ('F -> INT','F',1,'p_F','analizador_sintactico.py',24),
  ('F -> FLOAT','F',1,'p_F','analizador_sintactico.py',25),
  ('F -> DOUBLE','F',1,'p_F','analizador_sintactico.py',26),
  ('F -> STRING','F',1,'p_F','analizador_sintactico.py',27),
  ('F -> BOOL','F',1,'p_F','analizador_sintactico.py',28),
  ('F -> NOT E','F',2,'p_F','analizador_sintactico.py',29),
  ('F -> E COMPARISON E','F',3,'p_F','analizador_sintactico.py',30),
  ('F -> E LESS_THAN E','F',3,'p_F','analizador_sintactico.py',31),
  ('F -> E GREATER_THAN E','F',3,'p_F','analizador_sintactico.py',32),
  ('F -> E LESS_EQUAL E','F',3,'p_F','analizador_sintactico.py',33),
  ('F -> E GREATER_EQUAL E','F',3,'p_F','analizador_sintactico.py',34),
  ('F -> E NOT_EQUAL E','F',3,'p_F','analizador_sintactico.py',35),
  ('F -> E AND E','F',3,'p_F','analizador_sintactico.py',36),
  ('F -> E OR E','F',3,'p_F','analizador_sintactico.py',37),
  ('E -> F','E',1,'p_E','analizador_sintactico.py',66),
  ('E -> E PLUS E','E',3,'p_expression_plus','analizador_sintactico.py',70),
  ('E -> E MINUS E','E',3,'p_expression_minus','analizador_sintactico.py',74),
  ('E -> E TIMES E','E',3,'p_expression_times','analizador_sintactico.py',78),
  ('E -> E DIVIDE E','E',3,'p_expression_divide','analizador_sintactico.py',82),
  ('E -> E MODULO E','E',3,'p_expression_modulo','analizador_sintactico.py',86),
  ('E -> E POWER E','E',3,'p_expression_power','analizador_sintactico.py',90),
  ('VD -> IDENTIFIER COLON TD ASSIGN_OP E','VD',5,'p_VD','analizador_sintactico.py',94),
  ('TD -> TYPE_BOOL','TD',1,'p_TD','analizador_sintactico.py',99),
  ('TD -> TYPE_DOUBLE','TD',1,'p_TD','analizador_sintactico.py',100),
  ('TD -> TYPE_FLOAT','TD',1,'p_TD','analizador_sintactico.py',101),
  ('TD -> TYPE_INTEGER','TD',1,'p_TD','analizador_sintactico.py',102),
  ('TD -> TYPE_NULL','TD',1,'p_TD','analizador_sintactico.py',103),
  ('TD -> TYPE_STRING','TD',1,'p_TD','analizador_sintactico.py',104),
  ('TD -> TYPE_VOID','TD',1,'p_TD','analizador_sintactico.py',105),
  ('FD -> FUNCTION IDENTIFIER LEFT_PAREN PL RIGHT_PAREN ARROW TD B','FD',8,'p_FD','analizador_sintactico.py',109),
  ('S -> E SEMICOLON','S',2,'p_S','analizador_sintactico.py',114),
  ('S -> IfS','S',1,'p_S','analizador_sintactico.py',115),
  ('S -> WS','S',1,'p_S','analizador_sintactico.py',116),
  ('S -> FS','S',1,'p_S','analizador_sintactico.py',117),
  ('S -> RS','S',1,'p_S','analizador_sintactico.py',118),
  ('S -> VD SEMICOLON','S',2,'p_S','analizador_sintactico.py',119),
  ('B -> LEFT_BRACKET SL RIGHT_BRACKET','B',3,'p_B','analizador_sintactico.py',122),
  ('SL -> S','SL',1,'p_SL','analizador_sintactico.py',125),
  ('SL -> SL S','SL',2,'p_SL','analizador_sintactico.py',126),
  ('PL -> PL COMMA IDENTIFIER COLON TD','PL',5,'p_PL','analizador_sintactico.py',129),
  ('PL -> IDENTIFIER COLON TD','PL',3,'p_PL','analizador_sintactico.py',130),
  ('IfS -> IF LEFT_PAREN E RIGHT_PAREN B','IfS',5,'p_IfS','analizador_sintactico.py',133),
  ('IfS -> IF LEFT_PAREN E RIGHT_PAREN B ELSE B','IfS',7,'p_IfS','analizador_sintactico.py',134),
  ('WS -> WHILE LEFT_PAREN E RIGHT_PAREN B','WS',5,'p_WS','analizador_sintactico.py',137),
  ('FS -> FOR IDENTIFIER IN IDENTIFIER LEFT_BRACKET SL RIGHT_BRACKET','FS',7,'p_FS','analizador_sintactico.py',140),
  ('RS -> RETURN E SEMICOLON','RS',3,'p_RS','analizador_sintactico.py',143),
]
