grammar brownie_grammar;
//options{language = Python3;}

//----------------------REGLAS LEXICAS -------------------------------------------->
//Palabras reservadas
IF   : 'if';
ELIF : 'elif';
ELSE : 'else';

SWITCH : 'switch';
CASE : 'case';

WHILE : 'while';
FOR : 'for';
DO : 'do';

TRUE : 'True';
FALSE : 'False';
BREAK : 'break';

FUNCTION : 'fun';
RETURN : 'return';
THREAD : 'thread';

//Tipos de datos
NUMBER : [-]?[0-9]+ | [-]?[0-9]+('.'[0-9]+)  ;
STRING : '"' .*? '"';
VARIABLE : [a-zA-Z][a-zA-Z0-9_]*;

//Parentizacion
OP_SQUARE : '[';
OP_BRACE :'{';
OP_PARENTHESIS : '(';
CL_SQUARE : ']';
CL_BRACE :'}';
CL_PARENTHESIS : ')';
COMMA : ',';
DOT : '.';
COLON : ':';
SEMICOLON : ';';
//Operadores algebraicos
PLUS : '+';
MINUS : '-';
MUL : '*';
DIV : '/';
POW : '^';
//Operadores logicos
AND : '&&';
OR : '||';
NOT : '!';
//Operadores de comparacion
EQ : '==';
DIF : '!=';
GREATER : '>';
LESS : '<';
GEQ : '>=';
LEQ : '<=';
//Asignacion
ASSIGN : '=';
//Comentarios
COMMENT_LINE : '#';
COMM_OPEN : '/*';
COMM_CLOSE : '*/';


WHITESPACE : [ \t\n] -> skip;

//-------------------------------GRAMATICA------------------------------------->
start : structure* | 'EOF';

structure : function | sentence  | call;
//Cualquier instruccion
sentence : definition | conditional | call_sentence ;
//Definicion de funciones
function : FUNCTION VARIABLE OP_PARENTHESIS parameter CL_PARENTHESIS fun_body;
//Llamado de una funcion
call :  VARIABLE OP_PARENTHESIS parameter_call CL_PARENTHESIS;
call_sentence : call SEMICOLON;
//Parametros
parameter : VARIABLE | parameter ',' parameter;
parameter_call : VARIABLE* |NUMBER | STRING | call | parameter ',' parameter;

//Definicion y asignacion de variables
definition : VARIABLE ASSIGN exp SEMICOLON;
//Expresion matematica
exp : ar_value ar_operator exp | ar_value;
ar_value : NUMBER | VARIABLE | call ;
//Operadores aritmeticos
ar_operator : PLUS | MINUS | MUL | DIV | POW;

//Estructura condicional
conditional : IF OP_PARENTHESIS condition CL_PARENTHESIS  body otherwise*;
otherwise : ELIF OP_PARENTHESIS condition CL_PARENTHESIS  body | ELSE body ;
condition : com_value comparator com_value (logic condition)* | TRUE | FALSE ;
com_value : NUMBER | VARIABLE | STRING | | TRUE | FALSE | call;
comparator : EQ | DIF | GREATER | LESS | GEQ | LEQ ;

//Cuerpo de instrucciones
body : OP_BRACE sentence* CL_BRACE;
fun_body : OP_BRACE fun_sentence* CL_BRACE ;
fun_sentence : sentence | RETURN exp SEMICOLON;


//Array de objetos
element : NUMBER | STRING | element ',' element;
list_elements: OP_SQUARE element? CL_SQUARE;
//Operadores
logic : AND | OR ;
test : NUMBER*;