from gml.graph.graph_viz import GraphViz
from gml.graph.data_factory import DataFactory, EdgeLabelFactory

graph = DataFactory().create_graph_with_doubles(n=1, add_dc=True)
graph.draw(layout=GraphViz.SPIRAL_LAYOUT)

graph = DataFactory().create_graph_with_doubles(n=1, add_id=False, add_dc=True)
graph.draw(layout=GraphViz.SPIRAL_LAYOUT)



