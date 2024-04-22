# Generated from algoCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .algoCodeParser import algoCodeParser
else:
    from algoCodeParser import algoCodeParser

# This class defines a complete listener for a parse tree produced by algoCodeParser.
class algoCodeListener(ParseTreeListener):

    # Enter a parse tree produced by algoCodeParser#program.
    def enterProgram(self, ctx:algoCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by algoCodeParser#program.
    def exitProgram(self, ctx:algoCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by algoCodeParser#function.
    def enterFunction(self, ctx:algoCodeParser.FunctionContext):
        pass

    # Exit a parse tree produced by algoCodeParser#function.
    def exitFunction(self, ctx:algoCodeParser.FunctionContext):
        pass


    # Enter a parse tree produced by algoCodeParser#arguments.
    def enterArguments(self, ctx:algoCodeParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by algoCodeParser#arguments.
    def exitArguments(self, ctx:algoCodeParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by algoCodeParser#statement.
    def enterStatement(self, ctx:algoCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#statement.
    def exitStatement(self, ctx:algoCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#assignment.
    def enterAssignment(self, ctx:algoCodeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by algoCodeParser#assignment.
    def exitAssignment(self, ctx:algoCodeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by algoCodeParser#for_loop.
    def enterFor_loop(self, ctx:algoCodeParser.For_loopContext):
        pass

    # Exit a parse tree produced by algoCodeParser#for_loop.
    def exitFor_loop(self, ctx:algoCodeParser.For_loopContext):
        pass


    # Enter a parse tree produced by algoCodeParser#if_statement.
    def enterIf_statement(self, ctx:algoCodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#if_statement.
    def exitIf_statement(self, ctx:algoCodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#return_statement.
    def enterReturn_statement(self, ctx:algoCodeParser.Return_statementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#return_statement.
    def exitReturn_statement(self, ctx:algoCodeParser.Return_statementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#function_call.
    def enterFunction_call(self, ctx:algoCodeParser.Function_callContext):
        pass

    # Exit a parse tree produced by algoCodeParser#function_call.
    def exitFunction_call(self, ctx:algoCodeParser.Function_callContext):
        pass


    # Enter a parse tree produced by algoCodeParser#expression_list.
    def enterExpression_list(self, ctx:algoCodeParser.Expression_listContext):
        pass

    # Exit a parse tree produced by algoCodeParser#expression_list.
    def exitExpression_list(self, ctx:algoCodeParser.Expression_listContext):
        pass


    # Enter a parse tree produced by algoCodeParser#expression.
    def enterExpression(self, ctx:algoCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by algoCodeParser#expression.
    def exitExpression(self, ctx:algoCodeParser.ExpressionContext):
        pass



del algoCodeParser