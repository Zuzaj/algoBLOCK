from antlr4 import *
from compiler.algoCodeLexer import algoCodeLexer
from compiler.algoCodeParser import algoCodeParser
from compiler.algoCodeListener import algoCodeListener
from antlr4.tree.Tree import *

from antlr4 import ParserRuleContext

def print_tokens(lexer):
    lexer.reset()
    tokens = []
    used_token_types = [] 
    for token in lexer.getAllTokens():
        token_description = f"{token.text} ({lexer.symbolicNames[token.type]})"
        tokens.append(token_description)
        used_token_types.append(lexer.symbolicNames[token.type]) 
    lexer.reset()
    tokens_string = '\n'.join(tokens)
    with open('tokens.txt', 'w', encoding='utf-8') as file:
        file.write(tokens_string)


class TreePrinterListener(ParseTreeListener):
    def __init__(self, rule_names):
        self.rule_names = rule_names
        self.lines = []
        self.level = 0

    def enterEveryRule(self, ctx):
        rule_index = ctx.getRuleIndex()
        rule_name = self.rule_names[rule_index] if self.rule_names else "Unknown rule"
        self.lines.append(' ' * 2 * self.level + rule_name)
        self.level += 1

    def exitEveryRule(self, ctx):
        self.level -= 1

    def getFormattedTree(self):
        return "\n".join(self.lines)


def main():
    #tu możesz wybrać inny plik do testowania z folderu algorithms lub przesłać swój plik do folderu, a następnie wpisać jesgo nazwę
    input_stream = FileStream('algorithms/algo13.txt', encoding='utf-8')
    lexer = algoCodeLexer(input_stream)
    print_tokens(lexer)
    stream = CommonTokenStream(lexer)
    parser = algoCodeParser(stream)
    tree = parser.program() 

    printer = TreePrinterListener(parser.ruleNames)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    formatted_tree = printer.getFormattedTree()
    print(formatted_tree)
    with open('formatted_tree.txt', 'w', encoding='utf-8') as file:
        file.write(formatted_tree)
    

if __name__ == '__main__':
    main()
