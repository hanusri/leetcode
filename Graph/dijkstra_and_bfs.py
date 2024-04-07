import heapq
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def addEdge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
    
    def edges(self, vertex):
        return self.adjacency_list[vertex]

    def dijkstra(self, start_vertex):
        shortest_distance_map = {vertex: float('infinity') for vertex in self.vertices}
        shortest_distance_map[start_vertex] = 0

        priority_queue = [(0, start_vertex)]
        while priority_queue:
            (dist, current_vertex) = heapq.heappop(priority_queue)
            for neighbor, neighbor_dist in self.adjacency_list[current_vertex]:
                old_cost = shortest_distance_map[neighbor]
                new_cost = shortest_distance_map[current_vertex] + neighbor_dist
                if new_cost < old_cost:
                    shortest_distance_map[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        return shortest_distance_map  # Dictionary of shortest distance to each vertex

    def shortest_path(self, start):
        visited = {vertex: False for vertex in self.vertices}
        distance = {vertex: float('inf') for vertex in self.vertices}
        predecessor = {vertex: None for vertex in self.vertices}

        queue = deque([start])
        visited[start] = True
        distance[start] = 0

        while queue:
            vertex = queue.popleft()
            for neighbor, _ in self.edges(vertex):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    distance[neighbor] = distance[vertex] + 1
                    predecessor[neighbor] = vertex

        return distance, predecessor