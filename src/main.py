from sys import argv as args
from os import system as shell

from lexer import lexer
from parser import parser
from compiler import compiler
#quit('enum vs union')
if len(args)!=2:
 print(f'usage: {args[0]} <file>')
 quit(1)

input=open(args[1]).read()

input=lexer(input)
#print('lexer out',input)

input=parser(input,'_start')
input=input[2]+input[1]+input[0]
print('parser out:',input)
#print(input[6].lexeme.src)
#quit(8)

code,data,bss,fns=compiler(input,'_start')

out=f"""global _start
segment .data
{data}
segment .bss
{bss}
segment .text
{fns}
_start:
{code}"""
open('out.asm','w').write(out)
shell('nasm -O0    -f elf64 -o out.o out.asm')
shell('ld out.o -o out.elf')
shell('rm out.o')
shell('strip out.elf')

'''

plan:
scops
recursion
fn prototype
loops
while
break
continue
type tjeking
gen yield

for loop
clean/spelchek
tests
git push

fn args fix
genrics
proper f-strings  \\xfe \\u64


arry indexing
import
inetsion
function overloat
type prototype
do while
conts/var/let/defualt
fn args from name to regist via context

make list of features
rethin unary and binary opts
stdlib tjeck notes

fizbuz
brain f*ck compiler program
calculator
Cimport
fractol
game of live via raylib
port compiler

documentation for language
documentation for convetions
documentation for libstd

rewite in abstraction-script whit a good plan ad beter varr names and context, function cald by main seprat from acl fn, not alwat 64bit size:
CLI
optamization
difrent archrstuers
tools


'''
