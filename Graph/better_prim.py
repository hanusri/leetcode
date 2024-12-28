import heapq
from better_graph import Graph, Vertex

def prim(graph, start_vertex):
    mst = Graph()
    start = graph.vertices[start_vertex]
    start.distance = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex.id in visited:
            continue

        visited.add(current_vertex.id)

        if current_vertex.previous_vertex:
            mst.add_edge(current_vertex.previous_vertex.id, current_vertex.id, current_distance)

        for neighbor, weight in current_vertex.neighbors.items():
            if neighbor.id not in visited:
                if weight < neighbor.distance:
                    neighbor.distance = weight
                    neighbor.previous_vertex = current_vertex
                    heapq.heappush(pq, (weight, neighbor))

    return mst

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    g.add_edge('D', 'F', 6)
    g.add_edge('E', 'F', 3)

    mst = prim(g, 'A')

    # Print the edges in the MST
    for vertex in mst.vertices.values():
        for neighbor, weight in vertex.neighbors.items():
            print(f"{vertex.id} - {neighbor.id}: {weight}")