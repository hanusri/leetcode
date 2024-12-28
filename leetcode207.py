from Graph.better_graph import Graph
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = Graph()
        # load vertices
        for course in range(numCourses):
            self.graph.add_vertex(course)
        
        # load edges
        for prereq in prerequisites:
            course, prerequisite = prereq
            self.graph.add_edge(prerequisite, course, 1)
        
        # Keep track of visited nodes and nodes in current path
        visited = set()
        path = set()

        def has_cycle(vertex_id):
            if vertex_id in path:
                return True
            
            path.add(vertex_id)
            vertex = self.graph.vertices[vertex_id]

            for neighbor in vertex.neighbors:
                if not neighbor.visited:
                    if has_cycle(neighbor.id):
                        return True
            
            path.remove(vertex_id)
            vertex.visited = True

            return False
        
        for vertex_id in self.graph.vertices:
            if vertex_id not in visited:
                if has_cycle(vertex_id):
                    return False
        
        return True
