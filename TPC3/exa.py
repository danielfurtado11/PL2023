import re

dic = {}

file = open("processos.txt")
exp = re.compile('((\d{4})-)')

for line in file.readlines():
   ano = exp.search(line)
   
   if ano != None:
        if ano[2] not in dic.keys():
           dic[ano[2]] = 1
        else:
            dic[ano[2]] +=1

print(dic)