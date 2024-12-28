import heapq
from better_graph import Graph

def dijkstra(graph, start):
    start_vertex = graph.vertices[start]
    start_vertex.distance = 0

    pq = [(0, start_vertex)]
    
    while pq:
        _, current_vertex = heapq.heappop(pq)
        if current_vertex.visited:
            continue
        current_vertex.visited = True
        
        for neighbor, weight in current_vertex.neighbors.items():
            if not neighbor.visited:
                distance = current_vertex.distance + weight
                
                if distance < neighbor.distance:
                    neighbor.distance = distance
                    neighbor.previous_vertex = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

def get_shortest_path(end_vertex):
    path = []
    current = end_vertex
    while current:
        path.append(current.id)
        current = current.previous_vertex
    return path[::-1]

# Example usage
graph = Graph()
edges = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', 1), ('B', 'D', 5),
    ('C', 'D', 8), ('C', 'E', 10),
    ('D', 'E', 2), ('D', 'F', 6),
    ('E', 'F', 3)
]

for from_node, to_node, weight in edges:
    graph.add_edge(from_node, to_node, weight)
    graph.add_edge(to_node, from_node, weight)  # For undirected graph

start_node = 'A'
dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}:")
for vertex in graph.vertices.values():
    print(f"{vertex.id}: {vertex.distance}")

end_node = 'F'
shortest_path = get_shortest_path(graph.vertices[end_node])
print(f"\nShortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")