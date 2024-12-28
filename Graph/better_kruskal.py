from better_graph import Graph, Vertex

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def kruskal(graph):
    # Create a list of all edges in the graph
    edges = []
    for v in graph.vertices.values():
        for neighbor, weight in v.neighbors.items():
            edges.append((v.id, neighbor.id, weight))
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Create disjoint set
    vertices = list(graph.vertices.keys())
    disjoint_set = DisjointSet(vertices)

    # Initialize MST
    mst = Graph()

    for edge in edges:
        v1, v2, weight = edge
        if disjoint_set.find(v1) != disjoint_set.find(v2):
            disjoint_set.union(v1, v2)
            mst.add_edge(v1, v2, weight)

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

    mst = kruskal(g)

    # Print the edges in the MST
    for vertex in mst.vertices.values():
        for neighbor, weight in vertex.neighbors.items():
            print(f"{vertex.id} - {neighbor.id}: {weight}")