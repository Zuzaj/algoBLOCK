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

    # def enter_scope(self):
    #     self.context.append({}) 

    # def exit_scope(self):
    #     if len(self.context) > 1:
    #         self.context.pop()
    
    #wchodze do bloku, odwiedzam dzieci, wychodze z bloku
    def visitFunction_def(self, ctx:algoCodeParser.Function_defContext):
        func_name = ctx.TOK_VAR().getText()
        # self.enter_scope()
        self.context[-1][func_name] = {}
        return self.visitChildren(ctx)
    
    #początkowo samo przypisanie zmiennej bez tablicy dla testow
    def visitAssignment(self, ctx:algoCodeParser.AssignmentContext):
        left_value = ctx.getChild(0).getText() 
        value = self.visit(ctx.expression())
        if ctx.array_call():
            array_name = left_value
            index = self.visit(ctx.array_call().expression())
            #sprawdzam czy tablica zainicjowana
            if array_name not in self.context[-1]:
                #jeśli nie to inicjuję jako słownik
                self.context[-1][array_name] = {}
            self.context[-1][array_name][index] = value
        else:
            self.context[-1][left_value] = value
        return value
    
    def visitExpression(self, ctx:algoCodeParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            if isinstance(child, algoCodeParser.TOK_VARContext):
                # zmienna
                var_name = child.getText()
                return self.context[-1].get(var_name, None)
            elif isinstance(child, algoCodeParser.TOK_NUMContext):
                # liczba
                return int(child.getText())
            elif isinstance(child, algoCodeParser.Array_callContext):
                # tablica
                return self.visitArray_call(child)
            elif isinstance(child, algoCodeParser.Function_callContext):
                # fukcja
                return self.visitFunction_call(child)
            else:
                # jesli cos innego to odwiedzamy śwezel
                return self.visit(child)
    
    def visitFunction_call(self, ctx:algoCodeParser.Function_callContext):
        func_name = ctx.TOK_VAR().getText()
        # obsługa specjalnych funkcji, na razie tylko print
        if func_name.lower() == 'print':
            print('print')
        # tutaj można dodać obsługę innych funkcji
        return None
       



    # Visit a parse tree produced by algoCodeParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoCodeParser#code.
    def visitCode(self, ctx:algoCodeParser.CodeContext):
        for child in ctx.getChildren():
            self.visit(child)



    # Visit a parse tree produced by algoCodeParser#argument.
    def visitArgument(self, ctx:algoCodeParser.ArgumentContext):
        #zwracam dziecko czyli argument
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by algoCodeParser#arguments.
    def visitArguments(self, ctx:algoCodeParser.ArgumentsContext):
        arguments = []
        # Przechodze przez każdy argument
        for child in ctx.getChildren():
            if isinstance(child, algoCodeParser.ArgumentContext):
                arguments.append(self.visitArgument(child))
        return arguments


    # Visit a parse tree produced by algoCodeParser#statement.
    def visitStatement(self, ctx:algoCodeParser.StatementContext):
        statement_child = ctx.getChild(0)
        if isinstance(statement_child, algoCodeParser.AssignmentContext):
            self.visitAssignment(statement_child)
        elif isinstance(statement_child, algoCodeParser.Array_defContext):
            self.visitArray_def(statement_child)
        elif isinstance(statement_child, algoCodeParser.Function_callContext):
            self.visitFunction_call(statement_child)
        elif isinstance(statement_child, algoCodeParser.For_loopContext):
            self.visitFor_loop(statement_child)
        elif isinstance(statement_child, algoCodeParser.If_statementContext):
            self.visitIf_statement(statement_child)
        elif isinstance(statement_child, algoCodeParser.While_statementContext):
            self.visitWhile_statement(statement_child)
    


    # Visit a parse tree produced by algoCodeParser#bool_expression.
    def visitBool_expression(self, ctx:algoCodeParser.Bool_expressionContext):
        left_operand = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right_operand = self.visit(ctx.getChild(2))

        # Sprawdzam warunki i zwracam wartość
        if operator == '==':
            return left_operand == right_operand
        elif operator == '!=':
            return left_operand != right_operand
        elif operator == '<':
            return left_operand < right_operand
        elif operator == '<=':
            return left_operand <= right_operand
        elif operator == '>':
            return left_operand > right_operand
        elif operator == '>=':
            return left_operand >= right_operand


    # Visit a parse tree produced by algoCodeParser#for_loop.
    def visitFor_loop(self, ctx:algoCodeParser.For_loopContext):
        var = ctx.TOK_VAR().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        statements = [self.visitStatement(child) for child in ctx.statement()]

        # logika dla for 
        for i in range(start, end + 1):
            self.context[-1][var] = i
            for statement in statements:
                self.visitStatement(statement)


    # Visit a parse tree produced by algoCodeParser#if_else_statement.
    def visitIf_else_statement(self, ctx:algoCodeParser.If_else_statementContext):
        condition = self.visit(ctx.if_statement())
        #lista wszystkich elsów
        else_statements = []
        if ctx.else_statement():
            #przechodzę po wszystkich statementach w kazdym elsie
            else_statements = [self.visitStatement(child) for child in ctx.else_statement().statement()]

        return condition, else_statements


    # Visit a parse tree produced by algoCodeParser#else_statement.
    def visitElse_statement(self, ctx:algoCodeParser.Else_statementContext):
        return [self.visitStatement(child) for child in ctx.statement()]

    # Visit a parse tree produced by algoCodeParser#else_return_statement.
    def visitElse_return_statement(self, ctx:algoCodeParser.Else_return_statementContext):
        return self.visitReturn_statement(ctx.return_statement())


    # Visit a parse tree produced by algoCodeParser#if_return_statement.
    def visitIf_return_statement(self, ctx:algoCodeParser.If_return_statementContext):
        condition = self.visit(ctx.if_statement())
        return_statement = self.visitReturn_statement(ctx.return_statement())
        return condition, return_statement


    # Visit a parse tree produced by algoCodeParser#if_statement.
    def visitIf_statement(self, ctx:algoCodeParser.If_statementContext):
        condition = self.visit(ctx.bool_expression())

        # iteruje po statememntach w ifie
        statements = [self.visitStatement(child) for child in ctx.statement()]
        return condition, statements


    # Visit a parse tree produced by algoCodeParser#while_statement.
    def visitWhile_statement(self, ctx:algoCodeParser.While_statementContext):
        condition = self.visit(ctx.bool_expression())

        # iteruje po statementach w whilu
        statements = [self.visitStatement(child) for child in ctx.statement()]

        # wykonuje whila
        while while_condition:
            for statement in statements:
                self.visitStatement(statement)
            while_condition = self.visit(ctx.bool_expression())


    # Visit a parse tree produced by algoCodeParser#array_def.
    def visitArray_def(self, ctx:algoCodeParser.Array_defContext):
        #pobieram nazzwe tablicy i dodaje do kontekstu jako zainicjalizowana
        arr_name = ctx.TOK_VAR().getText()
        self.context[-1][arr_name] = {}
        return None


    # Visit a parse tree produced by algoCodeParser#array_call.
    def visitArray_call(self, ctx:algoCodeParser.Array_callContext):
        arr_name = ctx.TOK_VAR().getText()
        #sprawdzam index w nawiasach
        index = self.visit(ctx.expression())
        # jeśli istnieje tablica i taki index to pobieram wartość
        if arr_name in self.context[-1] and index in self.context[-1][arr_name]:
            return self.context[-1][arr_name][index]
        else:
            #jak nie to nic? tutaj chyba error by się przydał
            return None


    # Visit a parse tree produced by algoCodeParser#return_statement.
    def visitReturn_statement(self, ctx:algoCodeParser.Return_statementContext):
        value = self.visit(ctx.getChild(1))
        return value




del algoCodeParser
