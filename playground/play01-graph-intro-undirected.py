import networkx as nx
import matplotlib.pyplot as plt

from gml.graph.graph_builder import GraphBuilder

print("#")
print("# Create graph with networkx")
print("#")

def print_graph(graph):
    print("Graph:")
    print("- Nodes    :", graph.nodes)
    print("- Edges    :", graph.edges)
    print("- Order    :", graph.number_of_nodes())
    print("- Size     :", graph.number_of_edges())
    degrees = []
    neighbors = []
    for node in graph.nodes:
        degrees.append( node + "=" + str( graph.degree(node) ) )
        neighbors.append( node + "=" + str( list(graph.neighbors(node)) ) )
    print("- Degrees  :", degrees)
    print("- Neighbors:", neighbors)


def draw_graph(G, pos_nodes, node_names={}, node_size=50, plot_weight=False):
    nx.draw(G, pos_nodes, with_labels=False, node_size=node_size, edge_color='gray', arrowsize=30)

    pos_attrs = {}
    for node, coords in pos_nodes.items():
        pos_attrs[node] = (coords[0], coords[1] + 0.08)

    nx.draw_networkx_labels(G, pos_attrs, font_family='serif', font_size=20)


    if plot_weight:
        pos_attrs = {}
        for node, coords in pos_nodes.items():
            pos_attrs[node] = (coords[0], coords[1] + 0.08)

        nx.draw_networkx_labels(G, pos_attrs, font_family='serif', font_size=20)
        edge_labels=dict([((a,b,),d["weight"]) for a,b,d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos_nodes, edge_labels=edge_labels)

    plt.axis('off')
    axis = plt.gca()
    axis.set_xlim([1.2*x for x in axis.get_xlim()])
    axis.set_ylim([1.2*y for y in axis.get_ylim()])
    plt.show()

nodes = {'Dublin', 'Paris', 'Milan', 'Rome'}
edges = [('Milan','Dublin'), ('Milan','Paris'), ('Paris','Dublin'), ('Milan','Rome')]

graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_edges_from(edges)

print_graph(graph)
# draw_graph(graph, nx.shell_layout(graph))


print("#")
print("# Create graph with graph classes")
print("#")

graph = GraphBuilder()\
    .append_nodes(nodes)\
    .append_edges(edges)\
    .create()

graph.print_properties()
graph.draw()

# Override some styles
# mystyles = GraphViz.get_styles()
# mystyles['node_color'] = 'blue'
# graph.draw(styles=mystyles)

