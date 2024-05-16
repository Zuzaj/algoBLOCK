from antlr4 import *
from compiler.algoCodeLexer import algoCodeLexer
from compiler.algoCodeParser import algoCodeParser
from compiler.algoCodeListener import algoCodeListener
from compiler.algoCodeVisitor import algoCodeVisitor
from antlr4.tree.Tree import *

from antlr4 import ParserRuleContext
import tkinter as tk
from tkinter import simpledialog
from antlr4 import FileStream, CommonTokenStream
import io
import sys
from PIL import Image, ImageTk

def save_and_process_code():
    code = text_area_input.get("1.0", tk.END)

    with open('algorithms/algo0.txt', 'w', encoding='utf-8') as file:
        file.write(code)

    try:
        input_stream = FileStream('algorithms/algo0.txt', encoding='utf-8')
        lexer = algoCodeLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = algoCodeParser(stream)
        tree = parser.program()
        visitor = algoCodeVisitor()

        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output
        visitor.visitProgram(tree)

        sys.stdout = old_stdout
        output = redirected_output.getvalue()
        text_area_output.delete("1.0", tk.END)
        text_area_output.insert("1.0", output)
    except Exception as e:
        text_area_output.delete("1.0", tk.END)
        text_area_output.insert("1.0", str(e))

def basic():
    input_stream = FileStream('algorithms/algo0.txt', encoding='utf-8')
    lexer = algoCodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = algoCodeParser(stream)
    tree = parser.program() 
    print(tree.toStringTree(recog=parser))

    visitor = algoCodeVisitor()
    visitor.visitProgram(tree)

def interface():
    def function_def_code():
        root.clipboard_clear() 
        code = """
function myFunction(arg1)
    
endfunction
"""
        root.clipboard_append(code) 

    def if_code():
        root.clipboard_clear() 
        code = """
if  then ->
    
>-
"""
        root.clipboard_append(code) 

    def if_else_code():
        root.clipboard_clear() 
        code = """
if  then ->
    
>- else ->
    
>-
"""
        root.clipboard_append(code) 

    def while_code():
        root.clipboard_clear() 
        code = """
while  do ->
    
>-
"""
        root.clipboard_append(code) 

    def for_code():
        root.clipboard_clear() 
        code = """
for i = 1 to 10 do ->
    
>-
"""
        root.clipboard_append(code) 
        
    root = tk.Tk()
    root.title("AlgoBlock")
    root.configure(bg='light blue')


    frame = tk.Frame(root, bg='light blue')
    frame.pack(expand=True, fill=tk.BOTH)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    options_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Słowa kluczowe", menu=options_menu)
    options_menu.add_command(label="Definicja funkcji", command=function_def_code)
    options_menu.add_command(label="Instrukcja IF", command=if_code)
    options_menu.add_command(label="Instrukcja IF_ELSE", command=if_else_code)
    options_menu.add_command(label="Pętla WHILE", command=while_code)
    options_menu.add_command(label="Pętla FOR", command=while_code)

    global text_area_input
    text_area_input = tk.Text(frame, height=30, width=60, bg="black", fg="white", insertbackground='white')
    text_area_input.pack(side=tk.LEFT, padx=15, pady=15, expand=True, fill=tk.BOTH)

    global text_area_output
    text_area_output = tk.Text(frame, height=30, width=60, bg="black", fg="white", insertbackground='white')
    text_area_output.pack(side=tk.RIGHT, padx=15, pady=15, expand=True, fill=tk.BOTH)

    button_save_process = tk.Button(root, text="RESULT", command=save_and_process_code, font=("Helvetica", 12), bg="black", fg="black")
    button_save_process.pack(pady=15)

    root.mainloop()
    



def main():
    #interface()
    
    basic()
    

if __name__ == '__main__':
    main()
