import math
import re


dic = {}
file = open("processos.txt")
exp = re.compile('((?P<ano>\d{4})-).*?::(?P<nome>\w+).*?(?P<sobrenome>\w+)::')



for line in file.readlines():
    info = exp.search(line)
    
    if info != None:
        seculo = math.floor(int(info["ano"]) / 100) + 1
        
        if seculo not in dic.keys():
            dic[seculo] = {}
            
        for nome in [info['nome'],info['sobrenome']]:
            if nome not in dic[seculo].keys():
                dic[seculo][nome] = 1
            else:
                dic[seculo][nome] += 1
                
# Ordenar os sec por ordem crescente
dic = dict(sorted(dic.items(), key=lambda x: x[0]))

# Ordernar dicionário
for key,value in dic.items():
    dic[key] = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
    
          
for key,value  in dic.items():
    print("** TOP 5 [SEC " + str(key) + "] **")

    for i, (key,value) in enumerate(dic[key].items()):
        if (i>4):
            break
        print(str(i+1) + ". " + key + " (" +str(value)+")")
    print("")
    
            
        
