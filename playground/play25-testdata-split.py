from stellargraph.data import EdgeSplitter
from gml.graph.data_factory import DataFactory, MatchingCluster, Employee, DataCollection

print("EdgeSplitter Test:")

# Graph
graph = DataFactory().create_graph(n=4, add_dc=True, connected=True)

# test_graph
edgeSplitter = EdgeSplitter(graph.graph)
test_graph, test_samples, test_labels  = edgeSplitter.train_test_split(p=0.1, method="global", keep_connected=True)

# train_graph
edgeSplitter = EdgeSplitter(test_graph, graph.graph)
train_graph, train_samples, train_labels = edgeSplitter.train_test_split(p=0.1, method="global", keep_connected=True)

print("Orig. graph: nodes={}, edges={}".format(len(graph.nodes), len(graph.edges)))
print("Test  graph: nodes={}, edges={}".format(len(test_graph.nodes), len(test_graph.edges)))
print("Train graph: nodes={}, edges={}".format(len(train_graph.nodes), len(train_graph.edges)))

