"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

import networkx as nx
from .graph_utils import GraphUtils
from .graph_metrics import GraphMetrics

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
        self.normalized = False
        self.labeled = False

    def predict(self, *algorithms):
        for a in algorithms:
            prediction = list(a["func"](self.graph.graph, self.possible_edges))
            self.algorithms.append(a)
            self.predictions.append(prediction)
        return self

    def normalize(self):
        """Normalizes the prediction results for each algorithm.

        Processing rules:
            - Each prediction is a list of the predictions from the corresponding algorithm
            - Each prediction entry is a triple with: from node, to node and prediction value
            - For the normalization process the following steps will be done for each algorithm:
                1. get maximum of the prediction entries
                2. Normalize each entry with the given maximum and create a new triple
                3. Replace the existing triple with the new one.

        Note:
            The normalization will be executed in place, therfor the original ranges will be gone.
        """
        # check precondition
        if self.normalized:
            return self
        # normalize
        for i, prediction in enumerate(self.predictions):
            vmax = 0
            for _, _, v in prediction:
                if v > vmax:
                    vmax = v
            for j, t in enumerate(prediction):
                if vmax == 0:
                    tnew = t
                else:
                    tnew = (t[0], t[1], t[2]/vmax)
                self.predictions[i][j] = tnew
        # return result
        self.normalized = True
        return self

    def filter_deprecated(self, edges):
        """Filter results for the given edges."""
        for i, prediction in enumerate(self.predictions):
            new_prediction = []
            for j, t in enumerate(prediction):
                edge = (t[0],t[1])
                reverse_edge = (t[1],t[0])
                if edge in edges:
                    new_prediction.append(t)
                elif reverse_edge in edges:
                    t_new = (t[1], t[0], t[2])
                    new_prediction.append(t_new)
            self.predictions[i] = new_prediction
        return self

    def filter(self, edges):
        """Filter results for the given edges."""
        for i, prediction in enumerate(self.predictions):
            new_prediction = []
            for edge in edges:
                for t in prediction:
                    e = (t[0],t[1])
                    re= (t[1],t[0])
                    if edge == e or edge == re:
                        new_prediction.append((edge[0], edge[1], t[2]))
            self.predictions[i] = new_prediction
        return self

    def label(self, threshold=0.8):
        """Labels the normalized predictions to 0 or 1 according the given threshold."""
        # check precondition
        if self.labeled:
            return self
        if not self.normalized:
            self.normalize()
        # label
        for i, prediction in enumerate(self.predictions):
            for j, t in enumerate(prediction):
                vnew = 1 if t[2] > threshold else 0
                tnew = (t[0], t[1], vnew)
                self.predictions[i][j] = tnew
        # return result
        self.labeled = True
        return self


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

    def to_y_preds_list(self):
        result = []
        for preds in self.predictions:
            l = []
            for p in preds:
                l.append(p[2])
            result.append(l)
        return result

    def to_metrics_list(self, y_true):
        y_preds = self.to_y_preds_list()
        metrics = GraphMetrics().metrics_list(y_true, y_preds)
        return metrics

    def to_metrics_pandas(self, y_true, use_key_as_label=True):
        """Return predictions as pandas data frame."""
        # init labels
        labels = []
        field = "key" if use_key_as_label else "name"
        for a in self.algorithms:
            labels.append( a[field] )
        return GraphMetrics().metrics_pandas(y_true, self.to_y_preds_list(), labels)

    def print_metrics(self, y_true, incl_legend=True, title="Metrics", use_key_as_label=True):
        self.label()
        print(title)
        print((self.to_metrics_pandas(y_true, use_key_as_label=use_key_as_label)).to_string())
        if incl_legend:
            print("")
            self.print_legend()

    def print_results(self, incl_legend=True, normalize=False, label=False, title="Results"):
        if normalize:
            self.normalize()
        if label:
            self.label()
        print(title)
        print((self.to_pandas()).to_string())
        if incl_legend:
            print("")
            self.print_legend()


    def print_legend(self):
        """Print the legend of the current predictions."""
        print("Legend:")
        for a in self.algorithms:
            print(" ", a['key'], " =", a['name'])

