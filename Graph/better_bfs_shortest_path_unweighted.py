from collections import deque
from better_graph import Graph, Vertex

class UnweightedGraph(Graph):
    def shortest_path_bfs(self, start_node, end_node):
        """
        Find shortest path between start_node and end_node using BFS.
        Returns tuple of (distance, path).
        If no path exists, returns (infinity, []).
        """
        if start_node not in self.vertices or end_node not in self.vertices:
            return float('inf'), []
            
        # Reset all vertices
        for vertex in self.vertices.values():
            vertex.distance = float('inf')
            vertex.previous_vertex = None
            vertex.visited = False
            
        # Initialize start vertex
        start_vertex = self.vertices[start_node]
        start_vertex.distance = 0
        start_vertex.visited = True
        
        # BFS using queue
        queue = deque([start_vertex])
        
        while queue:
            current_vertex = queue.popleft()
            
            # If we reached the end node, we're done
            if current_vertex.id == end_node:
                break
                
            # Process all neighbors
            for neighbor in current_vertex.neighbors:
                if not neighbor.visited:
                    neighbor.visited = True
                    neighbor.distance = current_vertex.distance + 1
                    neighbor.previous_vertex = current_vertex
                    queue.append(neighbor)
        
        # If end_vertex wasn't reached, return infinity and empty path
        end_vertex = self.vertices[end_node]
        if end_vertex.distance == float('inf'):
            return float('inf'), []
            
        # Reconstruct path
        path = []
        current = end_vertex
        while current is not None:
            path.append(current.id)
            current = current.previous_vertex
            
        return end_vertex.distance, path[::-1]  # Reverse path to get start→end order

def test_shortest_path():
    # Create graph
    g = UnweightedGraph()
    
    # Test case 1: Simple path
    edges1 = [
        ('A', 'B', 1),
        ('B', 'C', 1),
        ('A', 'C', 1),
        ('C', 'D', 1)
    ]
    
    for from_node, to_node, weight in edges1:
        g.add_edge(from_node, to_node, weight)
        g.add_edge(to_node, from_node, weight)  # Make it undirected
        
    distance, path = g.shortest_path_bfs('A', 'D')
    print(f"Test 1 - Path from A to D:")
    print(f"Distance: {distance}")
    print(f"Path: {' → '.join(path)}")
    
    # Test case 2: No path exists
    g = UnweightedGraph()
    edges2 = [
        ('A', 'B', 1),
        ('C', 'D', 1)
    ]
    
    for from_node, to_node, weight in edges2:
        g.add_edge(from_node, to_node, weight)
        g.add_edge(to_node, from_node, weight)
        
    distance, path = g.shortest_path_bfs('A', 'D')
    print(f"\nTest 2 - No path exists from A to D:")
    print(f"Distance: {distance}")
    print(f"Path: {path}")
    
    # Test case 3: Cycle in graph
    g = UnweightedGraph()
    edges3 = [
        ('A', 'B', 1),
        ('B', 'C', 1),
        ('C', 'A', 1),
        ('C', 'D', 1)
    ]
    
    for from_node, to_node, weight in edges3:
        g.add_edge(from_node, to_node, weight)
        g.add_edge(to_node, from_node, weight)
        
    distance, path = g.shortest_path_bfs('A', 'D')
    print(f"\nTest 3 - Path from A to D with cycle in graph:")
    print(f"Distance: {distance}")
    print(f"Path: {' → '.join(path)}")

if __name__ == "__main__":
    test_shortest_path()