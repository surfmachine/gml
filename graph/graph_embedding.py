"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

from node2vec import Node2Vec
from node2vec.edges import HadamardEmbedder
import matplotlib.pyplot as plt
from karateclub import Graph2Vec


class NodeEmbedding():
    """Node embedding with with node2vec and visualization.

    References:
    - https://networkx.org
    - https://snap.stanford.edu/node2vec/
    """
    def __init__(self, graph, dimensions=2, window=10):
        self.graph = graph
        self.node2vec = Node2Vec(self.graph, dimensions=dimensions)
        self.model = self.node2vec.fit(window=window)

    def draw(self, title="Node embeddings"):
        fig, ax = plt.subplots(figsize=(10,10))
        for x in self.graph.nodes():
            v = self.model.wv.get_vector(str(x))
            ax.scatter(v[0],v[1], s=1000)
            ax.annotate(str(x), (v[0]-0.02,v[1]-0.01), fontsize=12)
        plt.title(title, fontsize=15)
        plt.show()


class EdgeEmbedding():
    """Edge embedding with with node2vec.edges HadamardEmbedder and visualization.

    References:
    - https://networkx.org
    - https://github.com/eliorc/node2vec/blob/master/node2vec/edges.py
    """
    def __init__(self, graph, dimensions=2, window=10):
        self.graph = graph
        self.node2vec = Node2Vec(self.graph, dimensions=dimensions)
        self.model = self.node2vec.fit(window=window)
        self.embeddings = HadamardEmbedder(keyed_vectors=self.model.wv)

    def draw(self, title="Edge embeddings"):
        fig, ax = plt.subplots(figsize=(10,10))
        for x in self.graph.edges():
            v = self.embeddings[(str(x[0]), str(x[1]))]
            ax.scatter(v[0],v[1], s=600)
            ax.annotate(str(x), (v[0]-0.08,v[1]+0.1), fontsize=12)
        plt.title(title, fontsize=15)
        plt.show()


class GraphEmbedding():
    """Graph embedding with karateclub Graph2Vec and visualization.

    References:
    - https://networkx.org
    - https://github.com/benedekrozemberczki/karateclub
    """
    def __init__(self, graphs, dimensions=2, wl_iterations=10):
        self.graphs = graphs
        self.model = Graph2Vec(dimensions=dimensions, wl_iterations=wl_iterations)
        self.model.fit([x.graph for x in graphs])
        self.embeddings = self.model.get_embedding()

    def draw(self, title="Graph embeddings"):
        fig, ax = plt.subplots(figsize=(10,10))
        for i,v in enumerate(self.embeddings):
            ax.scatter(v[0],v[1], s=1000)
            ax.annotate(str(i), (v[0]-0.01,v[1]-0.01), fontsize=12)
        plt.title(title, fontsize=15)
        plt.show()

