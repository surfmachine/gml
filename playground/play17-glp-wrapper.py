
import networkx as nx
from gml.graph.graph_builder import GraphBuilder
from gml.graph.graph_link import GraphLink, Algorithm

print("#")
print("# Link Prediction - Native")
print("#")


edges = [(1,3),(2,3),(2,4),(4,5),(5,6),(5,7)]
graph = GraphBuilder().append_edges(edges).create()
# graph.draw()

possible_edges = [(1,2),(2,5),(3,4),(6,7),(1,4),(1,7)]

print("Resource Allocation")
predictions = nx.resource_allocation_index(graph.graph,possible_edges)
print(list(predictions))


print("#")
print("# Link Prediction - Wrapper")
print("#")

result = GraphLink(graph, possible_edges).predict(Algorithm.RESOURCE_ALLOCATION_INDEX).to_list()
print(result)

print("#")
print("# Link Prediction - Wrapper Multipredic")
print("#")

GraphLink(graph, possible_edges)\
    .predict(Algorithm.RESOURCE_ALLOCATION_INDEX, Algorithm.JACCARD_COEFFICIENT)\
    .predict(Algorithm.ADAMIC_ADAR_INDEX)\
    .print_results()

# --------------------------------------------------------------------------------------------------------------------

print("#")
print("# Link Prediction - Native Community")
print("#")

edges = [(1,3),(2,3),(2,4),(4,5),(5,6),(5,7)]
graph = GraphBuilder()\
    .append_edges(edges)\
    .create()

graph.graph.nodes[1]["community"] = 0
graph.graph.nodes[2]["community"] = 0
graph.graph.nodes[3]["community"] = 0

graph.graph.nodes[4]["community"] = 1
graph.graph.nodes[5]["community"] = 1
graph.graph.nodes[6]["community"] = 1
graph.graph.nodes[7]["community"] = 1

preds = nx.cn_soundarajan_hopcroft(graph.graph,[(1,2),(2,5),(3,4)])
print(list(preds))


print("#")
print("# Link Prediction - Builder Community")
print("#")

edges = [(1,3),(2,3),(2,4),(4,5),(5,6),(5,7)]

graph = GraphBuilder() \
    .append_edges(edges) \
    .append_community(0, [1, 2, 3]) \
    .append_community(1, [4, 5, 6, 7]) \
    .create()

possible_edges = [(1,2),(2,5),(3,4)]

GraphLink(graph, possible_edges) \
    .predict(Algorithm.SOUNDARAJAN_HOPCROFT) \
    .print_results()

graph = GraphBuilder() \
    .append_edges(edges) \
    .append_communities([ (0, [1, 2, 3]), (1, [4, 5, 6, 7]) ]) \
    .create()

GraphLink(graph, possible_edges) \
    .predict(Algorithm.SOUNDARAJAN_HOPCROFT) \
    .print_results()
