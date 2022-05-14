"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

import pandas as pd
import networkx as nx
import networkx.algorithms.community as nxc

from .graph_utils import GraphUtils
from .graph_viz import GraphViz
from .graph_embedding import NodeEmbedding, EdgeEmbedding

class Graph:
    """Generic graph implementation wrapping a concrete graph framework.

    The goal of this implementation is to be able to enhance the frameworks capabilities with additional features
    (mostly provided by a delegate pattern).

    References:
    - https://networkx.org
    """

    def __init__(self, nodes, edges, directed=False):
        """Create a graph instance."""
        # Properties
        self.nodes = nodes
        self.edges = edges
        self.directed = directed
        self.weighted = True if (len(edges) > 0 and len(edges[0]) > 2) else False
        self.multi = self.detect_multi_graph()
        # Create network x graph instance
        if self.multi:
            self.graph = nx.MultiDiGraph() if self.directed else nx.MultiGraph()
        else:
            self.graph = nx.DiGraph() if self.directed else nx.Graph()
        # add nodes
        self.graph.add_nodes_from(self.nodes)
        # add edges
        if self.weighted:
            self.graph.add_weighted_edges_from(self.edges)
        else:
            self.graph.add_edges_from(self.edges)

    def detect_multi_graph(self):
        # skip additional edge infos (only use nodes for detection)
        plain_edges = []
        for e in self.edges:
            plain_edges.append((e[0],e[1]))
        # check for same tuples and same reversed tubles
        for i in range(len(plain_edges)):
            item = plain_edges[i]
            rev_item = (item[1], item[0])
            others = plain_edges[i+1:]
            if item in others or rev_item in others:
                return True
        return False

    def number_of_nodes(self):
        """Return the number of nodes."""
        return len(self.nodes)

    def properties(self):
        """Assemble the basic graph properties."""
        # assemble common properties
        neighbors = {}
        degrees = {}
        for node in self.graph.nodes:
            neighbors[node] = list(self.graph.neighbors(node))
            degrees[node] = self.graph.degree(node)
        result = {
            "nodes": self.graph.nodes,
            "edges": self.graph.edges,
            "order": self.graph.number_of_nodes(),
            "size": self.graph.number_of_edges(),
            "neighbors": neighbors,
            "degrees": degrees
        }
        # assemble directed properties
        if self.directed:
            in_degrees = {}
            out_degrees = {}
            for node in self.graph.nodes:
                in_degrees[node] = self.graph.in_degree(node)
                out_degrees[node] = self.graph.out_degree(node)
            result['in_degrees'] = in_degrees
            result['out_degrees'] = out_degrees
        # return result
        return result

    def print_properties(self, title=None, indention=2):
        """Print the basic graph properties."""
        props = self.properties()
        space = " " * (indention-1)
        if title is None:
            print("Graph properties:")
        else:
            print(title + ":")
        for k in props:
            print(space, k.ljust(11), ":", props[k] )

    def draw(self, title=None, path=[], filename=None):
        """Draw the graph with the default settings. If an additional path is defined, the edges of the listed path
        entries will be colored.

        Note: If you wish to override some or all of the default settings, please use the GraphViz.draw()
        methode directly."""
        GraphViz.draw(self.graph, title=title, multi=self.multi, weighted=self.weighted, path=path, filename=filename)


    # -----------------------------------------------------------------------------------------------------------------
    # matrix and edge list functions
    # -----------------------------------------------------------------------------------------------------------------

    def pandas_matrix(self, dtype=int):
        """Returns the graph adjacency matrix as a Pandas dataframe."""
        return nx.to_pandas_adjacency(self.graph, dtype=dtype)

    def numpy_matrix(self):
        """Returns the graph adjacency matrix as a NumPy matrix."""
        return nx.to_numpy_matrix(self.graph)

    def print_matrix(self, label=True):
        """Print the adjacency matrix with or without labels."""
        if label:
            print(self.pandas_matrix())
        else:
            print(self.numpy_matrix())

    def pandas_edgelist(self, source="Source", target="Target"):
        """Returns the graph edgelist as a Pandas dataframe."""
        df = nx.to_pandas_edgelist(self.graph, source=source, target=target)
        # override default lowercase weight to Weight
        if len(df.columns) == 3 and df.columns[2] == "weight":
            df.rename (columns={'weight':'Weight'}, inplace=True)
        # return result
        return df

    def print_edgelist(self):
        """Print the edgelist. If the list is directed, the nodes are labeled as source and target, otherwise the
        first node is labeld as edge."""
        if self.directed:
            print(self.pandas_edgelist())
        else:
            print(self.pandas_edgelist(source="Edge", target=""))

    # -----------------------------------------------------------------------------------------------------------------
    # metrics
    # -----------------------------------------------------------------------------------------------------------------

    def shortest_path(self, source, target):
        """Return list of nodes of the shortest path."""
        return nx.shortest_path(self.graph, source=source, target=target)

    def shortest_path_average(self):
        """Return average """
        return nx.average_shortest_path_length(self.graph)

    def node_combinations(self):
        """Return all node combinations as list of tuples.
        Each tuple contains the source and target node name. Sample tuple: ('Genf', 'Lausanne')
        """
        return GraphUtils.combinations(self.nodes)

    def shortest_path_combinations(self, pandas_df=True):
        """Return all shortest path combinations as list of tuples or pandas data frame (default).

        Each tuple contains the source and target node name, the list of the nodes of the shortest path and the number
        of edges to pass. Sample tuple: ('Genf', 'Lausanne', ['Genf', 'Lausanne'], 1)
        """
        data = []
        for source, target in self.node_combinations():
            shortest_path = self.shortest_path(source, target)
            number_of_edges = len(shortest_path) - 1
            data.append((source, target, shortest_path, number_of_edges))
        if pandas_df:
            return pd.DataFrame(data, columns=["Source", "Target", "Shortest path", "Number of edges"])
        return data

    def efficiency(self, local=False):
        """Return the global (default) or local efficiency of the graph."""
        if local:
            return nx.local_efficiency(self.graph)
        return nx.global_efficiency(self.graph)

    def clustering(self, average=False, pandas_df=True):
        """Return the clustering coefficient for each node (default) or the average of all nodes.
        The clustering coefficient for each node can either be returned as pandas dataframe (default) or dictionary.
        """
        if average:
            return nx.average_clustering(self.graph)
        if pandas_df:
            data = [(k,v) for k, v in nx.clustering(self.graph).items() ]
            return pd.DataFrame(data, columns=["Clustering", "Coefficient"])
        return nx.clustering(self.graph)

    def transitivity(self):
        """Return the transitivity of the graph."""
        return nx.transitivity(self.graph)

    def modularity(self, communities):
        """Return the modularity of the graph. The value is calculated with the modularity function of the networkx
        algorithm module."""
        return nxc.modularity(self.graph, communities=communities)

    def centrality(self, pandas_df=True):
        data = GraphUtils.zip_dicts(
            self.centrality_degree(),
            self.centrality_closeness(),
            self.centrality_betweenness()
        )
        if pandas_df:
            return pd.DataFrame(data, columns=["Centrality", "Degreee", "Closeness", "Betweenness"])
        return data

    def centrality_degree(self):
        return nx.degree_centrality(self.graph)

    def centrality_closeness(self):
        return nx.closeness_centrality(self.graph)

    def centrality_betweenness(self):
        return nx.betweenness_centrality(self.graph)

    def assortativity(self, pearson=False):
        if pearson:
            return nx.degree_pearson_correlation_coefficient(self.graph)
        return nx.degree_assortativity_coefficient(self.graph)

    # -----------------------------------------------------------------------------------------------------------------
    # embeddings
    # -----------------------------------------------------------------------------------------------------------------

    def create_node_embedding(self):
        return NodeEmbedding(self.graph)

    def create_edge_embedding(self):
        return EdgeEmbedding(self.graph)

    # -----------------------------------------------------------------------------------------------------------------
    # link predictions
    # -----------------------------------------------------------------------------------------------------------------

    def missing_edges(self):
        """Return a list of all missing edges in the graph."""
        result = []
        for edge in GraphUtils.combinations(self.nodes):
            inverse_edge = (edge[1], edge[0])
            if not edge in self.edges and not inverse_edge in self.edges:
                result.append(edge)
        return result




