from sys import argv as args

from lexer import lexer

if len(args)!=2:
    print('error: cmd file')
    exit(1)

fd=open(args[1])
input=fd.read()

lexed=lexer(input)

print(lexed)