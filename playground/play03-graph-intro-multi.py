import networkx as nx
import matplotlib.pyplot as plt

from gml.graph.graph_builder import GraphBuilder

print("#")
print("# Create multi graph with networkx")
print("#")

G = nx.MultiDiGraph()
G.add_node('n1')
G.add_node('n2')
G.add_edge('n1', 'n2', rad=0.1)
G.add_edge('n1', 'n2', rad=0.2)
G.add_edge('n1', 'n2', rad=0.3)

plt.figure(figsize=(6,6))

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)

for edge in G.edges(data=True):
    nx.draw_networkx_edges(G, pos, edgelist=[(edge[0],edge[1])], connectionstyle=f'arc3, rad = {edge[2]["rad"]}')
plt.show()


print("#")
print("# Detect multi graph")
print("#")

edges = [('Alice', 'David'), ('Alice', 'Zora'), ('David', 'Emma'), ('Emma', 'Luca'), ('Alice', 'David')]
# edges = [('David', 'Alice'), ('Alice', 'Zora'), ('David', 'Emma'), ('Emma', 'Luca'), ('Alice', 'David')]

multi = False
for i in range(len(edges)):
    item = edges[i]
    rev_item = (item[1], item[0])
    others = edges[i+1:]
    exist = True if (item in others or rev_item in others) else False
    print(i, ":", item, "in", others, "=", exist)
    if exist:
        multi = True

print("Multi :", multi)

print("#")
print("# Create plain edges list for weighted edges")
print("#")

# edges = []
# edges = [('Alice', 'David'), ('Alice', 'Zora'), ('David', 'Emma'), ('Emma', 'Luca'), ('Alice', 'David')]
edges = [('Alice', 'David', 5), ('Alice', 'Zora', 2), ('David', 'Emma', 4), ('Emma', 'Luca', 5), ('Alice', 'David', 7)]
weighted = True if (len(edges) > 0 and len(edges[0]) > 2) else False

print(weighted)

if weighted:
    edges2 = []
    for edge in edges:
        edges2.append( (edge[0], edge[1]) )
    print(edges2)




