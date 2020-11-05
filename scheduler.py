from operations import *
from graphs import Graph, Node


def extract_var(arglist):
    vars_list = []
    for elem in arglist:
        if type(elem) == type(Var("dummy")):
            vars_list.append(elem.name)
    return vars_list

def read_exp(exp):
    if exp.opname == "REG":
        return []
    else:
        return extract_var(exp.arglist)

def schedule(program):
    dependency_graph = Graph()
    equations = program.equlist
    ordered_equlist = []
    for equation in equations:
        dependency_graph.add_node(Node(equation.var))
        for var in read_exp(equation.op):
            dependency_graph.add_node(Node(var))
            dependency_graph.add_edge(var, equation.var)

    ordered_nodes = dependency_graph.topological_sort()
    for node in ordered_nodes:
        for equation in equations:
            if equation.var == node.label:
                ordered_equlist.append(equation)

    program.equlist = ordered_equlist
    return program

