
from gml.graph.graph_viz import GraphViz
from gml.graph.data_factory import DataFactory

print("#")
print("# Test data for EDC - Connected Graph")
print("#")

graph = DataFactory().create_graph(n=3, connected=True)
graph.draw()

graph = DataFactory().create_graph(n=2, connected=True, directed=True, add_dc=True)
graph.draw()
