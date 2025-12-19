from collections import deque


class Graph:
    def __init__(self):
        # The core storage using an Adjacency List (Dictionary)
        self.adj_list = {}

    # --- Structural Methods ---

    def add_vertex(self, vertex):
        """Adds a new vertex to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2, directed=False):
        """Creates a connection between two vertices."""
        # Ensure both vertices exist before connecting
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            if not directed:
                self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        """Removes the connection between two vertices."""
        if v1 in self.adj_list and v2 in self.adj_list:
            if v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)

    def remove_vertex(self, vertex):
        """Removes a vertex and all associated edges."""
        if vertex in self.adj_list:
            # Remove this vertex from all other adjacency lists
            for other_vertex in self.adj_list:
                if vertex in self.adj_list[other_vertex]:
                    self.adj_list[other_vertex].remove(vertex)
            # Delete the vertex entry itself
            del self.adj_list[vertex]

    # --- Traversal Methods ---

    def bfs(self, start_node):
        """Breadth-First Search: Explores layer by layer."""
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start_node, visited=None):
        """Depth-First Search: Explores as deep as possible."""
        if visited is None:
            visited = set()

        visited.add(start_node)
        traversal = [start_node]

        for neighbor in self.adj_list[start_node]:
            if neighbor not in visited:
                traversal.extend(self.dfs(neighbor, visited))
        return traversal

    def display(self):
        """Displays the adjacency list representation of the graph."""
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")


# --- Example Usage ---
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

print("Graph Structure:")
graph.display()

print("\n\nBFS from different starting nodes:")
print("BFS from A:", graph.bfs("A"))
print("BFS from B:", graph.bfs("B"))
print("BFS from C:", graph.bfs("C"))
print("BFS from D:", graph.bfs("D"))

print("\n\nDFS from different starting nodes:")
print("DFS from A:", graph.dfs("A"))
print("DFS from B:", graph.dfs("B"))
print("DFS from C:", graph.dfs("C"))
print("DFS from D:", graph.dfs("D"))