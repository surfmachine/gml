import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from stellargraph import StellarGraph, datasets
from stellargraph.data import EdgeSplitter
from node2vec import Node2Vec
from node2vec.edges import HadamardEmbedder

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import metrics


def draw_graph(G, node_names={}, node_size=50):
    pos_nodes = nx.spring_layout(G)
    nx.draw(G, pos_nodes, with_labels=False, node_size=node_size, edge_color='gray', arrowsize=30)

    pos_attrs = {}
    for node, coords in pos_nodes.items():
        pos_attrs[node] = (coords[0], coords[1] + 0.08)

    # print labels
    # nx.draw_networkx_labels(G, pos_attrs, font_family='serif', font_size=20)

    plt.axis('off')
    axis = plt.gca()
    axis.set_xlim([1.2*x for x in axis.get_xlim()])
    axis.set_ylim([1.2*y for y in axis.get_ylim()])
    plt.show()

print("#")
print("# Link Prediction - Embedding Based")
print("#")

edgelist = pd.read_csv("../data/cora/cora.cites", sep='\t', header=None, names=["target", "source"])
G = nx.from_pandas_edgelist(edgelist)


# print(edgelist)
# draw_graph(G)

edgeSplitter = EdgeSplitter(G)
graph_test, samples_test, labels_test = edgeSplitter.train_test_split(
    p=0.1, method="global"
)

edgeSplitter = EdgeSplitter(graph_test, G)
graph_train, samples_train, labels_train = edgeSplitter.train_test_split(
    p=0.1, method="global"
)


print(type(graph_train))

node2vec = Node2Vec(graph_train)
model = node2vec.fit()
edges_embs = HadamardEmbedder(keyed_vectors=model.wv)
train_embeddings = [edges_embs[str(x[0]),str(x[1])] for x in samples_train]

test_embeddings = [edges_embs[str(x[0]),str(x[1])] for x in samples_test]


"""
rf = RandomForestClassifier(n_estimators=1000)
rf.fit(train_embeddings, labels_train);


y_pred = rf.predict(test_embeddings)

print('Precision:', metrics.precision_score(labels_test, y_pred))
print('Recall:', metrics.recall_score(labels_test, y_pred))
print('F1-Score:', metrics.f1_score(labels_test, y_pred))
"""

print("---")

rf = AdaBoostClassifier(n_estimators=1000)
rf.fit(train_embeddings, labels_train);

y_pred = rf.predict(test_embeddings)

print('Precision:', metrics.precision_score(labels_test, y_pred))
print('Recall:', metrics.recall_score(labels_test, y_pred))
print('F1-Score:', metrics.f1_score(labels_test, y_pred))

