
# possible token's types :
# 'TOK_OP'
# 'TOK_KEYWORD'
# 'TOK_VAR'
# 'TOK_EOF'
# 'TOK_SPACE'
# 'TOK_NUM'
# 'TOK_NL'


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"\"{self.type}\" : \"{str(self.value)}\""
