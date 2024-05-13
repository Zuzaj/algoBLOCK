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
        self.context[-1][func_name] = {}
        arguments = self.visit(ctx.arguments())
        statements = [self.visit(statement) for statement in ctx.statement()]
        return_statement = self.visit(ctx.return_statement()) if ctx.return_statement() else None
        print(f"Function: {func_name}, Arguments: {arguments}")
        for statement in statements:
            self.visitStatement(statement)
        if return_statement:
            self.visitReturn_statement(return_statement)

    
    #początkowo samo przypisanie zmiennej bez tablicy dla testow
    def visitAssignment(self, ctx:algoCodeParser.AssignmentContext):
        left_value = ctx.getChild(0).getText() 
        value = self.visitExpression(ctx.expression())
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
        print("Assignment successful")
        return value
    
    def visitExpression(self, ctx: algoCodeParser.ExpressionContext):
            # If the expression is a variable
        if  ctx.getChildCount() == 1:  
            if ctx.TOK_VAR():
                var_name = ctx.TOK_VAR().getText()
                return var_name
            
            # If the expression is a number
            elif ctx.TOK_NUM():
                return int(ctx.TOK_NUM().getText())
            
            # If the expression is an array call
            elif ctx.array_call():
                return self.visitArray_call(ctx.array_call())
            
            # If the expression is a function call
            elif ctx.function_call():
                return self.visitFunction_call(ctx.function_call())
            
            # ten len token to chyba nie powinien istnieć wgl
            elif ctx.TOK_LEN():
                array_name = ctx.expression().getText()
                if array_name in self.context[-1]:
                    return len(self.context[-1][array_name])
                else:
                    return None
        
        # jeśli działanie
        elif ctx.getChildCount() > 1:
            if(ctx.getChild(0).TOK_VAR()):
                left_operand_name = ctx.getChild(0).getText()
                left_operand =  self.context[-1].get(left_operand_name, None)
            else:
                left_operand = int(ctx.getChild(0).getText())

            if(ctx.getChild(2).TOK_VAR()):
                right_operand_name = ctx.getChild(2).getText()
                right_operand =  self.context[-1].get(right_operand_name, None)
            else:
                right_operand = int(ctx.getChild(2).getText())
            
            # tutaj się wali bo jak mam a = a + 5 to bierze a za ciag znaków i nie odwoła się do tego co przechowuje zmienna
            # left_operand = self.visitExpression(ctx.expression(0))
            # right_operand = self.visitExpression(ctx.expression(1))
            # print(left_operand) 
            operator = ctx.getChild(1).getText()
            
            if operator == '+':
                return (left_operand + right_operand)
            elif operator == '-':
                return left_operand - right_operand
            elif operator == '/':
                if right_operand != 0:
                    return left_operand / right_operand
                else:
                    # cholero nie dziel przez zero
                    return None
        else:
            print('blaba')
            return self.visitChildren(ctx)
                
        
    def visitFunction_call(self, ctx:algoCodeParser.Function_callContext):
        func_name = ctx.TOK_VAR().getText()
        arguments = self.visitArguments(ctx.arguments())
            # obsługa specjalnych funkcji, na razie tylko print
        if func_name.lower() == 'print':
            print(arguments)
            # tutaj można dodać obsługę innych funkcji
       



    # Visit a parse tree produced by algoCodeParser#program.
    def visitProgram(self, ctx):
        self.visitCode(ctx.code())


    # Visit a parse tree produced by algoCodeParser#code.
    def visitCode(self, ctx:algoCodeParser.CodeContext):
        code_result = []
        for child in ctx.getChildren():
            code_result.append(self.visitStatement(child))
        print('success')
                

    # Visit a parse tree produced by algoCodeParser#argument.
    def visitArgument(self, ctx:algoCodeParser.ArgumentContext):
        #zwracam dziecko czyli argument
        var_name = ctx.getText()
        print(f"wartosc: {self.context[-1].get(var_name, None)}")
        return self.context[-1].get(var_name, None)


    # Visit a parse tree produced by algoCodeParser#arguments.
    def visitArguments(self, ctx:algoCodeParser.ArgumentsContext):
        arguments = []
        # Przechodze przez każdy argument
        if ctx.argument():
            for child in ctx.argument():
                arguments.append(self.visitArgument(child))
        return arguments

    # Visit a parse tree produced by algoCodeParser#statement.
    def visitStatement(self, ctx: algoCodeParser.StatementContext):
        if ctx.assignment():
            return self.visitAssignment(ctx.assignment())
        elif ctx.array_def():
            return self.visitArray_def(ctx.array_def())
        elif ctx.function_call():
            return self.visitFunction_call(ctx.function_call())
        elif ctx.for_loop():
            return self.visitFor_loop(ctx.for_loop())
        elif ctx.if_statement():
            return self.visitIf_statement(ctx.if_statement())
        elif ctx.if_else_statement():
            return self.visitIf_else_statement(ctx.if_else_statement())
        elif ctx.if_return_statement():
            return self.visitIf_return_statement(ctx.if_return_statement())
        elif ctx.while_statement():
            return self.visitWhile_statement(ctx.while_statement())
        else:
            raise ValueError("Unsupported statement context: {}".format(ctx.getText()))
        
        


    # Visit a parse tree produced by algoCodeParser#bool_expression.
    def visitBool_expression(self, ctx:algoCodeParser.Bool_expressionContext):
        left_operand = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right_operand = self.visit(ctx.getChild(2))
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
            # jeśli child jest tokenerm, sprawdzam typ i wartość
                token_type = child.getSymbol().type
                token_text = child.getText()
                if token_type == algoCodeParser.TOK_VAR:
                # Variable token
                # Perform any necessary actions, such as fetching its value from the context
                    pass
                elif token_type == algoCodeParser.TOK_NUM:
                # Numeric token
                # Convert its text to an integer
                    pass
                elif token_type in [algoCodeParser.TOK_IS_EQUAL, algoCodeParser.TOK_NOT_EQUAL, algoCodeParser.TOK_SMALLER, algoCodeParser.TOK_GREATER, algoCodeParser.TOK_GREATER_EQ, algoCodeParser.TOK_SMALLER_EQ]:
                # Comparison operator tokens
                    operator = token_text
                elif token_type in [algoCodeParser.TOK_AND, algoCodeParser.TOK_OR]:
                # Logical operator tokens
                    operator = token_text
                else:
                # Handle other token types if necessary
                    pass
            elif child.array_call():
            # If the child is an array call context, handle it accordingly
                pass
            elif isinstance(child, algoCodeParser.Bool_expressionContext):
            # If the child is another boolean expression context, recursively visit it
                pass




    # Visit a parse tree produced by algoCodeParser#for_loop.
    def visitFor_loop(self, ctx:algoCodeParser.For_loopContext):
        loop_var = ctx.TOK_VAR().getText()
        start = self.visitExpression(ctx.expression(0))
        end = self.visitExpression(ctx.expression(1))
        for current_value in range(start, end + 1):
            self.context[-1][loop_var] = current_value
            for statement in ctx.statement():
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
        print(f"Array defined: {arr_name} as empty dictionary")
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
    
    def visitChildren(self, ctx):
        result = []
        for child in ctx.children:
            result.append(self.visit(child))
        return result




del algoCodeParser
