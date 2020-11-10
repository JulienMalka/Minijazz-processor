from utils import convert_int


class Env:
    def __init__(self):
        self.vars = []
        self.regs = {}
        self.memories = {}

    def add_var(self, var):
        self.vars.append(var)

    def add_reg(self, i):
        self.regs[i] = Reg()

    def add_mem(self, i, addr_size, word_size):
        self.memories[i] = Memory(addr_size, word_size)

    def update_var(self, varname, value):
        for var in self.vars:
            if var.name == varname:
                var.value = value
                break

    def get_var(self, varname):
        for var in self.vars:
            if var.name == varname:
                return var.value
        raise Exception("Variable doesn't exist in this environment")

    def update_regs(self):
        for reg in self.regs.values():
            reg.tick(self)

    def update_memories(self):
        for mem in self.memories.values():
            mem.tick(self)


class Reg:
    def __init__(self):
        self.input = None
        self.output = [0]

    def tick(self, env):
        self.output = env.get_var(self.input)
        self.input = None


class Memory:
    def __init__(self, addr_size, word_size):
        self.memory = []
        nb_case = 2**addr_size
        case = [0] * word_size
        for i in range(nb_case):
            self.memory.append(case.copy())
        self.write = False
        self.writeaddr = None
        self.writedata = None

    def read_addr(self, addr):
        if len(addr) > 1:
            addr = convert_int(addr)
        return self.memory[addr]

    def write_addr(self, write, addr, value):
        self.write = write
        self.writeaddr = addr
        self.writedata = value

    def tick(self, env):
        if int(env.get_var(self.write)[0]):
            self.write = False
            addr = env.get_var(self.writeaddr)
            if len(addr) > 1:
                addr = convert_int(addr)
            value = env.get_var(self.writedata)
            self.memory[addr] = value


class Program:
    def __init__(self, input_block, output_block, vars_block, equ):
        self.output = output_block
        self.vars = vars_block
        self.equlist = [equ]
        self.input = input_block

    def add_equ(self, equ):
        self.equlist.append(equ)


class Exp:
    def __init__(self, opname, arglist):
        self.arglist = arglist
        self.opname = opname

    def execute(self, env, line):
        argvalues = []
        for arg in self.arglist:
            if isinstance(arg, Var):
                argvalues.append(env.get_var(arg.name))
            else:
                argvalues.append(arg)

        if self.opname == "NOT":
            return [int(not argvalues[0][0])]

        if self.opname == "AND":
            return [int(argvalues[0][0] and argvalues[1][0])]

        if self.opname == "OR":
            return [int(argvalues[0][0] or argvalues[1][0])]

        if self.opname == "NAND":
            return [int(not(argvalues[0][0] and argvalues[1][0]))]

        if self.opname == "XOR":
            return [argvalues[0][0] ^ argvalues[1][0]]

        if self.opname == "REG":
            env.regs[line].input = self.arglist[0].name
            return env.regs[line].output

        if self.opname is None:
            return argvalues[0]

        if self.opname == "SELECT":
            return [argvalues[1][argvalues[0][0]]]

        if self.opname == "CONCAT":
            return argvalues[0] + argvalues[1]

        if self.opname == "SLICE":
            return argvalues[2][argvalues[0][0]:argvalues[1][0]+1]

        if self.opname == "RAM":
            env.memories[line].write_addr(self.arglist[3].name, self.arglist[4].name, self.arglist[5].name)
            return env.memories[line].read_addr(argvalues[2])

        if self.opname == "ROM":
            return env.memories[line].read_addr(argvalues[2])

        if self.opname == "MUX":
            return argvalues[1] if argvalues[0][0] == 0 else argvalues[2]


class Equ:
    def __init__(self, var, op):
        self.var = var
        self.op = op

    def __repr__(self):
        return self.var + " = " + self.op.opname + " " + " ".join([str(elem) for elem in self.op.arglist])



class Input:
    def __init__(self):
        self.ids = []

    def add_id(self, id_):
        self.ids.append(id_)


class Output:
    def __init__(self):
        self.ids = []

    def add_id(self, id_):
        self.ids.append(id_)


class Vars:
    def __init__(self, var):
        self.varlist = [var]

    def add_var(self, var):
        self.varlist.append(var)


class Var:
    def __init__(self, name, length):
        self.name = name
        self.value = []
        for i in range(length):
            self.value.append(0)

    def __repr__(self):
        return self.name

