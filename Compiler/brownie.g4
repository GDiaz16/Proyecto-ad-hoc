grammar brownie;
options{language = Python3;}

//----------------------REGLAS LEXICAS -------------------------------------------->
//Palabras reservadas
IF   : 'if';
ELIF : 'elif';
ELSE : 'else';


WHILE : 'while';
FOR : 'for';
DO : 'do';

TRUE : 'True';
FALSE : 'False';

//Concurrencia
PROCESS : 'process';
START : 'start';

//Imprimir
PRINT :'print';

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

WHITESPACE : [ \t\n] -> skip;

//-------------------------------GRAMATICA------------------------------------->
start : structure*  EOF;

structure :  sentence | procedure;
//Cualquier instruccion
sentence : definition | conditional | print_ | cycle | concurrency ;

//Parametros
parameter : VARIABLE #parameter1| parameter ',' parameter #parameter2;
parameter_call : VARIABLE #parameter_call1 | NUMBER #parameter_call2
                | STRING #parameter_call3
                | parameter_call ',' parameter_call #parameter_call5;

//Definicion y asignacion de variables
definition : assign SEMICOLON ;
assign :  VARIABLE ASSIGN exp #assign1| VARIABLE INCREMENT #assign2
        | VARIABLE DECREMENT #assign3 | VARIABLE ASSIGN list_elements #assign4
        |  VARIABLE ASSIGN text #assign6;

text : text PLUS text #text1| STRING #text2 | VARIABLE #text3;

//Array de objetos
element : NUMBER #element1| VARIABLE #element2| STRING #element3| element ',' element #element4;
list_elements: OP_SQUARE element? CL_SQUARE;

//Expresion matematica
exp : exp ar_operator term #exp1| term #exp2 ;
term : ar_value prior_operator term #term1| ar_value #term2;
ar_value : NUMBER #ar_value1 | VARIABLE #ar_value2
            | OP_PARENTHESIS exp CL_PARENTHESIS #ar_value4;

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

//Concurrencia
procedure : PROCESS  VARIABLE body;
concurrency : start_process ;
start_process : START VARIABLE SEMICOLON;

//Print
print_ : PRINT OP_PARENTHESIS print_value CL_PARENTHESIS SEMICOLON;
print_value : VARIABLE | NUMBER | STRING ;//| list_elements;
