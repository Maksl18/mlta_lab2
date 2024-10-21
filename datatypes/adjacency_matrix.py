from datatypes.node import Node
import networkx as nx
from datatypes.node import Node
import matplotlib.pyplot as plt
from queue import Queue

class AdjacencyMatrix:
    def __init__(self, matrix_type: str):
        allowed_types: list[str] = ["directed", "undirected"]
        if not matrix_type in allowed_types:
            raise TypeError("Invalid matrix type")

        self.matrix_type = matrix_type
        self.node_list: list[Node] = []
        self.matrix: list[list[int]] = [[0] * 1 for _ in range(1)]

    def add_node(self, node: Node) -> None:
        if self.node_list:
            self.matrix.append([0] * len(self.matrix[0]))
            for row in self.matrix:
                row.append(0)
        self.node_list.append(node)

    def del_node(self, node_id: int) -> None:
        if node_id >= len(self.node_list) or node_id < 0:
            raise IndexError("Node index is out of bounds")
        self.node_list.pop(node_id)
        self.matrix.pop(node_id)
        for row in self.matrix:
            row.pop(node_id)

    def add_edge(self, src: int, dest: int) -> None:
        self.matrix[src][dest] = 1
        if self.matrix_type == "undirected":
            self.matrix[dest][src] = 1

    def print(self) -> None:
        print(end="\t")
        for node in self.node_list:
            print(node.data, end="\t")
        print(end="\n")

        for i in range(len(self.matrix)):
            print(self.node_list[i].data, end="\t")
            for j in range(len(self.matrix[i])):
                print(f"{self.matrix[i][j]}", sep=" ", end="\t")
            print(end="\n")

    def visualise(self):
        graph = nx.Graph()
        if self.matrix_type == "directed":
            graph = nx.DiGraph()

        nodes = [node.data for node in self.node_list]
        graph.add_nodes_from(nodes)
        mapping = {i: node.data for i, node in enumerate(self.node_list)}
        graph = nx.relabel_nodes(graph, mapping)

        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                if element == 1:
                    graph.add_edge(nodes[i], nodes[j])

        plt.figure(figsize=(6, 5))
        nx.draw(graph, pos=nx.shell_layout(graph), with_labels=True, node_size=700, font_size=10, edge_color='black')
        plt.title("Graph Visualization")
        image = f"./media/graph.png"
        plt.savefig(image)

    def depth_first_search(self, src: int) -> str:
        visited: list[bool] = [False] * len(self.node_list)
        visited_indexes: list[int] = []
        self.dfs_helper(src, visited, visited_indexes)

        # Return traversal as a formatted string: A -> B -> C -> D
        return " -> ".join(self.node_list[i].data for i in visited_indexes)

    def dfs_helper(self, src: int, visited: list[bool], visited_indexes: list[int]) -> None:
        if visited[src]:
            return

        visited[src] = True
        visited_indexes.append(src)

        for i in range(len(self.matrix[src])):
            if self.matrix[src][i]:
                self.dfs_helper(i, visited, visited_indexes)

    def breath_first_search(self, src: int) -> str:
        queue: Queue[int] = Queue()
        visited: list[bool] = [False] * len(self.node_list)
        visited_indexes: list[int] = []

        queue.put(src)
        visited[src] = True

        while queue.qsize() != 0:
            src = queue.get()
            visited_indexes.append(src)

            for i in range(len(self.matrix[src])):
                if self.matrix[src][i] == 1 and not visited[i]:
                    queue.put(i)
                    visited[i] = True
        return " -> ".join(self.node_list[i].data for i in visited_indexes)

