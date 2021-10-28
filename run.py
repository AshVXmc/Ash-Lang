from src.ash import *

def run():
    inp = input()
    if inp.startswith("ash"):
        filename = inp.replace(inp[0:4], "", 1)  
        data = openfile(filename)
        tokens = lexer(data)
        parser(tokens)

# Method run
run()  