
from gml.graph.graph_builder import GraphBuilder

print("#")
print("# Matrix ungerichtet")
print("#")

edges = [('Alice', 'David'), ('Alice', 'Luca'), ('Alice', 'Zora'), ('David', 'Emma'), ('Emma', 'Luca'), ('Luca', 'Zora'), ('Mike')]

graph = GraphBuilder().append_edges(edges).create()
graph.draw()
graph.print_edgelist()

print("#")
print("# Matrix gerichtet")
print("#")

graph = GraphBuilder().append_edges(edges).create_directed()
graph.print_edgelist()


print("#")
print("# Matrix ungerichtet Multigraph")
print("#")

edges = [('Alice', 'David', 1), ('Alice', 'Luca', 7), ('Alice', 'Zora', 4), ('David', 'Emma', 9), ('Emma', 'Luca', 5), ('Luca', 'Zora', 2)]

graph = GraphBuilder().append_edges(edges).create()
graph.print_edgelist()

print("#")
print("# Matrix gerichtet Multigraph")
print("#")

graph = GraphBuilder().append_edges(edges).create_directed()
graph.print_edgelist()

""" 
 
print("#")
print("# Matrix ungerichtet Multigraph")
print("#")

edges = [('Alice', 'David', {'w':1, 'c':1}), ('Alice', 'Luca', {'w':1, 'c':1}), ('Alice', 'Zora', {'w':1, 'c':1}),
         ('David', 'Emma', {'w':1, 'c':1}), ('Emma', 'Luca', {'w':1, 'c':1}), ('Luca', 'Zora', {'w':1, 'c':1})]

graph = GraphBuilder().append_edges(edges).create()
graph.draw()
graph.print_edgelist()

"""