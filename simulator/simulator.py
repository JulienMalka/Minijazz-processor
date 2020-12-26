from par import parser
from operations import *
from scheduler import schedule
import click
import sys
from utils import convert_int
import pickle

def simulator(program, inputs, steps, rom=None):
    env = Env()
    for var in program.vars.varlist:
        env.add_var(var)

    for i in range(len(program.equlist)):
        equation = program.equlist[i]
        if equation.op.opname == "REG":
            env.add_reg(i)
        if equation.op.opname == "RAM" or equation.op.opname == "ROM":
            if equation .op.opname == "ROM" and rom is not None:
                env.add_mem(i, equation.op.arglist[0][0], equation.op.arglist[1][0], rom)
            else:
                env.add_mem(i, equation.op.arglist[0][0], equation.op.arglist[1][0])



    for step in range(steps):
        print("Cycle n° : " + str(step + 1))
        for varname, value in zip(program.input.ids, inputs[step]):
            env.update_var(varname, value)

        for i in range(len(program.equlist)):
            equation = program.equlist[i]
            env.update_var(equation.var, equation.op.execute(env, i))

        for varname in program.output.ids:
            value = env.get_var(varname)
            print("Value of " + varname + " : " + str(value) + " --> " + str(convert_int(value)))
        print("-------------------------------------------------------------")
        env.update_regs()
        env.update_memories()


def format_input(i):
    out = []
    for ch in i:
        out.append(int(ch))
    return out

def format_rom(rom_lines):
    result = []
    for i in range(len(rom_lines)-2):
        rom_hex = int(rom_lines[i][9:17], 16)
        bitstr = '{:032b}'.format(rom_hex)
        result.append([int(e) for e in bitstr])
    return result

@click.command()
@click.option('--netlist', help="The input netlist to simulate", required=True, type=click.File())
@click.option('--steps', help="The number of steps to simulate", required=True)
@click.option('--inputs', help="The inputs", type=click.File())
@click.option('--ROM', help="The rom initialisation", type=click.File())
@click.option('--scheduled', help="Scheduled program dump")

def main(netlist, steps, inputs=None, rom=None, scheduled=None):
    steps = int(steps)
    if steps <= 0:
        print("Unexpected value of steps. Try again.")
        sys.exit()
    netlist_data = netlist.read()
    program = parser.parse(netlist_data)
    input_nb = len(program.input.ids)
    expected_inputs = input_nb * steps
    if input_nb > 0 and inputs is None:
        print("Unexpected number of inputs (0 != " + str(expected_inputs) + "). Try again.")
        sys.exit()

    if inputs is None:
        inputs_formatted = [[]] * steps
    else:
        input_data = inputs.read()
        inputs = input_data.split("\n")
        while "" in inputs:
            inputs.remove("")
        if len(inputs) != expected_inputs:
            print("Unexpected number of inputs (" + str(len(inputs)) + " != " + str(expected_inputs) + "). Try again.")
            sys.exit()

        inputs_formatted = [inputs[i:i + input_nb] for i in range(0, len(inputs), input_nb)]
        for step in inputs_formatted:
            for i in range(len(step)):
                step[i] = format_input(step[i])
    if rom is not None:
        ROM_data = rom.read()
        ROM_lines = ROM_data.split("\n")
        print(len(ROM_lines))
        print(ROM_lines)
        rom = format_rom(ROM_lines)

    if scheduled is not None:
        with open(scheduled, 'rb') as program_file:
            scheduled_program = pickle.load(program_file)
    else:
        scheduled_program = schedule(program)
    simulator(scheduled_program, inputs_formatted, steps, rom)


if __name__ == "__main__":
    main()
