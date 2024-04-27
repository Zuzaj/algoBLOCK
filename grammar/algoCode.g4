grammar algoCode;


// Define tokens
TOK_VAR: '"'[a-zA-Z_]+'"';
TOK_NUM: '[0-9]+([.][0-9]+)?';

//pytanie czy my potrzebujemy floatów?
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
TOK_FUNC : 'function';
TOK_AND : 'and';
TOK_OR : 'or';
TOK_EOF : '"EOF"';
TOK_END_FUNC : 'endfunction';
TOK_DOWNTO: 'downto';
TOK_COM: ',';
TOK_ARROW_L: '->';
TOK_ARROW_R: '>-';



// Parser rules
program: (function_def | statement)+ TOK_EOF;

function_def: TOK_FUNC TOK_VAR TOK_ARG_L arguments? TOK_ARG_R (statement)* return_statement? TOK_END_FUNC;

function_call: TOK_VAR TOK_ARG_L arguments? TOK_ARG_R;

argument: expression;

arguments: argument (TOK_COMMA argument)*;

statement: TOK_EL ( assignment | for_loop | if_statement | return_statement | function_call | while_statement | array_def );

assignment: (TOK_VAR | array_call) TOK_ASSIGN expression;

bool_expression: ( TOK_VAR | TOK_NUM | array_call )
                 (TOK_IS_EQUAL | TOK_NOT_EQUAL | TOK_SMALLER | TOK_GREATER | TOK_GREATER_EQ | TOK_SMALLER_EQ)
                 ( TOK_VAR | TOK_NUM | array_call) 
                 ((TOK_AND | TOK_OR)  
                 ( TOK_VAR | TOK_NUM | array_call ) 
                 (TOK_IS_EQUAL | TOK_NOT_EQUAL | TOK_SMALLER | TOK_GREATER | TOK_SMALLER_EQ | TOK_GREATER_EQ)
                ( TOK_VAR | TOK_NUM | array_call))*;

for_loop: TOK_FOR TOK_VAR TOK_ASSIGN expression (TOK_TO | TOK_DOWNTO) expression TOK_DO TOK_ARROW_L (statement)+ TOK_ARROW_R;

if_statement: TOK_IF bool_expression TOK_THEN TOK_ARROW_L (statement)+ TOK_ARROW_R;

else_statement: TOK_ELSE TOK_ARROW_L (statement)+ TOK_ARROW_R;

while_statement: TOK_WHILE bool_expression TOK_DO TOK_ARROW_L (statement)+ TOK_ARROW_R;

array_def: TOK_VAR TOK_ASSIGN TOK_TAB_L TOK_TAB_R;

array_call: TOK_VAR TOK_TAB_L 
            ( expression | function_call)
            TOK_TAB_R;

return_statement: TOK_RETURN (TOK_VAR | TOK_NUM);

expression_list: expression (',' expression)*;


expression: TOK_VAR
           | TOK_NUM
           | array_call
           | expression TOK_PLUS expression
           | expression TOK_MINUS expression
           | expression TOK_DIV expression
           | TOK_LEN TOK_ARG_L TOK_VAR TOK_ARG_R
           | function_call;


