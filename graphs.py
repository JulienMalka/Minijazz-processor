class Graph:
    def __init__():
        self.nodes = []


    def add_node(n):
        for node in self.nodes:
            if node.label == n.label:
                return
        self.node.append(node)

    def find_node(label):
        for node in self.nodes:
            if node.label == label:
                return node


    def add_edge(label1, label2):
        node1 = find_node(label1)
        node2 = find_node(label2)





class Node:
    def __init__(label, linked_to, linked_by):
        self.label = label
        self.mark = 0
        self.linked_to = linked_to
        self.linked_by = linked_by
