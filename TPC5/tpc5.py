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
    global saldo
    euros = str(int(saldo/100))
    centimos = str(saldo)[-2:]
    string = euros+"e"+centimos+"c"
    return string    


def parseMoedas(moedas):
    global saldo
    dinheiro = ['10c', '20c', '50c', '1e', '2e']

    valores = re.findall(r'(\d+(?:c|e))',moedas)
    for valor in valores:
        if valor in dinheiro:
            tipo = valor[-1:]
            valor = int(valor[:-1])
            if tipo == 'e':
                saldo += valor * 100
            if tipo == 'c':
                saldo += valor
        else:
            print("maq: " + valor + " - moeda inválida")
    print("maq: saldo = " + calculaSaldo())

            
def parseNumero(numero):
    global saldo
    
    if (numero[:3] == "601" or numero[:3] == "641"):
        print("maq: Esse número é permitido neste telefone. Queira dicar novo número!")
    
    elif (numero[:2] == "00"):
        if (saldo > 150):
            saido -= 150
            print("maq: saldo = " + calculaSaldo())
        else:
            print("maq: Saldo Insuficiente")
    
    elif (numero[:3] == "800"):
        print("maq: saldo = " + calculaSaldo())
        
    elif (numero[:3]):
        if (saldo > 10):
            saldo -= 10
            print("maq: saldo = " + calculaSaldo())
        else:
            
            print("maq: Saldo Insuficiente")
    else: print("maq: Contacto inválido")   
        

def parse(token):
    global estado
    
    if (token.type == "LEVANTAR"):
        if (estado == 0):
            estado = 1
            print("maq: Introduza moedas.")
        else: print("maq; O telefone já se encontra levanto...")
    
    elif (token.type == "POUSAR"):
        if (estado == 1):
            saldoTotal = calculaSaldo()
            print("maq: Troco =" + saldoTotal + "; Volte sempre!")
        else: print("maq: O telefone já se encontra pousado...")
    
    elif (token.type == "MOEDA"):
        if (estado == 0):
            print("maq: O telefone está pousado...")
        else: parseMoedas(token.value)
    
    elif (token.type == "CONTACTO"):
        if (estado == 0):
            print("maq: O telefone está pousado...")
        else: parseNumero(token.value)
    
    elif (token.type == "ABORTAR"):
        estado = 2
    else:
        print("Erro no input")


lexer = lex.lex()

while(True):
    line = input(">> ")
    lexer.input(line)
    for token in lexer:
        parse(token)
        if (estado == 2): 
            break
        