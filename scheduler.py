from operations import *
from graphs import Graph, Node

def read_exp(eqn):
    return eqn.op.oplist

def schedule(program):
    dependency_graph = Graph()
    equations = program.equlist
    ordered_equlist = []
    for equation in equations:
        dependency_graph.add_node(Node(equation.var))
        for var in read_exp(equation):
            dependency_graph.add_node(Node(var))
            dependency_graph.add_edge(var, equation.var)

    ordered_nodes = dependency_graph.topological_sort()
    for node in ordered_nodes:
        for equation in equations:
            if equation.var == node.label:
                ordered_equlist.append(equation)

    program.equlist = ordered_equlist
    return program

