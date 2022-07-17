
import networkx as nx
from gml.graph.graph_builder import GraphBuilder
from gml.graph.graph_link import GraphLink, Algorithm


print("#")
print("# Link Prediction - Wrapper - Normalize resutls to 0..1")
print("#")

edges = [(1,3),(2,3),(2,4),(4,5),(5,6),(5,7)]
graph = GraphBuilder().append_edges(edges).create()
possible_edges = [(1,2),(2,5),(3,4),(6,7),(1,4),(1,7)]


gl = GraphLink(graph, possible_edges)\
    .predict(Algorithm.RESOURCE_ALLOCATION_INDEX, Algorithm.JACCARD_COEFFICIENT)\
    .predict(Algorithm.ADAMIC_ADAR_INDEX)\

gl.print_results(incl_legend=False)
gl.print_results(normalize=True, incl_legend=False, title="Normalized results:")


gl.filter([(1,2), (6,7), (1,7)])
gl.print_results(incl_legend=False)



