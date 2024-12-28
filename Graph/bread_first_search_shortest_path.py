from better_graph import Graph
from queue import Queue

def shortestPath(graph, source):
    queue = Queue()
    source.distance = 0
    queue.put(source)

    while not queue.empty():
        vertex = queue.get()
        for neighbor in vertex.neighbors:
            if neighbor == float('inf'):
                neighbor.distance = vertex.distance + 1
                neighbor.previous_vertex = vertex
                queue.put(neighbor)
        