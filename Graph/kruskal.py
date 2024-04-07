class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 1 for v in vertices}  # rank is the size of the tree

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.rank[root_u] += self.rank[root_v]
            else:
                self.parent[root_u] = root_v
                self.rank[root_v] += self.rank[root_u]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def addEdge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))

    def edges(self):
        edge_list = []
        for vertex in self.vertices:
            for edge in self.adjacency_list[vertex]:
                edge_list.append((vertex, *edge))
        return edge_list

    def kruskal(self):
        disjoint_set = DisjointSet(self.vertices)
        mst = []
        for u, v, w in sorted(self.edges(), key=lambda x: x[2]):
            if disjoint_set.find(u) != disjoint_set.find(v):
                disjoint_set.union(u, v)
                mst.append((u, v, w))
        return mst