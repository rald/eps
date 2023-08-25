import sys

from Lexer import Lexer

f=open(sys.argv[1],"r")
s=f.read()
l=Lexer(s)
t=l.lex()
print(t)
