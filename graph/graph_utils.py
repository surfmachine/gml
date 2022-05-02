"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

class GraphUtils:
    """Utility class with some helper methods used within the graph modules."""

    @staticmethod
    def combinations(nodes):
        """Return all node combinations as list of tuples for the given nodes.  Each tuple contains the source and
        target node name. Sample tuple: ('Genf', 'Lausanne')
        """
        combinations = []
        i = 0
        j = i + 1
        while i < len(nodes):
            # print(graph.nodes[i])
            while j < len(nodes):
                combinations.append( (nodes[i], nodes[j]) )
                j = j + 1
            i += 1
            j = i + 1
        return combinations

    @staticmethod
    def zip_dicts(*dicts):
        """ZIP n dictionaries to a list with the key as first entry followed by the values of each dict."""
        result = []
        for key in dicts[0].keys():
            entries = [key]
            for dict in dicts:
                entries.append(dict[key])
            result.append(entries)
        return result


