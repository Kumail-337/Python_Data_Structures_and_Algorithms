class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.graph_dict = {}

    def add_vertex(self, vertex):
        # Add a new node to the graph
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, v1, v2):
        # Create a connection between two nodes
        # For an undirected graph, add each to the other's list
        if v1 in self.graph_dict and v2 in self.graph_dict:
            self.graph_dict[v1].append(v2)
            self.graph_dict[v2].append(v1)

    def display(self):
        for vertex in self.graph_dict:
            print(f"{vertex}: {self.graph_dict[vertex]}")

# Usage:
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_edge("A", "B")
my_graph.display()