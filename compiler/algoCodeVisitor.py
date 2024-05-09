# Generated from algoCode.g4 by ANTLR 4.13.1
from antlr4 import ParseTreeVisitor
from antlr4 import *
if "." in __name__:
    from .algoCodeParser import algoCodeParser
else:
    from algoCodeParser import algoCodeParser



# This class defines a complete generic visitor for a parse tree produced by algoCodeParser.

class algoCodeVisitor(ParseTreeVisitor):

    # def listę słowników booo każdy słownik = blok kodu
    def __init__(self):
        self.context = [{}] 

    def enter_scope(self):
        self.context.append({}) 

    def exit_scope(self):
        if len(self.context) > 1:
            self.context.pop()
    
    #wchodze do bloku, odwiedzam dzieci, wychodze z bloku
    def visitFunction_def(self, ctx:algoCodeParser.Function_defContext):
        print("1")
        self.enter_scope()
        result = self.visitChildren(ctx)
        self.exit_scope()
        return result
    
    #początkowo samo przypisanie zmiennej bez tablicy dla testow
    def visitAssignment(self, ctx:algoCodeParser.AssignmentContext):
        x = ctx.getChild(0) 
        value = self.visit(ctx.expression())
        #obsługa tablicy do zrobienia
        name = x.getText()
        self.context[-1][name] = value
        return value
    
    def visitExpression(self, ctx:algoCodeParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            if isinstance(child, algoCodeParser.TOK_VARContext):
                var_name = child.getText()
                return self.context[-1].get(var_name, None)  # Pobierz wartość zmiennej
            elif isinstance(child, algoCodeParser.TOK_NUMContext):
                return int(child.getText())  # Zwróć wartość liczby
            else:
                # Obsługa wywołania tablicy lub funkcji przez rekursywne wywołanie visit
                return self.visit(child)
    
    def visitFunction_call(self, ctx:algoCodeParser.Function_callContext):
        func_name = ctx.getChild(0).getText() 
        print(func_name)
        if func_name.lower() == 'print':  
            # self.visitPrintFunction()
            print('print')
       



    # Visit a parse tree produced by algoCodeParser#program.
    def visitProgram(self, ctx):
        print("1")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#code.
    def visitCode(self, ctx:algoCodeParser.CodeContext):
        if ctx.function_def():
            self.visitFunction_def()



    # Visit a parse tree produced by algoCodeParser#argument.
    def visitArgument(self, ctx:algoCodeParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#arguments.
    def visitArguments(self, ctx:algoCodeParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#statement.
    def visitStatement(self, ctx:algoCodeParser.StatementContext):
        return self.visitChildren(ctx.getChild(1))
    


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




del algoCodeParser
