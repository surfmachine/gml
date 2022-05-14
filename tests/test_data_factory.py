import unittest
from gml.graph.data_factory import DataFactory


class DataFactoryTest(unittest.TestCase):


    def test_create_names(self):
        names = DataFactory().create_names("T")
        self.assertEqual(len(names), 10)
        self.assertEqual(names[0], "T0")
        self.assertEqual(names[9], "T9")


if __name__ == '__main__':
    unittest.main()
