import unittest
from gml.graph.graph_builder import GraphBuilder

class GraphBuilderTest(unittest.TestCase):

    def test_append_node(self):
        gb = GraphBuilder()
        gb.append_node("Bern")
        gb.append_node("Lausanne")
        gb.append_node("Genf")
        gb.append_node("Bern")
        self.assertEqual(3, len(gb.nodes))
        self.assertEqual(['Bern', 'Lausanne', 'Genf'], gb.nodes )

    def test_append_nodes(self):
        gb = GraphBuilder()
        gb.append_nodes(("Bern", "Lausanne"))
        gb.append_nodes(["Genf","Bern"])
        self.assertEqual(3, len(gb.nodes))
        self.assertEqual(['Bern', 'Lausanne', 'Genf'], gb.nodes )

    def test_append_edge(self):
        gb = GraphBuilder()
        gb.append_edge(("Bern", "Lausanne"))
        gb.append_edge(("Lausanne", "Genf"))
        self.assertEqual(3, len(gb.nodes))
        self.assertEqual(['Bern', 'Lausanne', 'Genf'], gb.nodes )
        self.assertEqual([('Bern', 'Lausanne'), ('Lausanne', 'Genf')], gb.edges)
        gb.append_edge(("Bern", "Genf"))
        self.assertEqual(3, len(gb.nodes))
        self.assertEqual([('Bern', 'Lausanne'), ('Lausanne', 'Genf'), ('Bern', 'Genf')], gb.edges)

    def test_append_edges(self):
        gb = GraphBuilder()
        gb.append_edges([("Bern", "Lausanne"), ("Lausanne", "Genf")])
        self.assertEqual(3, len(gb.nodes))
        self.assertEqual(['Bern', 'Lausanne', 'Genf'], gb.nodes )


    def test_create(self):
        gb = GraphBuilder()
        gb.append_edge(("Bern", "Lausanne"))
        gb.append_edge(("Lausanne", "Genf"))
        graph = gb.create()
        self.assertEqual(3, len(graph.nodes))
        self.assertEqual(2, len(graph.edges))

if __name__ == '__main__':
    unittest.main()
