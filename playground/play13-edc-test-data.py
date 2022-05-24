
from gml.graph.graph_viz import GraphViz
from gml.graph.data_factory import DataFactory

print("#")
print("# Test data for EDC")
print("#")

graph = DataFactory().create_graph(add_dc=True, directed=True, typed=True)
graph.draw()
graph.draw(layout=GraphViz.SPIRAL_LAYOUT)
graph.draw(layout=GraphViz.SPECTRAL_LAYOUT)

