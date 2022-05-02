
from gml.graph.graph_builder import GraphBuilder

print("#")
print("# Matrix ungerichtet")
print("#")

nodes = ['Alice','David', 'Emma', 'Luca', 'Zora']
edges = [('Alice', 'David'), ('Alice', 'Luca'), ('Alice', 'Zora'), ('David', 'Emma'), ('Emma', 'Luca'), ('Luca', 'Zora')]

graph = GraphBuilder().append_nodes(nodes).append_edges(edges).create()
graph.print_matrix()

print("#")
print("# Matrix gerichtet")
print("#")

graph = GraphBuilder().append_nodes(nodes).append_edges(edges).create_directed()
graph.print_matrix()


print("#")
print("# Matrix ungerichtet Multigraph")
print("#")

nodes = ['Alice','David', 'Emma', 'Luca', 'Zora']
edges = [('Alice', 'David', 1), ('Alice', 'Luca', 7), ('Alice', 'Zora', 4), ('David', 'Emma', 9), ('Emma', 'Luca', 5), ('Luca', 'Zora', 2)]

graph = GraphBuilder().append_nodes(nodes).append_edges(edges).create()
graph.print_matrix()

print("#")
print("# Matrix gerichtet Multigraph")
print("#")

graph = GraphBuilder().append_nodes(nodes).append_edges(edges).create_directed()
graph.print_matrix()
