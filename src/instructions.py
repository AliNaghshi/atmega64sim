import memory as mem
from Exceptions import *

# create instructions

def lds(reg_num, addrs):
    if addrs not in mem.memory_external:
        raise NotAccessedRegion()
    else:
        mem.reg_file[reg_num] = mem.memory_external[addrs]

def add(reg_d, reg_o):
    # change status register
    # handle carries
    mem.reg_file[reg_d] += mem.reg_file[reg_o]

def cp(reg_d, reg_o):
    # set status register by reg_d - reg_o
    pass

def brcc(addrs):
    if mem.status_reg[0] == 0:
        mem.pc = addrs

