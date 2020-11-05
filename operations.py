class Env:
    def __init__(self):
        self.vars = {}

    def update_var(self, varname, value):
        self.vars[varname] = value

    def get_var(self, varname):
        return self.vars.get(varname, "ERREUR")




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

    def execute(self, env):
        argvalues = []
        for arg in self.arglist:
            if type(arg) == type(Var("test")):
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





class Equ:
    def __init__(self, var, op):
        self.var = var
        self.op = op

class Input:
    def __init__(self, id):
        self.ids = [id]

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
    def __init__(self, name):
        self.name = name