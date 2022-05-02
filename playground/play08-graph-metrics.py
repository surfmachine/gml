import pandas as pd
import networkx as nx
import networkx.algorithms.community as nxc

from gml.graph.graph_builder import GraphBuilder

print("#")
print("# Metrics - shorted path")
print("#")

edges = [('Genf', 'Lausanne'), ('Lausanne', 'Montreux'), ('Montreux', 'Bern'), ('Lausanne', 'Bern'), ('Bern', 'Zürich'), ('Bern', 'Basel'), ('Basel', 'Zürich')]
graph = GraphBuilder().append_edges(edges).create()

path = nx.shortest_path(graph.graph,source='Genf',target='Zürich')
print(path)

# graph.draw(path=path)


print("#")
print("# Metrics - node combinations")
print("#")

edges = [('Genf', 'Lausanne'), ('Lausanne', 'Montreux'), ('Montreux', 'Bern'), ('Lausanne', 'Bern')]
graph = GraphBuilder().append_edges(edges).create()

combinations = []
i = 0
j = i + 1
while i < len(graph.nodes):
    # print(graph.nodes[i])
    while j < len(graph.nodes):
        combinations.append( [graph.nodes[i], graph.nodes[j]] )
        j = j + 1
    i += 1
    j = i + 1
print(combinations)


print("#")
print("# Metrics - shortest path combinations")
print("#")

edges = [('Genf', 'Lausanne'), ('Lausanne', 'Montreux'), ('Montreux', 'Bern'), ('Lausanne', 'Bern')]
graph = GraphBuilder().append_edges(edges).create()

print( graph.shortest_path_combinations() )


print("#")
print("# Metrics - clustering")
print("#")

edges = [('Genf', 'Lausanne'), ('Lausanne', 'Montreux'), ('Montreux', 'Bern'), ('Lausanne', 'Bern')]
graph = GraphBuilder().append_edges(edges).create()

clusters = graph.clustering(pandas_df=False)
print(clusters)

cluster_list = [(k,v) for k, v in clusters.items() ]
print(cluster_list)

df = pd.DataFrame(cluster_list, columns=["Node", "Clustering coefficient"])
print(df)


print("#")
print("# Metrics - modularity")
print("#")

edges = [('Genf', 'Lausanne'), ('Lausanne', 'Montreux'), ('Montreux', 'Bern'), ('Lausanne', 'Bern'), ('Bern', 'Zürich'), ('Bern', 'Basel'), ('Basel', 'Zürich')]
graph = GraphBuilder().append_edges(edges).create()

mod = nxc.modularity(graph.graph, communities=[('Genf', 'Lausanne', 'Montreux'), ('Bern', 'Basel', 'Zürich')])
print(mod)

edges = [('Genf', 'Lausanne'), ('Lausanne', 'Montreux'), ('Lausanne', 'Fribourg'), ('Montreux', 'Fribourg'),
         ('Fribourg', 'Bern'), ('Bern', 'Zürich'), ('Bern', 'Basel'), ('Basel', 'Zürich')]
graph = GraphBuilder().append_edges(edges).create()
graph.draw()

mod = nxc.modularity(graph.graph, communities=[('Genf', 'Lausanne', 'Montreux', 'Fribourg'), ('Bern', 'Basel', 'Zürich')])
print(mod)

print("#")
print("# Metrics - centrality")
print("#")

print(graph.centrality_degree())
print(graph.centrality_closeness())
print(graph.centrality_betweenness())


def common_entries(*dcts):
    if not dcts:
        return
    for i in set(dcts[0]).intersection(*dcts[1:]):
        yield (i,) + tuple(d[i] for d in dcts)

res = common_entries(
    graph.centrality_degree(),
    graph.centrality_closeness(),
    graph.centrality_betweenness()
)

data = list(res)
print(data)
df = pd.DataFrame(data, columns=['Node','Degree','Closeness','Betweennness'])
print(df)

print("---")

def zip_dict(*dicts):
    result = []
    for key in dicts[0].keys():
        entries = [key]
        for dict in dicts:
            entries.append(dict[key])
        result.append(entries)
    return result

res = zip_dict(
    graph.centrality_degree(),
    graph.centrality_closeness(),
    graph.centrality_betweenness()
)

print(res)
print(graph.centrality())

# [(k,v) for k, v in nx.clustering(self.graph).items() ]