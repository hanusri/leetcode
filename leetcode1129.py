from typing import List
from Graph.better_graph import Graph
from queue import Queue

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = Graph(n)
        
        for from_node, to_node in redEdges:
            graph.add_edge(from_node, to_node, 'red')
        
        for from_node, to_node in blueEdges:
            graph.add_edge(from_node, to_node, 'blue')
        
        queue = Queue()
        queue.put((0, 'red', 0))
        queue.put((0, 'blue', 0))
        
        result = [-1] * n
        result[0] = 0
        
        while not queue.empty():
            node, color, distance = queue.get()
            neighbors = graph.vertices[node].neighbors[color]
            next_color = 'red' if color == 'blue' else 'blue'
            
            for neighbor in neighbors:
                if result[neighbor] == -1:
                    result[neighbor] = distance + 1
                    queue.put((neighbor, next_color, distance + 1))
        
        return result
        