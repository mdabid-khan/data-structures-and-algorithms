# ==============================
# Approach 1: Adjacency List (Dictionary)
# ==============================

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"]
}

print("Adjacency List (Dictionary):")
for node, neighbors in graph.items():
    print(f"{node} is connected to {neighbors}")


# ==============================
# Approach 2: Using Class
# ==============================

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)

        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)  # undirected graph

    def display(self):
        print("\nAdjacency List (Class):")
        for node in self.adj_list:
            print(f"{node} is connected to {self.adj_list[node]}")


obj = Graph()
obj.add_edge("A", "B")
obj.add_edge("A", "C")
obj.add_edge("B", "D")
obj.add_edge("B", "E")
obj.add_edge("C", "F")

obj.display()


# ==============================
# Approach 3: Adjacency Matrix
# ==============================

nodes = ["A", "B", "C", "D", "E", "F"]

matrix = [
    [1, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
]

print("\nAdjacency Matrix:")
print("  " + " ".join(nodes))

for i, row in enumerate(matrix):
    print(nodes[i], " ".join(map(str, row)))