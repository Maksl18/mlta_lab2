from datatypes.node import Node
from datatypes.adjacency_matrix import AdjacencyMatrix

def create_undirected_graph():
    graph = AdjacencyMatrix("undirected")
    nodes = ["A", "B", "C", "D", "E", "F", "G"]
#             0    1    2    3    4    5    6

    for node in nodes:
        graph.add_node(Node(node))

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    graph.add_edge(2, 5)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.visualise()

    return graph

def create_directed_graph():
    graph = AdjacencyMatrix("directed")
    nodes = ["A", "B", "C", "D", "F", "G"]
#             0    1    2    3    4    5
    for node in nodes:
        graph.add_node(Node(node))

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 0)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 1)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    graph.visualise()
    return graph
