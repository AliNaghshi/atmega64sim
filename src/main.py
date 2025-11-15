import memory
try:
    inp = input()
    inputFile = open("{}".format(inp), "r")
except FileNotFoundError:
    print("there is no such file in this directory")
    raise FileNotFoundError()

lst = []
try:
    for line in inputFile:
        lst.append(line)
except:
    inputFile.close()

instructions = ['LDS', 'ADD', 'CP', 'BRCS', 'BREQ', 'IN', 'COM', 'OUT', 'JMP', 'ELSE', 'ANDI', 'LDI', 'MUL', 'OR', 'STS', 'END', 'NOP']
print(lst)
for i in lst:
    j = i.split(" ")
    if j[0] not in instructions:
        instructions.append(j[0])
print(instructions)

