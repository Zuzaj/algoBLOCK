from tokens import Token
from tokens_dict import tokens_dict

class Scanner:
    def __init__(self, text, tokens_table):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.tokens_table = tokens_table

    def error(self, message):
        raise Exception(f"Error: {message} at column {self.pos + 1}")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer_float(self):
        result = ''
        is_float = False
        while self.current_char is not None:
            if self.current_char.isdigit():
                result += self.current_char
                self.advance()
            if self.current_char == '.':
                is_float = True
                result += self.current_char
                self.advance()
            else:
                break
        if is_float:
            return float(result)
        else:
            return int(result)

    
    def keywords(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char =='_') :
            result += self.current_char
            self.advance()
        return result

    def scan(self):
        if self.current_char is not None:
            if self.current_char.isspace():
                if self.current_char == '\n':
                    sign = '\n'
                    self.advance()
                    return Token('TOK_NL',sign)
                char = self.current_char
                self.advance()
                return Token("TOK_SPACE", char) 

            if self.current_char.isdigit():
                return Token('TOK_NUM', self.integer_float())
            
            if self.current_char.isalpha():
                result = self.keywords()
                if result in tokens_dict['Keyword']:
                    return Token('TOK_KEYWORD', result )
                else:
                    return Token('TOK_VAR', result)
            if self.current_char in tokens_dict['Operator'] or self.current_char =='+':
                operator = self.current_char
                self.advance()
                return Token('TOK_OP', operator)
            self.error("Invalid character")
    

def scan_tokens(input_file, possible_tokens):
    with open(input_file, 'r') as f:
        text = f.read()
    tokens = []
    while True:
        if not text:
            break
        scanner = Scanner(text, possible_tokens)
        try:
            while True:
                token = scanner.scan()
                if token.type == 'EOF':
                    break
                tokens.append(token)
        except Exception as e:
            print(e)
        return tokens
    
def main():
    input_file = input("Please enter file name: ")
    tokens_list = scan_tokens("algorithms/"+input_file, tokens_dict)
    for token in tokens_list:
        print(token)
    return tokens_list

main()