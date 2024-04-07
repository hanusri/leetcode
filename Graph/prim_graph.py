from Graph.dijkstra_and_bfs import Graph
class Heap:
    def __init__(self):
        self.heap = []
        self.indexes = {}

    def insert(self, v, priority):
        self.heap.append((v, priority))
        self.indexes[v] = len(self.heap) - 1
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        min_vertex, min_priority = self.heap[0]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.indexes.pop(min_vertex)
        self._bubble_down(0)
        return min_vertex, min_priority

    def decrease_key(self, v, new_priority):
        i = self.indexes[v]
        self.heap[i] = (v, new_priority)
        self._bubble_up(i)

    def _bubble_up(self, i):
        while i > 0 and self.heap[i][1] < self.heap[(i - 1) // 2][1]:
            self._swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def _bubble_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left][1] < self.heap[smallest][1]:
            smallest = left
        if right < len(self.heap) and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right
        if smallest != i:
            self._swap(smallest, i)
            self._bubble_down(smallest)

    def _swap(self, i, j):
        self.indexes[self.heap[i][0]] = j
        self.indexes[self.heap[j][0]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def prim(graph: Graph, start):
    mst = set()
    visited = set([start])
    heap = Heap()
    for to, cost in graph.edges(start):
        heap.insert(to, cost)

    while heap.heap:
        to, cost = heap.extract_min()
        if to not in visited:
            visited.add(to)
            mst.add((start, to, cost))
            start = to
            for to_next, cost2 in graph.edges(to):
                if to_next not in visited:
                    if to_next in heap.indexes and cost2 < heap.heap[heap.indexes[to_next]][1]:
                        heap.decrease_key(to_next, cost2)
                    else:
                        heap.insert(to_next, cost2)

    return mst

# example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(prim(graph, 'A'))  # output: {('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 1)}