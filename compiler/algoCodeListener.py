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


    # Enter a parse tree produced by algoCodeParser#code.
    def enterCode(self, ctx:algoCodeParser.CodeContext):
        pass

    # Exit a parse tree produced by algoCodeParser#code.
    def exitCode(self, ctx:algoCodeParser.CodeContext):
        pass


    # Enter a parse tree produced by algoCodeParser#function_def.
    def enterFunction_def(self, ctx:algoCodeParser.Function_defContext):
        pass

    # Exit a parse tree produced by algoCodeParser#function_def.
    def exitFunction_def(self, ctx:algoCodeParser.Function_defContext):
        pass


    # Enter a parse tree produced by algoCodeParser#function_call.
    def enterFunction_call(self, ctx:algoCodeParser.Function_callContext):
        pass

    # Exit a parse tree produced by algoCodeParser#function_call.
    def exitFunction_call(self, ctx:algoCodeParser.Function_callContext):
        pass


    # Enter a parse tree produced by algoCodeParser#argument.
    def enterArgument(self, ctx:algoCodeParser.ArgumentContext):
        pass

    # Exit a parse tree produced by algoCodeParser#argument.
    def exitArgument(self, ctx:algoCodeParser.ArgumentContext):
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


    # Enter a parse tree produced by algoCodeParser#bool_expression.
    def enterBool_expression(self, ctx:algoCodeParser.Bool_expressionContext):
        pass

    # Exit a parse tree produced by algoCodeParser#bool_expression.
    def exitBool_expression(self, ctx:algoCodeParser.Bool_expressionContext):
        pass


    # Enter a parse tree produced by algoCodeParser#for_loop.
    def enterFor_loop(self, ctx:algoCodeParser.For_loopContext):
        pass

    # Exit a parse tree produced by algoCodeParser#for_loop.
    def exitFor_loop(self, ctx:algoCodeParser.For_loopContext):
        pass


    # Enter a parse tree produced by algoCodeParser#if_else_statement.
    def enterIf_else_statement(self, ctx:algoCodeParser.If_else_statementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#if_else_statement.
    def exitIf_else_statement(self, ctx:algoCodeParser.If_else_statementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#else_statement.
    def enterElse_statement(self, ctx:algoCodeParser.Else_statementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#else_statement.
    def exitElse_statement(self, ctx:algoCodeParser.Else_statementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#else_return_statement.
    def enterElse_return_statement(self, ctx:algoCodeParser.Else_return_statementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#else_return_statement.
    def exitElse_return_statement(self, ctx:algoCodeParser.Else_return_statementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#if_return_statement.
    def enterIf_return_statement(self, ctx:algoCodeParser.If_return_statementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#if_return_statement.
    def exitIf_return_statement(self, ctx:algoCodeParser.If_return_statementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#if_statement.
    def enterIf_statement(self, ctx:algoCodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#if_statement.
    def exitIf_statement(self, ctx:algoCodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#while_statement.
    def enterWhile_statement(self, ctx:algoCodeParser.While_statementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#while_statement.
    def exitWhile_statement(self, ctx:algoCodeParser.While_statementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#array_def.
    def enterArray_def(self, ctx:algoCodeParser.Array_defContext):
        pass

    # Exit a parse tree produced by algoCodeParser#array_def.
    def exitArray_def(self, ctx:algoCodeParser.Array_defContext):
        pass


    # Enter a parse tree produced by algoCodeParser#array_call.
    def enterArray_call(self, ctx:algoCodeParser.Array_callContext):
        pass

    # Exit a parse tree produced by algoCodeParser#array_call.
    def exitArray_call(self, ctx:algoCodeParser.Array_callContext):
        pass


    # Enter a parse tree produced by algoCodeParser#return_statement.
    def enterReturn_statement(self, ctx:algoCodeParser.Return_statementContext):
        pass

    # Exit a parse tree produced by algoCodeParser#return_statement.
    def exitReturn_statement(self, ctx:algoCodeParser.Return_statementContext):
        pass


    # Enter a parse tree produced by algoCodeParser#expression.
    def enterExpression(self, ctx:algoCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by algoCodeParser#expression.
    def exitExpression(self, ctx:algoCodeParser.ExpressionContext):
        pass



del algoCodeParser