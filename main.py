from antlr4 import *
from compiler.algoCodeLexer import algoCodeLexer
from compiler.algoCodeParser import algoCodeParser
from compiler.algoCodeListener import algoCodeListener
from compiler.algoCodeVisitor import algoCodeVisitor
from antlr4.tree.Tree import *

from antlr4 import ParserRuleContext



def main():

    #tu możesz wybrać inny plik do testowania z folderu algorithms lub przesłać swój plik do folderu, a następnie wpisać jesgo nazwę
    input_stream = FileStream('algorithms/algo0.txt', encoding='utf-8')
    lexer = algoCodeLexer(input_stream)
    #print_tokens(lexer)
    stream = CommonTokenStream(lexer)
    parser = algoCodeParser(stream)
    tree = parser.program() 
    print(tree.toStringTree(recog=parser))

    visitor = algoCodeVisitor()
    visitor.visitProgram(tree)

    

if __name__ == '__main__':
    main()
