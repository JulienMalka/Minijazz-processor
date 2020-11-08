from par import parser
from operations import *
from scheduler import schedule

def simulator(program, input, steps):
    env = Env()
    for var in program.vars.varlist:
        env.add_var(var)

    for i in range(len(program.equlist)):
        equation = program.equlist[i]
        if equation.op.opname == "REG":
            env.add_reg(i)

    for i in range(steps):
        if i !=0:
            env.update_regs()
        for varname, value in zip(program.input.ids, input[i]):
            env.update_var(varname, value)


        for i in range(len(program.equlist)):
            equation = program.equlist[i]
            env.update_var(equation.var, equation.op.execute(env, i))

        for varname in program.output.ids:
            print(env.get_var(varname))





data = '''
INPUT 
OUTPUT o
VAR
  _l_2, c, o
IN
c = NOT _l_2
o = REG c
_l_2 = REG o
'''

program = parser.parse(data)

scheduled_program = schedule(program)

simulator(scheduled_program, [[],[],[],[],[],[],[],[],[],[]],10)
