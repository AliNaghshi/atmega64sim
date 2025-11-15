from memory import *
try:
    inp = input()
    inputFile = open("{}".format(inp), "r")
except FileNotFoundError:
    print("there is no such file in this directory")
    raise FileNotFoundError()

lst = []
line_num  = 0
labels = {}
try:
    for line in inputFile:
        word = line.split(" ")[0]
        if word not in instruction:
            labels[word] = line_num
        else:
            lst.append(line)
            line_num += 1
except:
    inputFile.close()

for i in lst:
    words = i.strip().split(" ")
    inst = instruction[words[0]]
    params = []
    for i in words[1:]:
        params.append(i)
    instl = [inst, params]
    instruction_memory.append(instl)


# run the code
pc = 0
while True:
    run(instruction_memory, pc)


print(lst)

