import ply.lex as lex
import re


tokens = (
    "CONDICAO",
    "CICLO",
    "COMENTARIO",
    "COMENTARIOPLUS",
    "PROGRAM",
    "FUNC",
    "TIPO",
    "SIZE",
    "NUM",
    "VARIAVEL",
    "OPERADOR",
    "FIMSTRING",
    "INTERVALO",
    "CHAVETASINIT", 
    "CHAVETASFIM",
    "PARENTINIT",
    "PARENTFIM"
)

t_CONDICAO = r"if|else|in\s"
t_CICLO = r"while|for"
t_COMENTARIO = r"\/\/.*"
t_COMENTARIOPLUS = r"\/\*(.|\n)*\*\/"

def t_PROGRAM(t):
    r"program\s(\w+)"
    result = re.match(r"program\s(\w+)", t.value)
    t.value = result.group(1)
    return t

t_FUNC = r"(function\s)?\w+(?=\()"
t_TIPO = r"int"
t_SIZE = r"\[\w+\]"
t_NUM = r"\d+"
t_VARIAVEL = r"\w+"
t_OPERADOR = "\+|-|\*|%|=|<|>|\,"
t_FIMSTRING = r";"
t_INTERVALO = r"\[\d+\.\.\d+\]"
t_CHAVETASINIT = r"{"
t_CHAVETASFIM = r"}"
t_PARENTINIT = r"\("
t_PARENTFIM = r"\)"

def t_whitespace(t):
    r"\s+"
    pass

def t_error(t):
    print(f"Inválido: '{t.value[0]}'")
    t.lexer.skip(1)



lexer = lex.lex()
file = input(">> ")

f = open(file,"r")
text = ""

for line in f.readlines():
    text += line
f.close()

lexer.input(text)

for token in lexer:
    print(token)

