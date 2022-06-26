import pandas as pd


d1 = {
    "graphs": 100,
    "nodes" : 603,
    "edges" : 902,
    "possible edges": 200,
    "cpu": 8.35,
    "memory": 698295.0,
    "time": 0.06,
}

d2 = {
    "graphs": 200,
    "nodes" : 1603,
    "edges" : 1902,
    "possible edges": 400,
    "cpu": 16.35,
    "memory": 698295.0,
    "time": 1.40,
}

"""
d = {
    "Network A": d1.values(),
    "Network A": d2.values()
}

index = list(d1.keys())
print(type(index))
print(index)

index = list(map(lambda s: s.capitalize(), index))
print(type(index))
print(index)


df = pd.DataFrame(data=d, index=index)
"""


def create_df(measures, labels):
    """Creates a pandas data frame from a list of measures. Each measure is a dictionary with the measure as key
    and the value. The keys are used as index labels. The values of a dict are the column values. The labels parameter
    is used as column labels. The order of the measuers must be aligned with the order of the labels.
    """
    # create dict as base for the data frame
    d = {}
    for label, measure in zip(labels, measures):
        d[label] = measure.values()
    # use measure dict keys as index
    index = list(measures[0].keys())
    index = list(map(lambda s: s.capitalize(), index))
    # create and return result
    return pd.DataFrame(data=d, index=index)

df = create_df([d1,d2], ["Network A", "Network B"])
print(df)

