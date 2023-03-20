import ply.lex as lex
import re

tokens = (
    "LEVANTAR",
    "POUSAR",
    "MOEDA",
    "NUMERO",
    "ABORTAR",
)

t_LEVANTAR = r"LEVANTAR"
t_POUSAR = r"POUSAR"
t_ABORTAR = r"ABORTAR"

saldo = 0

estado = 0  # 0: pousado | 1: levantado | 2: abortar


def t_MOEDA(t):
    r"MOEDA\s((\d+[c|e][,|\.]\s?)+)"
    match = re.match(r"MOEDA\s((\d+[c|e][,|\.]\s?)+)", t.value)
    t.value = match.group(1)
    return t

def t_NUMERO(t):
    r"T=(00\d*|\d{9}\b)"
    match = re.match(r"T=(00\d*|\d{9}\b)",t.values)
    t.value = match.group(1)
    return t


def t_error(t):
    print("ERRO!")
    t.lexer.skip(1)
    
def t_whitespace(t):
    r"\s+"
    pass


def calculaSaldo():

def parseMoedas(moedas):

def parseNumero(numero):

def parse(token):

lexer = lex.lex()

while(True):
    line = input(">> ")
    lexer.input(line)
    for token in lexer:
        parse(token)
        if (estado == 2): 
            break
        