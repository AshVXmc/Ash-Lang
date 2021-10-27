from src.ash import *

def run():
    # print("$> ")
    # filenameinput = input()
    # data = openfile(filenameinput)
    data = openfile("test.ash")
    tokens = lexer(data)
    parser(tokens)

# Method run
run()  