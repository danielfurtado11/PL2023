import re
import json

file = open("processos.txt")
exp = re.compile("(?P<pasta>\w+)::(?P<data>\d+.*?)::(?P<nome>\w+.*?)::(?P<pai>\w*.*?)::(?P<mae>\w*.*?)::(?P<obs>\w*.*)::")

i = 0
array = []

while i < 20:
    line = file.readline()
    info = exp.search(line)
    1
    if info != None:
        dic = info.groupdict()
        if dic['obs'] == '':
            del dic['obs']
    array.append(dic)
    i +=1


fileOut = open("file.json","w")
fileOut.write(json.dumps(array, indent=1))
file.close()
fileOut.close()