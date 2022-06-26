import numpy as np
from tensorflow import keras
import networkx as nx
from stellargraph import StellarGraph
from stellargraph.data import EdgeSplitter
from stellargraph.mapper import GraphSAGELinkGenerator
from stellargraph.layer import GraphSAGE, link_classification
from gml.graph.data_factory import DataFactory, MatchingCluster, Employee, DataCollection
from gml.measure.system_meter import CpuSystemMeter, MemorySystemMeter, TimeSystemMeter

print("#")
print("# Performance Tests with GNN based algorithms")
print("#")

sizes = [100, 1000, 2500] # , 5000, 10000, 15000]
meters = [TimeSystemMeter(), MemorySystemMeter(), CpuSystemMeter()]

for size in sizes:

    # create graph
    for meter in meters:
        meter.start()

    graph = DataFactory().create_graph(n=size, add_dc=True, connected=True)

    # Testdaten
    edgeSplitter = EdgeSplitter(graph.graph)
    test_graph, test_samples, test_labels  = edgeSplitter.train_test_split(p=0.1, method="global", keep_connected=True)

    # Trainingsdaten
    edgeSplitter = EdgeSplitter(test_graph, graph.graph)
    train_graph, train_samples, train_labels = edgeSplitter.train_test_split(p=0.1, method="global", keep_connected=True)

    # Node Features hinzufügen
    node_features="idm"
    eye = np.eye(test_graph.number_of_nodes())                      # Identiy matrix (idm) with size = number of nodes
    idm = {n:eye[i] for i,n in enumerate(test_graph.nodes())}       # Dictionary with node number as key and corresponding idm row as value
    nx.set_node_attributes(test_graph, idm, node_features)          # Assign node features (with name 'idm') to the test_graph nodes

    eye = np.eye(train_graph.number_of_nodes())
    idm = {n:eye[i] for i,n in enumerate(train_graph.nodes())}
    nx.set_node_attributes(train_graph, idm, node_features)

    # Link Generator definieren
    batch_size = 64
    num_samples = [4, 4]

    train_sg   = StellarGraph.from_networkx(train_graph, node_features=node_features)
    train_gen  = GraphSAGELinkGenerator(train_sg, batch_size, num_samples)
    train_flow = train_gen.flow(train_samples, train_labels, shuffle=True, seed=24)

    test_sg    = StellarGraph.from_networkx(test_graph, node_features=node_features)
    test_gen   = GraphSAGELinkGenerator(test_sg, batch_size, num_samples)
    test_flow  = test_gen.flow(test_samples, test_labels, seed=24)

    # Model training
    layer_sizes = [20, 20]
    graphsage = GraphSAGE(
        layer_sizes=layer_sizes,
        generator=train_gen,
        bias=True,
        dropout=0.3)

    x_inp, x_out = graphsage.in_out_tensors()
    prediction   = link_classification(output_dim=1, output_act="sigmoid", edge_embedding_method="ip")(x_out)

    model = keras.Model(inputs=x_inp, outputs=prediction)
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=1e-3),
        loss=keras.losses.mse,
        metrics=["acc"],
    )

    # Model trainieren
    epochs = 24
    history = model.fit(train_flow, epochs=epochs, validation_data=test_flow)


    # Prediction
    y_pred = np.round(model.predict(test_flow)).flatten()

    for meter in meters:
        meter.stop()
        print(meter.name, ":", meter.result())


