

def menu():
    print("\n\n+-------------------------- Menu ---------------------------+")
    print("|  {:<57}|".format(" [1] - Distribuição da doença por sexo."))
    print("|  {:<57}|".format(" [2] - Distribuição da doença por escalões etários."))
    print("|  {:<57}|".format(" [3] - Distribuição da doença por níveis de colesterol."))
    print("|  {:<57}|".format(" [0] - Sair."))
    print("+-----------------------------------------------------------+")
    

def drawSexo(list):
    print("\n\n+-------------------------------------------+")
    print("|              Doença por Sexo              |")
    print("+----------+----------+----------+----------+")
    print("|   Sexo   | Doentes  |   Total  |    (%)   |")
    print("+----------+----------+----------+----------+")
    print('|  {:<8}|  {:<8}|  {:<8}|  {:<8}|'.format("Homem",str(list[0][0]),str(list[0][1]), str("{:.2f}%".format((list[0][0] / list[0][1]) * 100))))
    print("+----------+----------+----------+----------+")
    print('|  {:<8}|  {:<8}|  {:<8}|  {:<8}|'.format("Mulher",str(list[1][0]),str(list[1][1]), str("{:.2f}%".format((list[1][0] / list[1][1]) * 100))))
    print("+----------+----------+----------+----------+\n\n")
    
def drawIdade(dicionario):
    
    print("\n\n+--------------------------------------------------+")
    print("|             Doença por Escalão Etário            |")
    print("+-----------------+----------+----------+----------+")
    print("|   Esc. Etário   | Doentes  |   Total  |    (%)   |")
    print("+-----------------+----------+----------+----------+")
    for key in dicionario:
        print("|      {:<11}|  {:<8}|  {:8}|  {:<8}|".format(str(key)+"-"+str(key+4), str(dicionario[key][0]), str(dicionario[key][1]), str("{:.2f}%".format((dicionario[key][0] / dicionario[key][1]) * 100))))
        print("+-----------------+----------+----------+----------+")
    

    
def drawColesterol(tuplo):
    print("\n\n+-------------------------------------------+")
    print("|       Doença por Nível de Colesterol      |")
    print("+---------------------+----------+----------+")
    print("|   Nvl. Colesterol   | Doentes  |   Total  |")
    print("+---------------------+----------+----------+")
    dicionario = tuplo[1]
    for key in dicionario:
        print("|        {:<13}|  {:<8}|  {:<8}|".format(str(key) + "-" + str(key+9), str(dicionario[key][0]), str(dicionario[key][1]), ))
        print("+---------------------+----------+----------+")   
    print("|        {:<13}|  {:<8}|  {:<8}|".format("**Erro**","-",str(tuplo[0]),"-"))
    print("+---------------------+----------+----------+")   
    


def doencaPorSexo(table):
    list = [[0,0],[0,0]] # [[M Doente, M Total],[F Doente, F Total]]
    for line in table:
        
        # Conta o número de pessoas de cada sexo
        if line[1] == "M":
            list[0][1] +=1
        else:
            list[1][1] +=1
        
        # Verifica quem tem a doença
        if line[1] == "M" and line[5] == "1":
            list[0][0] +=1
        elif line[1] == "F" and line[5] == "1":
            list[1][0] +=1
    return list
            
         
def doencaPorIdade(table):
    min = 100
    max = 0
    # verificar qual a idade máxima para conseguir saber qual o nível mínimo e máximo
    for line in table:
        if int(line[0]) > max:
            max = int(line[0])
        if int(line[0]) < min:
            min = int(line[0])

    # Cria um dicionário com os intervalos e com uma lista [Nº de Doentes, Nº Total]
    doencas = {i: [0,0] for i in range ((min // 5)*5, (max // 5) * 5 + 1, 5)}
          
    # Adiciona ao dicionário todos os dados    
    for line in table:
        for key in doencas:
            if int(line[0]) >= key and int(line[0]) < (key+5):
                if line[5] == "1":
                    doencas[key][0] +=1
                doencas[key][1] +=1
    return doencas
            

def doencaPorColesterol(table):
    min = 10000
    max = 0
    zero = 0
    for line in table:
        if line[3] == "0":
            zero +=1
        if int(line[3]) > 0 and int(line[3]) < min:
            min  = int(line[3])
        if int(line[3]) > max:
            max = int(line[3])

    colesterol = {i:[0,0] for i in range (min,max+1,10)}
    
    for line in table:
        for key in colesterol:
            if int(line[3]) >=key and int(line[3]) < (key+10):
                if line[5] == "1":
                    colesterol[key][0] +=1
                colesterol[key][1] +=1

    return (zero,colesterol)
    
            
    


    

        
    

table = []
with open("myheart.csv", 'r') as file:
  for line in file.readlines():
        line = line[:-1]
        table.append(line.split(','))
table.pop(0)
sexo = doencaPorSexo(table)
idade = doencaPorIdade(table)
colesterol = doencaPorColesterol(table)

while (1):
    menu()
    c = input("Escolha uma opção: ")
    if (c == "1"):
        drawSexo(sexo)
    if (c == "2"):
        drawIdade(idade)
    if (c == "3"):
        drawColesterol(colesterol)
    if (c == "0"):
        break
        
        





