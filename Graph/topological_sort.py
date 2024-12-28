from better_graph import Graph
from queue import Queue
def topological_sort(graph):
    queue = Queue()
    counter = 0

    for vertex in graph.vertices.values():
        if vertex.indegree == 0:
            queue.put(vertex)
    
    while not queue.empty():
        v = queue.get()
        counter += 1
        v.topNum = counter

        for neighbor in v.neighbors:
            neighbor.indegree -= 1
            if neighbor.indegree == 0:
                queue.put(neighbor)
    
    if counter != len(graph.vertices):
        raise RuntimeError("Graph contains a cycle")