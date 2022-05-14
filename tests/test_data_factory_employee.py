import unittest
from gml.graph.data_factory import Employee


class EmployeeTest(unittest.TestCase):

    def test_edges(self):
        expected_edges = [('EM7', 'I7'), ('EM7', 'F7'), ('EM7', 'L7')]
        emp = Employee(7)
        self.assertEqual(emp.edges(), expected_edges)

    def test_edges_connected_to_parent(self):
        expected_edges = [('EM7', 'I7'), ('EM7', 'F7'), ('EM7', 'L7'), ('EM7', 'Agency')]
        emp = Employee(7)
        self.assertEqual(emp.edges_connected_to_parent('Agency'), expected_edges)

    def test_edges_connected_to_childs(self):
        expected_edges = [('EM7', 'I7'), ('EM7', 'F7'), ('EM7', 'L7'), ('DC', 'I7'), ('DC', 'F7'), ('DC', 'L7')]
        emp = Employee(7)
        self.assertEqual(emp.edges_connected_to_childs('DC'), expected_edges)

    def test_edges_connected(self):
        expected_edges = [('EM7', 'I7'), ('EM7', 'F7'), ('EM7', 'L7'), ('EM7', 'Agency'), ('DC', 'I7'), ('DC', 'F7'), ('DC', 'L7')]
        emp = Employee(7)
        self.assertEqual(emp.edges_connected('Agency', 'DC'), expected_edges)

    #
    # test type nodes
    #
    def test_edges_with_typed(self):
        expected_edges = [('EM7', 'IType'), ('IType', 'I7'), ('EM7', 'FType'), ('FType', 'F7'), ('EM7', 'LType'), ('LType', 'L7')]
        emp = Employee(7, add_type_nodes=True)
        self.assertEqual(emp.edges(), expected_edges)

    def test_edges_connected_to_parent_typed(self):
        expected_edges = [('EM7', 'IType'), ('IType', 'I7'), ('EM7', 'FType'), ('FType', 'F7'), ('EM7', 'LType'), ('LType', 'L7'), ('EM7', 'Agency')]
        emp = Employee(7, add_type_nodes=True)
        self.assertEqual(emp.edges_connected_to_parent('Agency'), expected_edges)

    def test_edges_connected_to_childs_typed(self):
        expected_edges = [('EM7', 'IType'), ('IType', 'I7'), ('EM7', 'FType'), ('FType', 'F7'), ('EM7', 'LType'), ('LType', 'L7'), ('DC', 'I7'), ('DC', 'F7'), ('DC', 'L7')]
        emp = Employee(7, add_type_nodes=True)
        res = emp.edges_connected_to_childs('DC')
        self.assertEqual(emp.edges_connected_to_childs('DC'), expected_edges)

    def test_edges_connected_typed(self):
        expected_edges = [('EM7', 'IType'), ('IType', 'I7'), ('EM7', 'FType'), ('FType', 'F7'), ('EM7', 'LType'), ('LType', 'L7'), ('EM7', 'Agency'), ('DC', 'I7'), ('DC', 'F7'), ('DC', 'L7')]
        emp = Employee(7, add_type_nodes=True)
        self.assertEqual(emp.edges_connected('Agency', 'DC'), expected_edges)

    #
    # test weighted
    #
    def test_edges_weighted(self):
        expected_edges = [('EM7', 'I7', 1.0), ('EM7', 'F7', 0.5), ('EM7', 'L7', 0.5)]
        emp = Employee(7, weighted=True)
        self.assertEqual(emp.edges(), expected_edges)

    def test_edges_connected_to_parent_weighted(self):
        expected_edges = [('EM7', 'I7', 1.0), ('EM7', 'F7', 0.5), ('EM7', 'L7', 0.5), ('EM7', 'Agency', 1.0)]
        emp = Employee(7, weighted=True)
        self.assertEqual(emp.edges_connected_to_parent('Agency'), expected_edges)

    def test_edges_connected_to_parent_weighted_custom(self):
        expected_edges = [('EM7', 'I7', 0.9), ('EM7', 'F7', 0.5), ('EM7', 'L7', 0.7), ('EM7', 'Agency', 0.66)]
        emp = Employee(7, weighted=True, weight_id=0.9, weight_ln=0.7, weight_fn=0.5)
        self.assertEqual(emp.edges_connected_to_parent('Agency', weight=0.66), expected_edges)

    def test_edges_connected_to_childs_weighted(self):
        expected_edges = [('EM7', 'I7', 1.0), ('EM7', 'F7', 0.5), ('EM7', 'L7', 0.5), ('DC', 'I7', 1.0), ('DC', 'F7', 0.5), ('DC', 'L7', 0.5)]
        emp = Employee(7, weighted=True)
        self.assertEqual(emp.edges_connected_to_childs('DC'), expected_edges)

    def test_edges_connected_weighted(self):
        expected_edges = [('EM7', 'I7', 1.0), ('EM7', 'F7', 0.5), ('EM7', 'L7', 0.5), ('EM7', 'Agency', 1.0), ('DC', 'I7', 1.0), ('DC', 'F7', 0.5), ('DC', 'L7', 0.5), ]
        emp = Employee(7, weighted=True)
        self.assertEqual(emp.edges_connected('Agency', 'DC'), expected_edges)

    def test_edges_connected_weighted_custom(self):
        expected_edges = [('EM7', 'I7', 1.0), ('EM7', 'F7', 0.5), ('EM7', 'L7', 0.5), ('EM7', 'Agency', 0.8), ('DC', 'I7', 1.0), ('DC', 'F7', 0.5), ('DC', 'L7', 0.5), ]
        emp = Employee(7, weighted=True)
        self.assertEqual(emp.edges_connected('Agency', 'DC', weight_to_parent=0.8), expected_edges)

if __name__ == '__main__':
    unittest.main()
