import unittest
from gml.graph.graph_builder import GraphBuilder
from gml.graph.graph import Graph

class GraphTest(unittest.TestCase):

    def test_weighted(self):
        graph = GraphBuilder().append_edges([('A', 'B'), ('B', 'C'), ('C','D')]).create()
        self.assertEqual(False, graph.weighted)
        graph = GraphBuilder().append_edges([('A', 'B', 4), ('B', 'C', 2), ('C','D', 8)]).create()
        self.assertEqual(True, graph.weighted)

    def test_detect_multi(self):
        graph = GraphBuilder().append_edges([('A', 'B'), ('B', 'C'), ('C','D')]).create()
        self.assertEqual(False, graph.multi)
        graph = GraphBuilder().append_edges([('A', 'B'), ('B', 'C'), ('C','D'), ('A', 'B')]).create()
        self.assertEqual(True, graph.multi)
        graph = GraphBuilder().append_edges([('A', 'B'), ('B', 'C'), ('C','D'), ('B', 'A')]).create()
        self.assertEqual(True, graph.multi)


if __name__ == '__main__':
    unittest.main()
