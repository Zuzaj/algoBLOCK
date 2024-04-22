# algoBLOCK

## Założenia programu
Nasz projekt to prosty język do nauki algorytmów, który ma na celu stworzenie łatwo zrozumiałego środowiska programistycznego. Dzięki prostej składni oraz intuicyjnym słowom kluczowym, użytkownicy będą mogli zrozumieć działanie algorytmów poprzez praktyczne wykorzystanie ich w kodzie.
1. Planowany wynik działania programu to interpreter języka pseudokodu, umożliwiający użytkownikom pisanie, testowanie i analizowanie działania algorytmów w czasie rzeczywistym.
2. Planowanym językiem implementacji jest Python.
3. Planowana realizacja skanera oraz parsera poprzez użycie generatora parserów ANTLR 4.

## Uruchomienie 
1. Pobierz repozytorium na swój komputer.
2. Zainstaluj paiekt używając polecenia: `pip install antlr4-python3-runtime==4.13.1`
3. Uruchom plik `main.py`, możesz wcześniej edytować domyślny plik testowy.
4. Zidentyfikowane tokeny zostaną zapisane do pliku `tokens.txt`, a wynik analizy składniowej (hierarchia) do pliku `formatted_tree.txt`.

## Tokeny
- TOK_VAR: '[a-zA-Z_]+';
- TOK_NUM: '[0-9]+ (' .' [0-9]+)?';
- TOK_ASSIGN: '=';
- TOK_IS_EQUAL: '?=';
- TOK_NOT_EQUAL: '/=';
- TOK_SMALLER: '<';
- TOK_GREATER: '>';
- TOK_PLUS: '+';
- TOK_MINUS: '-';
- TOK_MUL: '*';
- TOK_DIV: '/';
- TOK_TAB_L: '[';
- TOK_TAB_R: ']';
- TOK_ARG_L: '(';
- TOK_ARG_R: ')';
- TOK_WS: '[ \t\r\n]+' -> skip;
- TON_NL: '\n';
- TOK_FOR  : 'for';
- TOK_WHILE : 'while';
- TOK_IF : 'if';
- TOK_DO : 'do';
- TOK_TO : 'to';
- TOK_THEN : 'then';
- TOK_LEN : 'length';
- TOK_RETURN : 'return';	
- TOK_FLOOR: 'floor';
- TOK_FUNC : 'function';
- TOK_AND : 'and';
- TOK_OR : 'or';

## Gramatyka
```g4
program: (function | statement)+ TOK_EOF;

function: TOK_FUNC TOK_VAR TOK_ARG_L arguments? TOK_ARG_R statement;

arguments: TOK_VAR (',' TOK_VAR)*;

statement: assignment | for_loop | if_statement | return_statement | function_call | TOK_NL;

assignment: TOK_VAR TOK_ASSIGN expression;

for_loop: TOK_FOR TOK_VAR TOK_ASSIGN expression TOK_TO expression TOK_DO statement;

if_statement: TOK_IF expression TOK_THEN statement;

return_statement: TOK_RETURN expression;

function_call: TOK_VAR TOK_ARG_L expression_list? TOK_ARG_R;

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
```

## Pakiety zewnętrzne
Wykorzystanie ANTLR4 (ANother Tool for Language Recognition) do generowania skanerów i parserów umożliwia szybkie i efektywne tworzenie analizatorów składniowych dla różnorodnych języków programowania oraz specyfikacji formalnych.

## Przykłady użycia 
Proponowane przykłady algorytmów do przetestowania działania języka znajdują się w folderze [algorythms](./algorithms/).




