import networkx as nx
from gml.graph.graph_builder import GraphBuilder


print("#")
print("# Link Prediction - Community Based")
print("#")

edges = [(1,3),(2,3),(2,4),(4,5),(5,6),(5,7)]
graph = GraphBuilder().append_edges(edges).create()
# graph.draw()

print(graph.graph.nodes)

graph.graph.nodes[1]["community"] = 0
graph.graph.nodes[2]["community"] = 0
graph.graph.nodes[3]["community"] = 0

graph.graph.nodes[4]["community"] = 1
graph.graph.nodes[5]["community"] = 1
graph.graph.nodes[6]["community"] = 1
graph.graph.nodes[7]["community"] = 1


print("#")
print("# Community Common Neighbor - cn_soundarajan_hopcroft")
print("#")

preds = nx.cn_soundarajan_hopcroft(graph.graph,[(1,2),(2,5),(3,4)])
print(list(preds))


print("#")
print("# Community resource allocation - ra_index_soundarajan_hopcroft")
print("#")

preds = nx.ra_index_soundarajan_hopcroft(graph.graph,[(1,2),(2,5),(3,4)])
print(list(preds))

print("#")
print("# within_inter_cluster")
print("#")

preds = nx.within_inter_cluster(graph.graph,[(1,2),(2,5),(3,4)])
print(list(preds))


print("#")
print("# common_neighbor_centrality")
print("#")

preds = nx.common_neighbor_centrality(graph.graph,[(1,2),(2,5),(3,4)])
print(list(preds))


