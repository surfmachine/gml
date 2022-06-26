from gml.graph.graph_viz import GraphViz
from gml.graph.data_factory import DataFactory, MatchingCluster, Employee, DataCollection
from gml.graph.graph_link import GraphLink, Algorithm
from gml.measure.system_meter import CpuSystemMeter, MemorySystemMeter, TimeSystemMeter

print("#")
print("# Performance Tests with Index based algorithms")
print("#")

#
# Create graph
#
n = 2

graph = DataFactory().create_graph(n=n, add_dc=True, connected=True)

if n < 3:
    graph.draw(layout=GraphViz.SPIRAL_LAYOUT)
graph.print_dimemsions()


#
# Create possible edges
#
possible_edges = []
for i in range(n):
    dc = DataCollection.create_name(i)
    mc = MatchingCluster.create_name(i)
    em = Employee.create_name(i)
    possible_edges.append((em, dc))
    possible_edges.append((em, mc))

if n < 3:
    print("Possible edges:")
    print(possible_edges)


#
# Link prediction
#
GraphLink(graph, possible_edges) \
    .predict(Algorithm.RESOURCE_ALLOCATION_INDEX) \
    .predict(Algorithm.JACCARD_COEFFICIENT) \
    .predict(Algorithm.ADAMIC_ADAR_INDEX) \
    .predict(Algorithm.PREFERENTIAL_ATTACHMENT) \
    .print_results()


print("#")
print("# Performance measures")
print("#")

sizes = [100, 1000, 2500] # , 5000, 10000, 15000]
meters = [TimeSystemMeter(), MemorySystemMeter(), CpuSystemMeter()]

for size in sizes:

    # create graph
    for meter in meters:
        meter.start()

    graph = DataFactory().create_graph(n=size, add_dc=True, connected=True)

    possible_edges = []
    for i in range(size):
        dc = DataCollection.create_name(i)
        mc = MatchingCluster.create_name(i)
        em = Employee.create_name(i)
        possible_edges.append((em, dc))
        possible_edges.append((em, mc))

    title = "Graph with size: " + str(size)
    graph.print_dimemsions(title=title)
    print("  possible edges size:", len(possible_edges))

    for meter in meters:
        meter.stop()
        print("  create", meter.name, ":", meter.result())

    # link prediction
    for meter in meters:
        meter.start()

    GraphLink(graph, possible_edges) \
        .predict(Algorithm.RESOURCE_ALLOCATION_INDEX) \
        .predict(Algorithm.JACCARD_COEFFICIENT) \
        .predict(Algorithm.ADAMIC_ADAR_INDEX) \
        .predict(Algorithm.PREFERENTIAL_ATTACHMENT)

    for meter in meters:
        meter.stop()
        print("  prediction", meter.name, ":", meter.result())

