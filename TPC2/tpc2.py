valor = 1
c = 0
i = 0
while valor == 1:
    
    x = input()
    if (i == 1 and x != "=" and x.lower() != "off" and x.lower() != "on"):
        c += int (x)
    if (x == "="):
        print(c)
    if (x.lower() == "on"):
        i = 1
    if (x.lower() == "off"):
        i = 0