    """Created by @VivanVatsa
    
    BellmanFord Algorithm:
    
    Input: Graph and a source vertex src
    Output: Shortest distance to all vertices from src. If there is a negative weight cycle, then shortest distances are not calculated, negative weight cycle is reported.
    """

class Graph:

    # __init__ function
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    # adding edge for graph
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # adding node to the graph
    def addNode(self, value):
        self.nodes.append(value)

    # output
    def print_solution(self, dist):
        print("dist of vertex from src")
        for key, value in dist.items():
            print(" " + key, " :   ", value)

    # BellmanFord Algorithm

    def bellmanFord(self, src):
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # loop x2 to check for negative cycle
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph has Negative cycle")
                return

        self.print_solution(dist)

# hard-coded test
g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")

g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)

g.bellmanFord("E")


        """
        Output:
        dist of vertex from src
        A  :    6
        B  :    3
        C  :    4
        D  :    2
        E  :    0
        """