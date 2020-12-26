from operations import *
from graphs import *
import pickle

def extract_var(arglist):
    vars_list = []
    for elem in arglist:
        if isinstance(elem, Var):
            vars_list.append(elem.name)
    return vars_list


def read_exp(exp):
    if exp.opname == "REG":
        return []
    elif exp.opname == "ROM":
        return []
    elif exp.opname == "RAM":
        return extract_var([exp.arglist[2]])
    else:
        return extract_var(exp.arglist)


def schedule(program):
    dependency_graph = Graph()
    equations = program.equlist
    ordered_equlist = []
    i = 0
    for equation in equations:
        dependency_graph.add_node(Node(equation.var))
        for var in read_exp(equation.op):
            dependency_graph.add_node(Node(var))
            dependency_graph.add_edge(var, equation.var)
    try:
        ordered_nodes = dependency_graph.topological_sort()
    except CycleError:
        print("blabla")
    for node in ordered_nodes:
        for equation in equations:
            if equation.var == node.label:
                ordered_equlist.append(equation)

    program.equlist = ordered_equlist
    with open('program.save', 'wb') as program_file:
        pickle.dump(program, program_file)
    return program

