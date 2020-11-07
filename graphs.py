class Graph:
    def __init__(self):
        self.nodes = []


    def add_node(self, n):
        for node in self.nodes:
            if node.label == n.label:
                return
        self.nodes.append(n)

    def find_node(self, label):
        for node in self.nodes:
            if node.label == label:
                return node


    def add_edge(self, label1, label2):
        node1 = self.find_node(label1)
        node2 = self.find_node(label2)
        node1.link_to.append(node2)
        node2.linked_by.append(node1)

    def find_roots(self):
        roots = []
        for node in self.nodes:
            if node.linked_by == []:
                roots.append(node)
        return roots



    def topological_sort(self):
        start = self.find_roots()
        sorted = []
        while len(start)>0:
            node = start[0]
            start.remove(node)
            sorted.append(node)
            for linked_node in node.link_to:
                linked_node.linked_by.remove(node)
                if linked_node.linked_by == []:
                    start.append(linked_node)
            node.link_to = []


        if len(sorted) == len(self.nodes):
            return sorted
        else:
            return "ERREUR"



class Node:
    def __init__(self, label):
        self.label = label
        self.link_to = []
        self.linked_by = []

