import random
import networkx as nx
from gml.graph.graph_builder import GraphBuilder
from gml.graph.graph_generator import GraphGenerator
from gml.graph.graph_embedding import GraphEmbedding

print("#")
print("# Grap Embeddings watts strogatz graph generic")
print("#")

"""
nx.watts_strogatz_graph(n,k,p)
    n: int    The number of nodes.
    k: int    Each node is joined with its k nearest neighbors in a ring topology.
    p: float  The probability of adding a new edge for each edge.
    seed: int random_state, or None (default)
              Indicator of random number generation state. See Randomness.
"""


def generate_radom_params():
    n = random.randint(6, 24)
    k = random.randint(3, n)
    p = random.uniform(0, 1)
    return [n,k,p]

n_graphs = 12
params = [generate_radom_params() for i in range(n_graphs)]

graphs = []
for p in params:
    g = nx.watts_strogatz_graph(*p, seed=1)
    graphs.append(GraphBuilder().append_nodes(g.nodes).append_edges(g.edges).create())

viz = False
props = False

for g in graphs:
    if viz:
        g.draw()
    if props:
        g.print_properties()

if viz:
    GraphEmbedding(graphs).draw()


print("#")
print("# Grap Embeddings watts strogatz graph generic")
print("#")

n_graphs = 12
graphs = GraphGenerator().append_random_watts_stragatz(n_graphs).create()

for g in graphs:
    g.draw()

GraphEmbedding(graphs).draw()

edges = [ (i, i+1) for i in range(1,13,2) ]
print(edges)
