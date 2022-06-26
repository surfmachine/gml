"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

from .graph import Graph
from .graph_utils import GraphUtils

class GraphBuilder:
    """Class to build up a graph with nodes and edges.

    The append methods return the builder instance itself; this way all append methods can be concatenated together.
    At the end of the build steps, the a generic graph instance can be created.

    References:
    - https://networkx.org
    """
    def __init__(self):
        """Create new graph builder instance."""
        self.nodes = []
        self.edges = []
        self.communities = []

    def append_node(self, node):
        """Append a single node, if not already present. Returns the builder instance."""
        if node not in self.nodes:
            self.nodes.append(node)
        return self

    def append_nodes(self, nodes, fully_connected=False):
        """Append nodes, if not already present. Returns the builder instance."""
        for node in nodes:
            self.append_node(node)
        if fully_connected:
            edges = GraphUtils.combinations(self.nodes)
            self.append_edges(edges)
        return self

    def append_edge(self, edge):
        """Append edge (tuple with two nodes). The nodes will automatically be added to the list of nodes if not already
        present. Returns the builder instance."""
        self.append_node(edge[0])
        self.append_node(edge[1])
        self.edges.append(edge)
        return self

    def append_edges(self, edges):
        """Append list of edges. The edge's nodes will automatically be added to the list of nodes if not already
        present. Returns the builder instance."""
        for edge in edges:
            if type(edge) is tuple:
                self.append_node(edge[0])
                self.append_node(edge[1])
                self.append_edge(edge)
            else:
                self.append_node(edge)
        return self

    def append_edges_file(self, file, sep=","):
        edges = []
        with open(file, "r") as f:
            line = f.readline()
            while (line):
                source, target = line.split(sep=sep)
                edges.append((source.strip(), target.strip()))
                line = f.readline()
        self.append_edges(edges)
        return self

    def append_community(self, community, nodes):
        """Append the given community to the graph for the list of nodes."""
        self.communities.append((community, nodes))
        return self

    def append_communities(self, communities):
        """Append a list of communities to the graph. The list of communities contails tuples. Each tuple has the
         community as first element and the list of nodes as second.
         """
        for t in communities:
            self.append_community(t[0],t[1])
        return self

    def create(self, detect_multi_graph=True):
        """Create a graph instance with the given nodes and edges and return the result."""
        return Graph(self.nodes, self.edges, communities=self.communities, detect_multi_graph=detect_multi_graph)

    def create_directed(self, detect_multi_graph=True):
        """Create a directed graph instance with the given nodes and edges and return the result."""
        return Graph(self.nodes, self.edges, directed=True, communities=self.communities, detect_multi_graph=detect_multi_graph)

