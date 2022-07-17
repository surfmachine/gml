"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

import pandas as pd

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

    @staticmethod
    def assemble_link_predictions(labels, perdictions, edge_label="Edge"):
        """
        Merge and convert list of link perdictions into a pandas data frame with the given labels.
        Sample:
            labels = ["Resource Allocation", "Jaccard Coefficient"]
            ra = [('PL', 'D1', 1.5), ('PL', 'D2', 0), ...]
            jc = [('PL', 'D1', 1.0), ('PL', 'D2', 0.0), ...]
            df = assemble_link_predictions(labels, [ra, jc])
        """
        # init result structure
        result = {edge_label: []}
        for label in labels:
            result[label] = []
        # assemble predictions
        first = perdictions[0]
        for i in range(len(first)):
            append_edge = True
            for j in range(len(labels)):
                if append_edge:
                    result[edge_label].append((first[i][0], first[i][1]))
                    append_edge = False
                label = labels[j]
                result[label].append(perdictions[j][i][2])
        # return result as pandas df
        return pd.DataFrame(result)



