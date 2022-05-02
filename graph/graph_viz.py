"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

import networkx as nx
import matplotlib.pyplot as plt

class GraphViz:
    """Graph visualization class. Currently the visualizations are based of the networkx graph framework.

    References:
    - https://networkx.org
    """

    STYLES = {
        'node_size': 60,
        'node_color': 'red',
        'edge_color': 'black',
        'arrowsize': 18,
        'with_labels': False,
        'ax': None
    }

    SCATTER_STYLES = {
    }

    @staticmethod
    def get_styles():
        """Get a copy of the default styles. Used to override some given defaults."""
        return GraphViz.STYLES.copy()

    @staticmethod
    def draw(graph, layout_func=nx.shell_layout, with_labels=True, multi=False, weighted=False, path=[],
             figsize=(6, 6), styles=STYLES):
        """Draw a networkx graph with the given settings."""
        #
        # init plot
        #
        plt.figure(figsize=figsize)
        plt.axis('off')
        #
        # draw network
        #
        node_pos = layout_func(graph)
        edgelist = [] if multi else graph.edges # skip edges for multi mode and draw them with rad
        nx.draw_networkx(graph, pos=node_pos, edgelist=edgelist, **styles)
        #
        # draw edges with rad (in multi mode)
        #
        rad = 0.0
        if multi:
            rad = 0.0
            for edge in graph.edges(data=True):
                rad = rad + 0.05
                nx.draw_networkx_edges(graph, node_pos, edgelist=[(edge[0],edge[1])], connectionstyle=f'arc3, rad={rad}')
        #
        # draw path (colorize with red)
        #
        rad = 0.0
        for edge in graph.edges(data=True):
            rad = rad + 0.05
            n1, n2 = edge[0], edge[1]
            if n1 in path and n2 in path:
                if multi:
                    nx.draw_networkx_edges(graph, node_pos, edgelist=[(edge[0],edge[1])], edge_color='red', connectionstyle=f'arc3, rad={rad}')
                else:
                    nx.draw_networkx_edges(graph, node_pos, edgelist=[(edge[0],edge[1])], edge_color='red')
        #
        # draw node labels
        #
        if with_labels:
            label_coords = {}
            for node, coords in node_pos.items():
                label_coords[node] = (coords[0], coords[1] + 0.1)
            nx.draw_networkx_labels(graph, label_coords, font_family='Arial', font_size=15)
        #
        # draw weights
        #
        if weighted:
            edge_labels=dict([((a,b,),d["weight"]) for a,b,d in graph.edges(data=True)])
            nx.draw_networkx_edge_labels(graph, node_pos, edge_labels=edge_labels)
        #
        # show plot
        #
        plt.show()
