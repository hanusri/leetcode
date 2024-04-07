from collections import deque
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def addEdge(self, u, v):
        self.adjacency_list[u].append(v)
    
    def edges(self, vertex):
        return self.adjacency_list[vertex]
    
    def bfsTraversal(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        while queue:
            vertex = queue.popleft(0)
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    queue.append(neighbor)
    
    def dfsTraversal(self, start_vertex):
        visited = set()
        self.dfsTraversalUtil(start_vertex, visited)
    
    def dfsTraversalUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.adjacency_list[v]:
            if neighbor not in visited:
                self.dfsTraversalUtil(neighbor, visited)

    def topologicalSortUtil(self, v, visited, stack):
        visited.add(v)
        for neighbor in self.adjacency_list[v]:
            if neighbor not in visited:
                self.topologicalSortUtil(neighbor, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        visited = set()
        stack = []
        for vertex in self.vertices:
            if vertex not in visited:
                self.topologicalSortUtil(vertex, visited, stack)
        return stack

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
graph = Graph(vertices)
graph.addEdge('A', 'C')
graph.addEdge('A', 'B')
graph.addEdge('B', 'D')
graph.addEdge('D', 'F')
graph.addEdge('E', 'F')
graph.addEdge('C', 'E')

sorted_vertices = graph.topologicalSort()
while sorted_vertices:
    print(sorted_vertices.pop(), end=' ')  # E C A B D F