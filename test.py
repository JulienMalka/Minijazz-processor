from graphs import Graph, Node

graph = Graph()
nodes_labels = ["1", "21", "22", "333"]
nodes = []
for label in nodes_labels:
    nodes.append(Node(label))

for node in nodes:
    graph.add_node(node)

graph.add_edge("1", "21")
graph.add_edge("1", "22")
graph.add_edge("21", "333")
graph.add_edge("22", "333")

ordered = graph.topological_sort()
for node in ordered:
    print(node.label)


graph = Graph()
nodes_labels = ["1", "2", "3"]
nodes = []
for label in nodes_labels:
    nodes.append(Node(label))

for node in nodes:
    graph.add_node(node)
graph.add_edge("1", "2")
graph.add_edge("2", "3")
graph.add_edge("3", "1")
ordered = graph.topological_sort()
print(ordered)
