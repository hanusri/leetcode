from typing import List

class Vertex:
    def __init__(self, node):
        self.id = node
        self.neighbors = set()
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, node):
        if node not in self.vertices:
            self.vertices[node] = Vertex(node)

    def add_edge(self, from_node, to_node):
        if from_node not in self.vertices:
            self.add_vertex(from_node)
        if to_node not in self.vertices:
            self.add_vertex(to_node)
        self.vertices[from_node].add_neighbor(to_node)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = Graph()
        
        # Build the graph
        for i, keys in enumerate(rooms):
            graph.add_vertex(i)
            for key in keys:
                graph.add_edge(i, key)
        
        # Perform DFS
        def dfs(node):
            vertex = graph.vertices[node]
            vertex.visited = True
            for neighbor in vertex.neighbors:
                if not graph.vertices[neighbor].visited:
                    dfs(neighbor)
        
        # Start DFS from room 0
        dfs(0)
        
        # Check if all rooms are visited
        return all(vertex.visited for vertex in graph.vertices.values())