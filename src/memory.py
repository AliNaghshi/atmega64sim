from instructions import *
memory_external = {}
status_reg = [0 for i in range(8)] # C Z N V S H T I
reg_file = [0 for _ in range(32)]
instruction_memory = []
instruction = {
    "LDS": lds,
    "ADD": add,
    "CP": cp,
    "BRCC": brcc,
    "IN": inp,
    "COM": com,
    "OUT": out,
    "JMP": jmp,
    "ANDI": andi,
    "MUL": mul,
    "STS": sts,
    "NOP": nop,
}

pc = 0
ports_mem = {}





