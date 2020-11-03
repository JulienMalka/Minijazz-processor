
class program:
    def __init__(self, input, output, var, equ):
        self.output = output
        self.var = var
        self.equlist = [equ]
        self.input = input

    def add_equ(self, equ):
        self.equlist.append((equ))


class op:
    def __init__(self, opname, oplist):
        self.oplist = oplist
        self.opname = opname



class equ:
    def __init__(self, var, op):
        self.var = var
        self.op = op

class input:
    def __init__(self, id):
        self.ids = [id]

    def add_id(self, id):
        self.ids.append(id)



class output:
    def __init__(self, id):
        self.ids = [id]

    def add_id(self, id):
        self.ids.append(id)


class vars:
    def __init__(self, id):
        self.ids = [id]

    def add_id(self, id):
        self.ids.append(id)