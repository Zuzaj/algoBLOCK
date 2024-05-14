# Generated from algoCode.g4 by ANTLR 4.13.1
from antlr4 import ParseTreeVisitor
from antlr4 import *
if "." in __name__:
    from .algoCodeParser import algoCodeParser
else:
    from algoCodeParser import algoCodeParser



# This class defines a complete generic visitor for a parse tree produced by algoCodeParser.

class algoCodeVisitor(ParseTreeVisitor):

    def __init__(self):
        self.context = [{}] 
        self.functions = []

    def visitProgram(self, ctx):
        self.visitCode(ctx.code())

    def visitCode(self, ctx:algoCodeParser.CodeContext):
        if ctx.function_def():
            for child in ctx.function_def():
                self.visitFunction_def(child)        
        if ctx.statement():
            for child in ctx.statement():
                self.visitStatement(child)
    
    
    def visitFunction_def(self, ctx:algoCodeParser.Function_defContext):
        function_name = ctx.TOK_VAR().getText()
        arguments = []
        statements = []
        return_statement = []

        arguments_ctx = ctx.arguments()
        if arguments_ctx:
            arguments = self.visitArguments(arguments_ctx)

        statement_ctxs = ctx.statement()
        for statement_ctx in statement_ctxs:
            statements.append(statement_ctx)

        return_statement = ctx.return_statement()
        self.functions.append(function_name)
        self.context[-1][function_name] = {}
        self.context[-1][function_name]["params"] = (arguments, statements, return_statement)

        print("visited function def")

    
    
    def visitAssignment(self, ctx:algoCodeParser.AssignmentContext):
        left_value = ctx.getChild(0).getText() 
        value = self.visitExpression(ctx.expression())
        if ctx.array_call():
            array_call = ctx.getChild(0)
            array_name = array_call.TOK_VAR().getText()
            index = self.visitExpression(ctx.array_call().expression())
            #sprawdzam czy tablica zainicjowana
            if array_name not in self.context[-1]:
                self.context[-1][array_name] = []
                print("tablica nie zdefiniowana")
                return None
        
            while len(self.context[-1][array_name]) <= index:
                self.context[-1][array_name].append(None)
            self.context[-1][array_name][index] = value
        else:
            self.context[-1][left_value] = value
        return value
    
    def visitExpression(self, ctx: algoCodeParser.ExpressionContext):
            # If the expression is a variable
        if  ctx.getChildCount() == 1:  
            if ctx.TOK_VAR():
                var_name = ctx.TOK_VAR().getText()
                return self.context[-1].get(var_name, None)
            
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
            left_operand = self.visitExpression(ctx.expression(0))
            right_operand = self.visitExpression(ctx.expression(1))
            operator = ctx.getChild(1).getText()
            
            if left_operand and right_operand:
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
        # else:
        #     return self.visitChildren(ctx)
                
        
    def visitFunction_call(self, ctx:algoCodeParser.Function_callContext):
        func_name = ctx.TOK_VAR().getText()
        arguments = self.visitArguments(ctx.arguments())
            # obsługa  print
        if func_name.lower() == 'print':
            for arg in arguments:
                print(arg)

            # inne funkcji
        elif func_name in self.context[-1]:
            function_definition = self.context[-1][func_name]["params"]
            if len(arguments) != len(function_definition[0]):
                print(f"Error: Function '{func_name}' expects {len(function_definition[0])} arguments, but {len(arguments)} were provided.")
                return None
            output = self.execute_statements(function_definition[0], arguments, function_definition[1], function_definition[2], func_name)
            print("visited function call ")
            if output:
                return output
        else:
            raise ValueError(f"Function '{func_name}' is not defined.")
        
    def execute_statements(self, func_args, call_args, func_statements, func_return, f_name):
        # dla kazdej funkcji słownik ze zmiennymi
        for arg_name, arg_value in zip(func_args, call_args):
            self.context[-1][f_name][arg_name] = arg_value
        output = None
        for statement_ctx in func_statements:
            self.visitStatement(statement_ctx)
        if func_return:
            output = self.visitReturn_statement(func_return)
        return output
        
       
    def visitArgument(self, ctx:algoCodeParser.ArgumentContext):
        if ctx.expression():
            return self.visitExpression(ctx.expression())
        else:
            return None


    def visitArguments(self, ctx:algoCodeParser.ArgumentsContext):
        arguments = []
        if ctx.argument():
            for child in ctx.argument():
                arguments.append(self.visitArgument(child))
        return arguments

   
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
        print("visited statement")
        


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


    def visitArray_def(self, ctx:algoCodeParser.Array_defContext):
        arr_name = ctx.TOK_VAR().getText()
        self.context[-1][arr_name] = []
        print(f"Tablica zainicjalizowana {arr_name} ")
        return None


    def visitArray_call(self, ctx:algoCodeParser.Array_callContext):
        arr_name = ctx.TOK_VAR().getText()  
        if(ctx.expression().TOK_VAR()):
            index_expression_name = ctx.expression().getText()
            index_expression =  self.context[-1].get(index_expression_name, None)
        else:
            index_expression = int(ctx.expression().getText())
    
        try:
            value = self.context[-1][arr_name][index_expression]
            print(f"Dodaj do tablicy '{arr_name}' na index {index_expression} wartosc {value}")
            return value
        except IndexError:
            return None 
        
        
    def visitReturn_statement(self, ctx:algoCodeParser.Return_statementContext):
        value = self.context[-1].get(ctx.getChild(1).getText())
        print("visited return")
        return value
    
    def visitChildren(self, ctx):
        result = []
        for child in ctx.children:
            result.append(self.visit(child))
        return result



del algoCodeParser
