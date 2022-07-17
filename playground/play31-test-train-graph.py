from gml.graph.data_factory import DataFactory, EdgeLabelFactory, TestTrainDataFactory
from gml.graph.graph_builder import GraphBuilder


n = 200
from_node = "EM"
to_node = "DC"

df = DataFactory()
ef = EdgeLabelFactory()

base_edges = df.create_edges_with_doubles(n=n, add_id=False, add_dc=True)  # graph edges without predict edges
link_edges = ef.sample_positive(from_node, to_node, n, p=1)                # graph predict edges (positive)
graph = GraphBuilder().append_edges(base_edges).append_edges(link_edges).create()

print("All positive link edges:")
print(link_edges)

test_edges, test_samples, test_labels = ef.edge_splitter(from_node, to_node, link_edges, p=0.2, shuffle=True)
test_graph = GraphBuilder().append_edges(base_edges).append_edges(test_edges).create()
print("Test data:")
print(test_edges)
print(test_samples)
print(test_labels)


train_edges, train_samples, train_labels = ef.edge_splitter(from_node, to_node, test_edges, p=0.2, shuffle=True)
train_graph = GraphBuilder().append_edges(base_edges).append_edges(train_edges).create()
print("Train data:")
print(train_edges)
print(train_samples)
print(train_labels)

graph.print_dimemsions("Graph")
test_graph.print_dimemsions("Test Graph")
train_graph.print_dimemsions("Train Graph")

print("------------------------------------")

graph, test_graph, test_samples, test_labels, train_graph, train_samples, train_labels \
    = TestTrainDataFactory().create_testdata(n)

graph.print_dimemsions("Graph")
test_graph.print_dimemsions("Test Graph")
train_graph.print_dimemsions("Train Graph")

print(test_samples)
print(test_labels)




