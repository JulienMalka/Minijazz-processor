from par2 import parser
from operations import *
from scheduler import schedule

def simulator(program, input, steps):
    env = Env()
    for var in program.vars.varlist:
        env.update_var(var.name, None)

    for i in range(steps):
        for varname, value in zip(program.input.ids, input[i]):
            env.update_var(varname, value)


        for equation in program.equlist:
            env.update_var(equation.var, equation.op.execute(env))

        for varname in program.output.ids:
            print(env.get_var(varname))





data = '''
INPUT a, b, c
OUTPUT s, r
VAR
  _l_1, _l_3, _l_4, _l_5, a, b, c, r, s
IN
r = OR _l_3 _l_5
s = XOR _l_1 c
_l_1 = XOR a b
_l_3 = AND a b
_l_4 = XOR a b
_l_5 = AND _l_4 c
'''

program = parser.parse(data)

scheduled_program = schedule(program)

simulator(scheduled_program, [[1,0,0]],1)
