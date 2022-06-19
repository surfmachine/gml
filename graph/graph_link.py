"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

import networkx as nx
from .graph_utils import GraphUtils

# ---------------------------------------------------------------------------------------------------------------------
# Class Algorithm
# ---------------------------------------------------------------------------------------------------------------------

class Algorithm():
    """Define the follwoing lgorithms with short name (key), name and the function of the implementation."""

    #
    # Index based algorithms
    #
    RESOURCE_ALLOCATION_INDEX = {
        "key" : "RA",
        "name": "Resource Allocation Index",
        "func": nx.resource_allocation_index
    }

    JACCARD_COEFFICIENT = {
        "key" : "JC",
        "name": "Jaccard Coefficient",
        "func": nx.jaccard_coefficient
    }

    ADAMIC_ADAR_INDEX = {
        "key" : "AA",
        "name": "Adamic Adar Index",
        "func": nx.adamic_adar_index
    }

    PREFERENTIAL_ATTACHMENT = {
        "key" : "PA",
        "name": "Preferential Attachment",
        "func": nx.preferential_attachment
    }

    #
    # Community based algorithms
    #

    SOUNDARAJAN_HOPCROFT = {
        "key" : "SH",
        "name": "Soundarajan Hopcroft",
        "func": nx.cn_soundarajan_hopcroft
    }

    SOUNDARAJAN_HOPCROFT_INDEX = {
        "key" : "SI",
        "name": "Index Soundarajan Hopcroft",
        "func": nx.ra_index_soundarajan_hopcroft
    }

    WITHIN_INTER_CLUSTER = {
        "key" : "IC",
        "name": "Within Inter Cluster",
        "func": nx.within_inter_cluster
    }

    COMMON_NEIGHBOR_CENTRALITY = {
        "key" : "CN",
        "name": "Common Neighbor Centrality",
        "func": nx.common_neighbor_centrality
    }


# ---------------------------------------------------------------------------------------------------------------------
# class GraphLink
# ---------------------------------------------------------------------------------------------------------------------

class GraphLink():
    """Wrapper of some index based link predictions of the networkx framework.

    References:
    - https://networkx.org
    """
    def __init__(self, graph, possible_edges):
        self.graph = graph
        self.possible_edges = possible_edges
        self.algorithms = []
        self.predictions = []

    def predict(self, *algorithms):
        for a in algorithms:
            prediction = list(a["func"](self.graph.graph, self.possible_edges))
            self.algorithms.append(a)
            self.predictions.append(prediction)
        return self

    def print_results(self, incl_legend=True):
        print("Results:")
        print(self.to_pandas())
        if incl_legend:
            print("")
            self.print_legend()

    def print_legend(self):
        """Print the legend of the current predictions."""
        print("Legend:")
        for a in self.algorithms:
            print(" ", a['key'], " =", a['name'])

    def to_list(self):
        """Return predictions as list."""
        return self.predictions

    def to_pandas(self, use_key_as_label=True):
        """Return predictions as pandas data frame."""
        labels = []
        field = "key" if use_key_as_label else "name"
        for a in self.algorithms:
            labels.append( a[field] )
        return GraphUtils.assemble_link_predictions(labels, self.predictions)

