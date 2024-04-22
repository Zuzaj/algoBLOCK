# algoBLOCK

## Założenia programu
Nasz projekt to prosty język do nauki algorytmów, który ma na celu stworzenie łatwo zrozumiałego środowiska programistycznego. Dzięki prostej składni oraz intuicyjnym słowom kluczowym, użytkownicy będą mogli zrozumieć działanie algorytmów poprzez praktyczne wykorzystanie ich w kodzie.
1. Planowany wynik działania programu to interpreter języka pseudokodu, umożliwiający użytkownikom pisanie, testowanie i analizowanie działania algorytmów w czasie rzeczywistym.
2. Planowanym językiem implementacji jest Python.
3. Planowana realizacja skanera oraz parsera poprzez użycie generatora parserów ANTLR 4.

## Tokeny
- ID: '[a-zA-Z_][a-zA-Z0-9_]*';
- NUM: '[0-9]+ (' .' [0-9]+)?';
- TOK_ASSIGN: '=';
- TOK_IS_EQUAL: '==';
- TOK_NOT_EQUAL: '!=';
- TOK_SMALLER: '<';
- TOK_GREATER: '>';
- TOK_PLUS: '+';
- TOK_MINUS: '-';
- TOK_MUL: '*';
- TOK_DIV: '/';
- TOK_TAB_L: '[';
- TOK_TAB_R: ']';
- WS: [ \t\r\n]+ -> skip;

## Gramatyka
```g4
program: function+;

function: 'function' identifier '(' parameterList? ')' block;

parameterList: identifier (',' identifier)*;

block: statement+;

statement:
	assignment
	| ifStatement
	| forStatement
	| whileStatement
	| returnStatement;

assignment:
	identifier ('TOK_TAB_L' (identifier | NUM) 'TOK_TAB_R')? 'TOK_ASSIGN' expression ';';

ifStatement: 'if' expression 'then' block ('else' block)?;

forStatement:
	'for' identifier 'TOK_ASSIGN' expression 'to' expression 'do' block;

whileStatement: 'while' expression 'do' block;

returnStatement: 'return' expression ';';

expression:
	expression (
		TOK_PLUS
		| TOK_MINUS
		| TOK_MUL
		| TOK_DIV
		| TOK_SMALLER
		| TOK_GREATER
		| TOK_IS_EQUAL
		| TOK_NOT_EQUAL
	) expression
	| identifier ('TOK_TAB_L' (identifier | NUM) 'TOK_TAB_R')?
	| '(' expression ')'
	| NUM
	| functionCall;

functionCall: identifier '(' parameterList? ')';
identifier: ID;
```

## Pakiety zewnętrzne
Wykorzystanie ANTLR4 (ANother Tool for Language Recognition) do generowania skanerów i parserów umożliwia szybkie i efektywne tworzenie analizatorów składniowych dla różnorodnych języków programowania oraz specyfikacji formalnych.

## Przykłady użycia 
Proponowane przykłady algorytmów do przetestowania działania języka znajdują się w folderze [algorythms](./algorithms/).




