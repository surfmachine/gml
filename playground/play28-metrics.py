import random
import numpy as np
from gml.graph.graph_metrics import GraphMetrics

labels = [1,1,1,1,1,1,1,1,1,1]
y_pred = [0,0,0,0,0,1,1,1,1,1]


gm = GraphMetrics()
gm.print_metrics(labels, y_pred)
