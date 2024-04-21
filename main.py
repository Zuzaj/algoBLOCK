import lexer
import parser



def main():
    input_file = input("Please enter file name: ")
    tokens_list = lexer.scaner.scan_tokens("algorithms/"+input_file, lexer.tokens.tokens_dict)
    

main()