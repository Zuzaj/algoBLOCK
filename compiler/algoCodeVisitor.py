# Generated from algoCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .algoCodeParser import algoCodeParser
else:
    from algoCodeParser import algoCodeParser

# This class defines a complete generic visitor for a parse tree produced by algoCodeParser.

class algoCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by algoCodeParser#program.
    def visitProgram(self, ctx:algoCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#code.
    def visitCode(self, ctx:algoCodeParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#function_def.
    def visitFunction_def(self, ctx:algoCodeParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#function_call.
    def visitFunction_call(self, ctx:algoCodeParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#argument.
    def visitArgument(self, ctx:algoCodeParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#arguments.
    def visitArguments(self, ctx:algoCodeParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#statement.
    def visitStatement(self, ctx:algoCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#assignment.
    def visitAssignment(self, ctx:algoCodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#bool_expression.
    def visitBool_expression(self, ctx:algoCodeParser.Bool_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#for_loop.
    def visitFor_loop(self, ctx:algoCodeParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#if_else_statement.
    def visitIf_else_statement(self, ctx:algoCodeParser.If_else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#else_statement.
    def visitElse_statement(self, ctx:algoCodeParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#else_return_statement.
    def visitElse_return_statement(self, ctx:algoCodeParser.Else_return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#if_return_statement.
    def visitIf_return_statement(self, ctx:algoCodeParser.If_return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#if_statement.
    def visitIf_statement(self, ctx:algoCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#while_statement.
    def visitWhile_statement(self, ctx:algoCodeParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#array_def.
    def visitArray_def(self, ctx:algoCodeParser.Array_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#array_call.
    def visitArray_call(self, ctx:algoCodeParser.Array_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#return_statement.
    def visitReturn_statement(self, ctx:algoCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#expression.
    def visitExpression(self, ctx:algoCodeParser.ExpressionContext):
        return self.visitChildren(ctx)



del algoCodeParser