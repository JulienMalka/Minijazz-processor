class Env:
    def __init__(self):
        self.vars = []
        self.regs = {}

    def add_var(self, var):
        var.value = 0
        self.vars.append(var)

    def add_reg(self, i):
        self.regs[i] = Reg()



    def update_var(self, varname, value):
        for var in self.vars:
            if var.name == varname:
                var.value = value
                break

    def get_var(self, varname):
        for var in self.vars:
            if var.name == varname:
                return var.value
        return "Erreur"

    def update_regs(self):
        for reg in self.regs.values():
            reg.tick(self)




class Reg:
    def __init__(self):
        self.input = None
        self.output = 0

    def tick(self, env):
        self.output = env.get_var(self.input)
        self.input = None


class Program:
    def __init__(self, input, output, vars, equ):
        self.output = output
        self.vars = vars
        self.equlist = [equ]
        self.input = input

    def add_equ(self, equ):
        self.equlist.append((equ))


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
            return int(not argvalues[0])

        if self.opname == "AND":
            return int(argvalues[0] and argvalues[1])

        if self.opname == "OR":
            return int(argvalues[0] or argvalues[1])

        if self.opname == "NAND":
            return int(not(argvalues[0] and argvalues[1]))

        if self.opname== "XOR":
            return argvalues[0] ^ argvalues[1]

        if self.opname == "REG":
            env.regs[line].input = argvalues[0]
            return env.regs[line].output





class Equ:
    def __init__(self, var, op):
        self.var = var
        self.op = op

class Input:
    def __init__(self):
        self.ids = []

    def add_id(self, id):
        self.ids.append(id)

class Output:
    def __init__(self, id):
        self.ids = [id]

    def add_id(self, id):
        self.ids.append(id)


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
            self.value.append(None)
