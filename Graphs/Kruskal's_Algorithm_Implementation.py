""" Created by @debjitpal5040

    Kruskal's Minimum Spanning Tree Algorithm
    This program is for set of edges representation of the graph

    It is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
    This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.
    The algorithm operates by in each step it adds the next lowest-weight edge that will not form a cycle to the minimum spanning tree.

    The algorithm may informally be described as performing the following steps:

    Create a forest F (a set of trees), where each vertex in the graph is a separate tree
    Create a set S containing all the edges in the graph
    While S is nonempty and F is not yet spanning
        Remove an edge with minimum weight from S
        If the removed edge connects two different trees then add it to the forest F, combining two trees into a single tree

"""
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def kruskalMST(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print(u,"--",v,"\t",weight)
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
print("Edge \tWeight")
g.kruskalMST()
"""
Output

Edge    Weight
2 -- 3   4
0 -- 3   5
0 -- 1   10

"""