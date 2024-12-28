class Vertex:
    def __init__(self, node):
        self.id = node
        self.distance = float('infinity')
        self.previous_vertex = None
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def __lt__(self, other):
        return self.distance < other.distance

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, node):
        self.vertices[node] = Vertex(node)

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.vertices:
            self.add_vertex(from_node)
        if to_node not in self.vertices:
            self.add_vertex(to_node)
        self.vertices[from_node].add_neighbor(self.vertices[to_node], weight)

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = Graph()
        
        # Build the graph
        for city_a, city_b in connections:
            graph.add_edge(city_a, city_b, 1)
            graph.add_edge(city_b, city_a, 0)  # Reverse edge with weight 0
        
        def dfs(vertex, parent):
            count = 0
            for neighbor, weight in vertex.neighbors.items():
                if neighbor.id != parent:
                    count += weight  # If weight is 1, it needs to be reversed
                    count += dfs(neighbor, vertex.id)
            return count
        
        return dfs(graph.vertices[0], -1)
        