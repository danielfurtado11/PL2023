import re

dic = {}
file = open("processos.txt")
exp = re.compile(r",(?P<Relacao>(?:Pai|Filho|Irmao|Avo|Neto|Tio|Sobrinho|Mae|Primo|Tia|Prima|Sobrinha|Irma|Filha)\b[^.]*).")
dic = {}

for line in file.readlines():
    info = exp.findall(line)
    if info != []:
        for r in info:
            if r not in dic.keys():
                dic[r] = 1
            else:
                dic[r] +=1 
print(dic)