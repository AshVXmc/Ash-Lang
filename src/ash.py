from sys import *
from src.tokens import *


def openfile(file_name):
    data = open(file_name, "r").read()
    return data

tokens = []

# LEXER
def lexer(filecontents):
    token = ""
    state = 0
    string = ""
    expression = ""
    n = ""
    filecontents = list(filecontents)

    for char in filecontents:
        token += char
        if token == " ":
            if state == 0:
                token = ""
            else:
                token = " "
        elif token == "\n" or token == EOF:
            token = ""
            if expression != "":
                print(expression)
                expression = ""
        elif token in NUMBERS:
            expression += token
            token = ""
        elif token == ADD:
            expression += token
            token = ""
        elif token == "echo" or token == "ECHO":
            tokens.append("ECHO")
            token = ""
        elif token == "typeof" or token == "TYPEOF":
            tokens.append("TYPEOF")
            token = "" 
        elif token == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING: " + string + "\"")
                string = ""
                state = 0
                token = ""
        elif state == 1:
            string += token
            token = ""
    return tokens

# Parser
def parser(tokens):
    i = 0
    while (i < len(tokens)):
        # token print debug
        # Start from the 6th letter in STRING
        if tokens[i] + " " + tokens[i + 1][0:6] == "ECHO STRING":
            # Starts with 7 to exclude the colon
            print(tokens[i+1][7:])
            i += 2
            print(tokens)
        if tokens[i] + " " + tokens[i + 1][0:6] == "TYPEOF STRING":
                # Starts with 7 to exclude the colon
            print(type(tokens[i+1][8:]))
            i += 2
            print(tokens)

        
        
