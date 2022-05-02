import networkx as nx
import matplotlib.pyplot as plt

from gml.graph.graph_builder import GraphBuilder

print("#")
print("# Create multi graph with networkx")
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


directed_multi_graph = nx.MultiDiGraph()
nodes = {'Dublin', 'Paris', 'Milan', 'Rome'}
edges = [('Milan','Dublin'), ('Milan','Dublin'), ('Dublin', 'Milan'), ('Paris','Milan'), ('Paris','Dublin'), ('Milan','Rome'), ('Milan','Rome')]
directed_multi_graph.add_nodes_from(nodes)
directed_multi_graph.add_edges_from(edges)

draw_graph(directed_multi_graph, pos_nodes=nx.shell_layout(directed_multi_graph), node_size=500)
# draw_graph(directed_multi_graph, pos_nodes=nx.drawing.spring_layout(directed_multi_graph), node_size=500)


print("#")
print("# Create multi graph with graph classes")
print("#")

# graph = GraphBuilder()\
#     .append_nodes(nodes)\
#     .append_edges(edges)\
#     .create_directed()

# graph.draw()
# graph.print_properties()

print("#")
print("# Create multi graph with graph classes 2")
print("#")

nodes = ['Alice','David', 'Emma', 'Luca', 'Zora']
edges = [('Alice', 'David'), ('Alice', 'Luca'), ('Alice', 'Zora'), ('David', 'Emma'), ('Emma', 'Luca'), ('Luca', 'Zora'), ('David', 'Alice')]

graph = GraphBuilder().append_nodes(nodes).append_edges(edges).create()
graph.draw()