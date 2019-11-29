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
IN : 'in';

//Concurrencia
PROCESS : 'process';
LOOP : 'loop';
EXEC : 'exec';
START : 'start';
STOP : 'stop';
MESSAGE : 'message';


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
MOD : '%';
INCREMENT : '++';
DECREMENT : '--';
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
//Control
MONITOR :'?';
CONNECTION :'@';

WHITESPACE : [ \t\n] -> skip;

//-------------------------------GRAMATICA------------------------------------->
start : structure+  EOF;

structure : function | sentence  | call_sentence | process;
//Cualquier instruccion
sentence : definition | conditional | call_sentence | cycle | concurrency;

//Definicion de funciones
function : FUNCTION VARIABLE OP_PARENTHESIS parameter? CL_PARENTHESIS fun_body;
//Llamado de una funcion
call :  VARIABLE OP_PARENTHESIS parameter_call? CL_PARENTHESIS;
call_sentence : call SEMICOLON;
//Parametros
parameter : VARIABLE | parameter ',' parameter;
parameter_call : VARIABLE | NUMBER | STRING | call | parameter_call ',' parameter_call;

//Definicion y asignacion de variables
definition : assign SEMICOLON ;
assign :  VARIABLE ASSIGN exp | VARIABLE INCREMENT | VARIABLE DECREMENT ;
//Expresion matematica
exp : ar_value ar_operator exp | ar_value | list_elements;
ar_value : NUMBER | VARIABLE | call ;
//Operadores aritmeticos
ar_operator : PLUS | MINUS | MUL | DIV | POW | MOD;

//Estructura condicional
conditional : IF  condition COLON  body otherwise*;
otherwise : ELIF  condition COLON  body | ELSE body ;
condition : com_value comparator com_value (logic condition)* | TRUE | FALSE ;
com_value : NUMBER | VARIABLE | STRING | | TRUE | FALSE | call;
comparator : EQ | DIF | GREATER | LESS | GEQ | LEQ ;

//Ciclos repetitivos
cycle : while_ | for_;
while_ : (DO body)? WHILE condition COLON body ;
for_ : FOR for_condition COLON body;
for_condition : for_definition SEMICOLON condition SEMICOLON assign | for_iterator;
for_definition :  VARIABLE ASSIGN exp ;
for_iterator : VARIABLE IN VARIABLE;

//Cuerpo de instrucciones
body : OP_BRACE sentence* CL_BRACE;
fun_body : OP_BRACE fun_sentence* CL_BRACE ;
fun_sentence : sentence | RETURN exp SEMICOLON;

//Concurrencia
process : PROCESS VARIABLE COLON MONITOR VARIABLE COLON CONNECTION VARIABLE dictionary body ;
concurrency : loop | exec | start_process | stop | message;
loop : LOOP call COLON MONITOR VARIABLE SEMICOLON ;
exec : EXEC call_sentence;
start_process : START VARIABLE SEMICOLON;
stop : STOP MONITOR? VARIABLE SEMICOLON;
message : MESSAGE CONNECTION VARIABLE COLON dictionary SEMICOLON;

//Diccionario de valores
dictionary : LESS dict_element? GREATER;
dict_element : STRING COLON dict_value | dict_element ',' dict_element;
dict_value : VARIABLE | NUMBER | STRING | call;


//Array de objetos
element : NUMBER | STRING | element ',' element;
list_elements: OP_SQUARE element? CL_SQUARE;
//Operadores
logic : AND | OR ;
//test : NUMBER*;