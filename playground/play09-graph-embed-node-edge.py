from node2vec import Node2Vec
from node2vec.edges import HadamardEmbedder
import matplotlib.pyplot as plt
from gml.graph.graph_builder import GraphBuilder

print("#")
print("# Graph")
print("#")

edges = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4),(4,5),(5,6),(6,7),(6,8),(7,8),(8,9),(9,10),(10,11),(10,12), (11,12)]
graph = GraphBuilder().append_edges(edges).create()
graph.draw()


print("#")
print("# Node Embeddings")
print("#")

class NodeEmbeddings():

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


ne = NodeEmbeddings(graph.graph).draw()


print("#")
print("# Edge Embeddings")
print("#")

class EdgeEmbeddings():

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


ee = EdgeEmbeddings(graph.graph).draw()


