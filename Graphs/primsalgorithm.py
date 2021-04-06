import sys


class Tree:
    def __init__(self):
        self._parent = None
        # Key = node.name , Value = Node obj
        self._nodes = dict()

    def add_node(self, parent, vertex):
        node = Node(vertex.x, vertex.y, vertex.name, parent=None)
        if self._parent is None:
            self._parent = node
        else:
            nodes = self._nodes.keys()
            if parent.name in nodes and vertex.name not in nodes:
                node.parent = self._nodes[parent.name]
                self._nodes[parent.name].children.add(node)
            else:
                return False
        self._nodes[node.name] = node
        return True

    def remove_node(self):
        pass

    def get_connections(self):
        out = []
        nodes = self._nodes.values()
        for node in nodes:
            for child in node.children:
                out.append(
                    (node, child,
                     Graph.WeightedGraph.calculate_distance(node, child)))
        return out

    def print_tree(self):
        nodes = self._nodes.values()
        for node in nodes:
            print(node)
            for child in node.children:
                out = " --- " + str(child)
                print(out)


class Node:
    def __init__(self, x, y, name, parent):
        # Cartesian x coordinate
        self.x = x
        # Cartesian y coordinate
        self.y = y
        # Node name. For Prim's should match graph node name
        self.name = name
        # parent Node object
        self.parent = parent
        # list of all child nodes
        self.children = set()

    def __str__(self):
        """
        Simple to-string method which prints the object data members
        """
        ret = "Node: " + str(self.name) + " x=" + str(self.x) + " y=" + str(
            self.y)
        return ret


def run_prims(graph, vertex):
    # reset all the traversed flags
    for vertex in graph._vertices:
        vertex.traversed = False
    # setup result tree and add parent node
    t = Tree()
    t.add_node(None, vertex)
    vertex.traversed = True
    connected_edges = graph.get_outgoing_edges(vertex)
    # Greedily go find the next smallest edge until there is no edges left
    while len(connected_edges) > 0:
        # print("-----------")
        # for item in connected_edges:
        #    print(item)
        #    print(item.connectedVertex.traversed)
        smallest_dist = float("inf")
        smallest_edge = None
        # Find the next smallest un-traversed vertex
        for edge in connected_edges:
            if (edge.connectedVertex.traversed is False
                    and edge.distance < smallest_dist):
                smallest_dist = edge.distance
                smallest_edge = edge
        connected_edges.remove(smallest_edge)
        smallest_edge.connectedVertex.traversed = True
        # Update the connected edges set to include edges from the newly added vertex
        connected_edges = connected_edges | graph.get_outgoing_edges(
            smallest_edge.connectedVertex)  # set union
        t.add_node(smallest_edge.sourceVertex, smallest_edge.connectedVertex)
        # Remove other edges that end at the next smallest vertex.
        remove_set = set()
        for edge in connected_edges:
            if edge.connectedVertex.traversed is True:
                remove_set.add(edge)
        connected_edges = connected_edges - remove_set  # set difference
    return t
