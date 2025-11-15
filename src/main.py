
from os import error


try:
    inp = input()
    inputFile = open("{}".format(inp), "r")
except FileNotFoundError:
    print("there is no such file in this directory")
    raise error

try:
    for line in inputFile:
        s_line = line.split(" ")
        print(s_line)
except:
    inputFile.close()

