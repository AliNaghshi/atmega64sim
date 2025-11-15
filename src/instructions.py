import memory as mem
from Exceptions import *


def set_status_register(a):
    if a > 255:
        mem.status_reg[0] = 1
    if a == 0:
        mem.status_reg[1] = 1
    if a - 128 > 0 and a <= 255:
        mem.status_reg[2] = 1
    # implement the rest


def nop():
    pass

def lds(reg_num, addrs):
    if addrs not in mem.memory_external:
        raise NotAccessedRegion()
    else:
        mem.reg_file[reg_num] = mem.memory_external[addrs]

def add(reg_d, reg_o):

    # handle overfolws
    mem.reg_file[reg_d] += mem.reg_file[reg_o]
    set_status_register(mem.reg_file[reg_d])

def cp(reg_d, reg_o):
    set_status_register(mem.reg_file[reg_d] - mem.reg_file[reg_o])
    pass

def brcc(addrs):
    if mem.status_reg[0] == 0:
        mem.pc = addrs

def inp(reg_num, prt):
    if prt not in mem.ports_mem:
        raise InvalidBoundary()
    mem.reg_file[reg_num] = mem.ports_mem[prt]

def com(reg_num):
    # handle zero flag
    mem.reg_file[reg_num] = ~ mem.reg_file[reg_num]


def out(reg_num, prt):
    if prt not in mem.ports_mem:
        raise InvalidBoundary()
    mem.ports_mem[prt] = mem.reg_file[reg_num]

def jmp(addrs):
    mem.pc = addrs

def andi(reg_num, imm):
    if not (-128 <= imm <= 127):
        raise InvalidImmideate()
    if reg_num < 16:
        raise UnallowedRegister()

    mem.reg_file[reg_num] &= imm
    set_status_register(mem.reg_file[reg_num])


def mul(reg_d, reg_o):
    a = (mem.reg_file[reg_o] * mem.reg_file[reg_d])
    set_status_register(a)
    mem.reg_file[0] = a & 255
    mem.reg_file[1] = (a >> 8) & 255

def sts(addrs, reg_num):
    mem.memory_external[addrs] = mem.reg_file[reg_num]


