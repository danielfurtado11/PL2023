c = 0
i = 0

print("Insira dígitos para realizar uma soma:")
while 1:
    
    line = input(">> ")
    numbers = ""

    if line.lower() == "on":
        i = 1
    
    if line.lower() == "off":
        i = 0

    if line == "=":
        print(c)
        
    if i == 1:
        for caracter in line:
            if caracter.isdigit():
                numbers += caracter

            else:
                if numbers != "":
                    c += int(numbers)
                numbers = ""
        if numbers != "":
            c += int(numbers)
            numbers = ""
