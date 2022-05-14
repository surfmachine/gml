import random
import networkx as nx
from karateclub import Graph2Vec
import matplotlib.pyplot as plt

from gml.graph.graph_builder import GraphBuilder


print("#")
print("# Grap Embeddings")
print("#")

n_graphs = 6

def generate_radom():
    n = random.randint(6, 20)
    k = random.randint(5, n)
    p = random.uniform(0, 1)
    return nx.watts_strogatz_graph(n,k,p), [n,k,p]

Gs = [generate_radom() for x in range(n_graphs)]

i = 0
for g in Gs:
    print("--- Graph {} ---".format(i))
    print("nodes: ", g[0].nodes)
    print("edges: ", g[0].edges)
    i += 1

model = Graph2Vec(dimensions=2, wl_iterations=10)
model.fit([x[0] for x in Gs])
embeddings = model.get_embedding()

fig, ax = plt.subplots(figsize=(10,10))

for i,vec in enumerate(embeddings):
    ax.scatter(vec[0],vec[1], s=1000)
    ax.annotate(str(i), (vec[0],vec[1]), fontsize=40)

plt.show()



print("#")
print("# Grap Embeddings node and edge details")
print("#")

n_graphs = 6

def generate_radom_graphs():
    n = random.randint(6, 20)
    k = random.randint(5, n)
    p = random.uniform(0, 1)
    return nx.watts_strogatz_graph(n,k,p)

graphs = [generate_radom() for x in range(n_graphs)]

i = 0
for g in graphs:
    print("--- Graph {} ---".format(i))
    print("nodes: ", g[0].nodes)
    print("edges: ", g[0].edges)
    # GraphViz.draw(g[0])
    i += 1


model = Graph2Vec(dimensions=2, wl_iterations=10)
model.fit([x[0] for x in graphs])
embeddings = model.get_embedding()

fig, ax = plt.subplots(figsize=(10,10))

for i,vec in enumerate(embeddings):
    ax.scatter(vec[0],vec[1], s=1000)
    ax.annotate(str(i), (vec[0],vec[1]), fontsize=40)

plt.show()

print("#")
print("# Grap Embeddings watts strogatz graph")
print("#")

"""
nx.watts_strogatz_graph(n,k,p)
    n: int    The number of nodes.
    k: int    Each node is joined with its k nearest neighbors in a ring topology.
    p: float  The probability of adding a new edge for each edge.
    seed: int random_state, or None (default)
              Indicator of random number generation state. See Randomness.
"""

gx1 = nx.watts_strogatz_graph(6,3,0.2, seed=1)
gx2 = nx.watts_strogatz_graph(12,4,0.2, seed=1)
gx3 = nx.watts_strogatz_graph(24,12,0.2, seed=1)

g1 = GraphBuilder().append_nodes(gx1.nodes).append_edges(gx1.edges).create()
g2 = GraphBuilder().append_nodes(gx2.nodes).append_edges(gx2.edges).create()
g3 = GraphBuilder().append_nodes(gx3.nodes).append_edges(gx3.edges).create()

graphs = [g1, g2, g3]

viz = True
props = False

for g in graphs:
    if viz:
        g.draw()
    if props:
        g.print_properties()


model = Graph2Vec(dimensions=2, wl_iterations=10)
model.fit([x.graph for x in graphs])
embeddings = model.get_embedding()

fig, ax = plt.subplots(figsize=(10,10))

for i,vec in enumerate(embeddings):
    ax.scatter(vec[0],vec[1], s=1000)
    ax.annotate(str(i), (vec[0],vec[1]), fontsize=40)

plt.show()
