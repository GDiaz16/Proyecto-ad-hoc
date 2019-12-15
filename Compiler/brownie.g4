grammar brownie;
options{language = Python3;}

//----------------------REGLAS LEXICAS -------------------------------------------->
//Palabras reservadas
IF   : 'if';
ELIF : 'elif';
ELSE : 'else';

SWITCH : 'switch';
CASE : 'case';
DEFAULT :'default';

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

//Imprimir
PRINT :'print';

//Salto de linea
//JUMPSPACE: '\n';

COMMENT : '#'.*?'\n'  -> skip;
COMMENT_AREA : '/*'.*?'*/' -> skip;

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
start : structure*  EOF;
//comm : COMMENT;

structure : function | sentence | call_sentence | process | procedure;
//Cualquier instruccion
sentence : definition | conditional | print_ | call_sentence | cycle | concurrency | switch_ | break_ ;

//Definicion de funciones
function : FUNCTION VARIABLE OP_PARENTHESIS parameter? CL_PARENTHESIS fun_body;
//Llamado de una funcion
call :  VARIABLE OP_PARENTHESIS parameter_call? CL_PARENTHESIS;
call_sentence : call SEMICOLON;
//Parametros
parameter : VARIABLE #parameter1| parameter ',' parameter #parameter2;
parameter_call : VARIABLE #parameter_call1 | NUMBER #parameter_call2
                | STRING #parameter_call3| call #parameter_call4
                | parameter_call ',' parameter_call #parameter_call5
                | array_call #parameter_call6;

//Definicion y asignacion de variables
definition : assign SEMICOLON ;
assign :  VARIABLE ASSIGN exp #assign1| VARIABLE INCREMENT #assign2
        | VARIABLE DECREMENT #assign3 | VARIABLE ASSIGN list_elements #assign4
        | array_call ASSIGN exp #assign5 | VARIABLE ASSIGN text #assign6;

text : text PLUS text #text1| STRING #text2 | VARIABLE #text3;

//Array de objetos
element : NUMBER #element1| VARIABLE #element2| STRING #element3| element ',' element #element4;
list_elements: OP_SQUARE element? CL_SQUARE;

//Expresion matematica
exp : exp ar_operator term #exp1| term #exp2 ;
term : ar_value prior_operator term #term1| ar_value #term2;
ar_value : NUMBER #ar_value1 | VARIABLE #ar_value2 | call #ar_value3
            | OP_PARENTHESIS exp CL_PARENTHESIS #ar_value4 | array_call #ar_value5;
array_call : VARIABLE OP_SQUARE ar_value CL_SQUARE;
//Operadores aritmeticos
ar_operator : PLUS | MINUS;
prior_operator :  MUL | DIV | POW | MOD ;

//Estructura condicional
conditional : IF  condition COLON  body otherwise?;
otherwise : ELIF  condition COLON  body otherwise? #otherwise1| ELSE body #otherwise2;

condition :  condition logic other_cond #condition1
                | other_cond #condition2;

other_cond : NOT? other_condition ;

other_condition : com_value comparator other_condition #other_condition1
                | com_value #other_condition2;

com_value : STRING | TRUE  | FALSE  | ar_value ;
comparator : EQ | DIF | GREATER | LESS | GEQ | LEQ ;
logic : AND | OR ;

//Ciclos repetitivos
cycle : do_while| while_ | for_;
do_while: DO body WHILE condition SEMICOLON;
while_ : WHILE condition COLON body ;
for_ : FOR for_condition COLON body;
for_condition : for_definition SEMICOLON condition SEMICOLON assign #for_condition1
                | for_iterator #for_condition2;
for_definition : VARIABLE ASSIGN exp;
for_iterator : VARIABLE IN VARIABLE;

//Cuerpo de instrucciones
body : OP_BRACE sentence* CL_BRACE;
fun_body : OP_BRACE fun_sentence* CL_BRACE ;
fun_sentence : sentence | RETURN exp SEMICOLON;

//Concurrencia
procedure : PROCESS body;
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

//Switch
switch_ : SWITCH VARIABLE COLON switch_body;
switch_body : OP_BRACE case_* default_? CL_BRACE;
case_ : CASE case_value COLON sentence* ;
default_: DEFAULT COLON sentence* ;
case_value: NUMBER | STRING;
break_ : BREAK SEMICOLON;

//Print
print_ : PRINT OP_PARENTHESIS print_value CL_PARENTHESIS SEMICOLON;
print_value : VARIABLE | NUMBER | STRING | list_elements;

