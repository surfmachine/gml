import networkx as nx
from gml.graph.graph_builder import GraphBuilder


print("#")
print("# Link Prediction - Index Based")
print("#")

edges = [(1,3),(2,3),(2,4),(4,5),(5,6),(5,7)]
graph = GraphBuilder().append_edges(edges).create()
graph.draw()

possible_edges = [(1,2),(2,5),(3,4),(6,7),(1,4),(1,7)]

print("Resource Allocation")
predictions = nx.resource_allocation_index(graph.graph,possible_edges)
print(list(predictions))

print("Jaccard Coefficient")
preds = nx.jaccard_coefficient(graph.graph,possible_edges)
print(list(preds))

print("#")
print("# Link Prediction - Index Based EDC Sample")
print("#")

edges = [
    ("PL","Peter"),("PL","Lang"),("PL","U11"),("D1","Peter"),("D1","Lang"),("D1","U11"),
    ("ZI","Zoe"),("ZI","Iten"),("D2","Zoe"),("D2","Iten"),
    ("JK","John"),("JK","Kathy"),("D3","John"),
]
graph = GraphBuilder().append_edges(edges).create()
graph.draw()

possible_edges = [("PL","D1"),("PL","D2"),("PL","D3"),
                 ("ZI","D1"),("ZI","D2"),("ZI","D3"),
                 ("JK","D1"),("JK","D2"),("JK","D3")]

print("Resource Allocation")
predictions = nx.resource_allocation_index(graph.graph,possible_edges)
print(list(predictions))

print("Jaccard Coefficient")
preds = nx.jaccard_coefficient(graph.graph,possible_edges)
print(list(preds))


print("#")
print("# Link Prediction - Index Based EDC Sample with Weights")
print("#")

edges = [
    ("PL","Peter",0.5),("PL","Lang",0.5),("PL","U11",1.0),("D1","Peter",0),("D1","Lang",0),("D1","U11",0),
    ("ZI","Zoe",0.5),("ZI","Iten",0.5),("D2","Zoe",0),("D2","Iten",0),
    ("JK","John",0.5),("JK","Kathy",0.5),("D3","John",0),
]
graph = GraphBuilder().append_edges(edges).create()
graph.draw()

possible_edges = [("PL","D1"),("PL","D2"),("PL","D3"),
                 ("ZI","D1"),("ZI","D2"),("ZI","D3"),
                 ("JK","D1"),("JK","D2"),("JK","D3")]

print("Resource Allocation")
predictions = nx.resource_allocation_index(graph.graph,possible_edges)
print(list(predictions))

print("Jaccard Coefficient")
preds = nx.jaccard_coefficient(graph.graph,possible_edges)
print(list(preds))


print("#")
print("# Link Prediction - Index Based EDC Sample with additional property nodes")
print("#")

edges = [
    ("PL","Firstname"), ("Firstname","Peter"),("PL","Lastname"),("Lastname","Lang"),("PL","Id"),("Id","U11"),("D1","Peter"),("D1","Lang"),("D1","U11"),
    ("ZI","Zoe"),("ZI","Iten"),("D2","Zoe"),("D2","Iten")
]
graph = GraphBuilder().append_edges(edges).create()
graph.draw()

possible_edges = [("PL","D1"),("PL","D2"),("ZI","D1"),("ZI","D2")]

print("Resource Allocation")
predictions = nx.resource_allocation_index(graph.graph,possible_edges)
print(list(predictions))

print("Jaccard Coefficient")
preds = nx.jaccard_coefficient(graph.graph,possible_edges)
print(list(preds))

