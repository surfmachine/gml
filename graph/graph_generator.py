"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

import random
import networkx as nx
from gml.graph.graph_builder import GraphBuilder

class GraphGenerator:
    """Class to generate random networkx graphs and convert them to the generic graph class.

    References:
    - https://networkx.org
    - https://networkx.org/documentation/stable/reference/generators.html#module-networkx.generators.classic
    """
    def __init__(self):
        """Create new graph generator instance."""
        self.nx_graphs = []

    def append(self, nx_graph):
        self.nx_graphs.append(nx_graph)
        return self

    def append_watts_stragatz(self, n, k, p, seed=None):
        """Generate a Watts-Strogatz small-world graph.

        Args:
            n: The number of nodes.
            k: Each node is joined with its k nearest neighbors in a ring topology.
            p: The probability of adding a new edge for each edge.
            seed: Indicator of random number generation state.
        """
        nx_graph = nx.watts_strogatz_graph(n,k,p, seed=seed)
        return self.nx_graphs.append(nx_graph)

    def append_random_watts_stragatz(self, n_graphs, n_range=(6,24), k_start=3, p_range=(0,1)):
        """Generate and append random Watts-Strogatz small-world graphs."""
        for _ in range(n_graphs):
            n,k,p = GraphGenerator.generate_random_watts_stragatz_params(n_range, k_start, p_range)
            self.append_watts_stragatz(n, k, p, seed=6)
        return self

    def create(self):
        """Create a list of generic graph instances and return the result."""
        graphs = []
        for nxg in self.nx_graphs:
            g = GraphBuilder().append_nodes(nxg.nodes).append_edges(nxg.edges).create()
            graphs.append(g)
        return graphs

    @staticmethod
    def generate_random_watts_stragatz_params(n_range=(6,24), k_start=3, p_range=(0,1)):
        """Generate random parameters for the Watts-Strogatz small-world graph."""
        n = random.randint(n_range[0], n_range[1])
        k = random.randint(k_start, n)
        p = random.uniform(p_range[0], p_range[1])
        return n,k,p

