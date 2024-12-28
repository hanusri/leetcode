import heapq

class Vertex:
    def __init__(self, node):
        self.id = node
        self.distance = float('inf')
        self.previous_vertex = None
        self.neighbors = {}
        self.indegree = 0
        self.topNum = float('inf')
        self.visited = False

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight
        neighbor.indegree += 1

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