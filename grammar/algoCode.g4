grammar algoCode;


// Define tokens
TOK_VAR: '"'[a-zA-Z_]+'"';
TOK_NUM: '[0-9]+([.][0-9]+)?';
TOK_ASSIGN: '=';
TOK_IS_EQUAL: '?=';
TOK_NOT_EQUAL: '/=';
TOK_SMALLER: '<';
TOK_SMALLER_EQ: '<=';
TOK_GREATER: '>';
TOK_GREATER_EQ: '>=';
TOK_PLUS: '+';
TOK_MINUS: '-';
TOK_EL: '*';
TOK_DIV: '/';
TOK_TAB_L: '[';
TOK_TAB_R: ']';
TOK_ARG_L: '(';
TOK_ARG_R: ')';
TOK_WS: '(' ' | '\t' | '\n') -> skip;
TOK_FOR : 'for';
TOK_WHILE : 'while';
TOK_IF : 'if';
TOK_END_IF: 'endif';
TOK_ELSE: 'else';
TOK_END_ELSE: 'endelse';
TOK_DO : 'do';
TOK_TO : 'to';
TOK_THEN : 'then';
TOK_LEN : 'length';
TOK_RETURN : 'return';
TOK_FLOOR: 'floor';
TOK_FUNC : 'func';
TOK_AND : 'and';
TOK_OR : 'or';
TOK_EOF : EOF;
TOK_END_FUNC : 'endfunction';
TOK_DOWNTO: 'downto';
TOK_COMMA: ',';



// Parser rules
program: (function | statement)+ TOK_EOF;

function_def: TOK_FUNC TOK_VAR TOK_ARG_L arguments? TOK_ARG_R (TOK_EL statement)+ TOK_END_FUNC;

function_call: TOK_VAR TOK_ARG_L expression_list? TOK_ARG_R;

argument: TOK_VAR | TOK_NUM | (( TOK_VAR | TOK_NUM) (TOK_PLUS|TOK_MINUS) ( TOK_VAR | TOK_NUM))

arguments: TOK_VAR (TOK_COMMA TOK_VAR)*;

statement: assignment | for_loop | if_statement | return_statement | function_call;

assignment: TOK_VAR TOK_ASSIGN expression;

bool_statement: ( TOK_VAR | TOK_NUM ) (TOK_IS_EQUAL | TOK_NOT_EQUAL | TOK_SMALLER | TOK_GREATER) ( TOK_VAR | TOK_NUM) 
((TOK_AND | TOK_OR)  ( TOK_VAR | TOK_NUM ) (TOK_IS_EQUAL | TOK_NOT_EQUAL | TOK_SMALLER | TOK_GREATER) ( TOK_VAR | TOK_NUM))*;

for_loop: TOK_FOR TOK_VAR TOK_ASSIGN expression (TOK_TO | TOK_DOWNTO) expression TOK_DO (TOK_EL statement)+;

if_statement: TOK_IF bool_statement TOK_THEN (TOK_EL statement)+;

else_statement: TOK_ELSE (TOK_EL statement)+;

while_statement: TOK_WHILE bool_statement TOK_DO (TOK_EL statement)+;

array_def: TOK_VAR TOK_ASSIGN TOK_TAB_L TOK_TAB_R;

return_statement: TOK_RETURN expression;

expression_list: expression (',' expression)*;

expression: TOK_VAR
           | TOK_NUM
           | expression TOK_PLUS expression
           | expression TOK_MINUS expression
           | expression TOK_MUL expression
           | expression TOK_DIV expression
           | TOK_TAB_L expression_list? TOK_TAB_R
           | TOK_VAR TOK_GREATER expression
           | TOK_VAR TOK_SMALLER expression
           | TOK_VAR TOK_IS_EQUAL expression
           | TOK_VAR TOK_NOT_EQUAL expression
           | TOK_LEN TOK_ARG_L TOK_VAR TOK_ARG_R
           | TOK_FLOOR TOK_ARG_L expression TOK_ARG_R
           | TOK_ARG_L expression TOK_ARG_R
           | TOK_VAR TOK_AND TOK_VAR
           | TOK_VAR TOK_OR TOK_VAR;
