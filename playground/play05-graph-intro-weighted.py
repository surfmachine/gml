import networkx as nx
import matplotlib.pyplot as plt

from gml.graph.graph_builder import GraphBuilder

print("#")
print("# Create weighted graph with networkx")
print("#")

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


graph = nx.MultiDiGraph()
nodes = {'Paris', 'Dublin','Milan', 'Rome'}
edges = [ ('Paris','Dublin', 11), ('Paris','Milan', 8),
      ('Milan','Rome', 5),('Milan','Dublin', 19)]
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)

draw_graph(graph, pos_nodes=nx.shell_layout(graph), node_size=500, plot_weight=True)


print("#")
print("# Create weighted graph graph classes")
print("#")

graph = GraphBuilder().append_nodes(nodes).append_edges(edges).create_directed()
graph.draw()

