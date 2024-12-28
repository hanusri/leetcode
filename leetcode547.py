class Vertex:
    def __init__(self, node):
        self.id = node
        self.neighbors = []
        self.is_safe = None  # None: unknown, True: safe, False: unsafe

class Graph:
    def __init__(self, n):
        self.vertices = {i: Vertex(i) for i in range(n)}

    def add_edge(self, from_node, to_node):
        self.vertices[from_node].neighbors.append(self.vertices[to_node])

def is_safe_node(graph, node, visited, in_stack):
    # If we've already determined if this node is safe, return that result
    if node.is_safe is not None:
        return node.is_safe
    
    # If this node is currently being evaluated (in the stack), it's not safe
    if node in in_stack:
        node.is_safe = False
        return False
    
    visited.add(node)
    in_stack.add(node)
    
    # Check all neighbors
    for neighbor in node.neighbors:
        if not is_safe_node(graph, neighbor, visited, in_stack):
            node.is_safe = False
            in_stack.remove(node)
            return False
    
    node.is_safe = True
    in_stack.remove(node)
    return True

def find_safe_nodes(graph):
    n = len(graph.vertices)
    visited = set()
    in_stack = set()
    
    for i in range(n):
        is_safe_node(graph, graph.vertices[i], visited, in_stack)
    
    return sorted([i for i in range(n) if graph.vertices[i].is_safe])

class Solution:
    def eventualSafeNodes(self, graph_array: List[List[int]]) -> List[int]:
        n = len(graph_array)
        graph = Graph(n)
        
        for i, neighbors in enumerate(graph_array):
            for neighbor in neighbors:
                graph.add_edge(i, neighbor)
        
        return find_safe_nodes(graph)