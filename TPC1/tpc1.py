import csv 




def menu():
    print("------------------------------- Menu -------------------------------\n")
    print(" [1] - Consultar distribuição da doença por sexo.")
    print(" [2] - Consultar distribuição da doença por escalões etários.")
    print(" [3] - Consultar distribuição da doença por níveis de colesterol.")
    print(" [0] - Sair.\n")
    print("--------------------------------------------------------------------")
    

def drawSexo(list):
    print("\n\n----------------------------------------------------------")
    print("  -> Total Sexo Masculino:  " + str(list[0][1]) )
    print("  -> Doentes Sexo Masculino:  " + str(list[0][0]))
    print("  -> Total Sexo Feminino:  " + str(list[1][1]))
    print("  -> Doentes Sexo Feminino:  " + str(list[1][0]))
    print("  -> % Doentes Sexo Masculino: " + str((list[0][0] / list[0][1]) * 100) + "%")
    print("  -> % Doentes Sexo Feminino: " + str((list[1][0] / list[1][1]) * 100) + "%")
    print("----------------------------------------------------------\n\n")
    
    


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
  csvreader = list(csv.reader(file))
  csvreader.pop(0)
  for row in csvreader:
    table.append(row)
sexo = doencaPorSexo(table)
idade = doencaPorIdade(table)
colesterol = doencaPorColesterol(table)


while (1):
    menu()
    c = input("Escolha uma opção: ")
    if (c == "1"):
        drawSexo(sexo)
    if (c == "2"):
        print(idade)
    if (c == "3"):
        print(colesterol)
    if (c == "0"):
        break
        
        







