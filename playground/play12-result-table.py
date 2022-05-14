import pandas as pd

print("#")
print("# Combine experiment results as pandas dataframe")
print("#")

# DataFrame sample
data = pd.DataFrame({
    'Edge': [('A','B'), ('A','C'), ('B','C'), ('B','D'), ('C','D')],
    'RA': [1, 2, 3, 4, 5],
    'JC': [6, 7, 8, 9, 10]
})

print(data)

# Resource Allocation
ra = [('PL', 'D1', 1.5), ('PL', 'D2', 0), ('PL', 'D3', 0), ('ZI', 'D1', 0), ('ZI', 'D2', 1.0), ('ZI', 'D3', 0), ('JK', 'D1', 0), ('JK', 'D2', 0), ('JK', 'D3', 0.5)]

# Jaccard Coefficient
jc = [('PL', 'D1', 1.0), ('PL', 'D2', 0.0), ('PL', 'D3', 0.0), ('ZI', 'D1', 0.0), ('ZI', 'D2', 1.0), ('ZI', 'D3', 0.0), ('JK', 'D1', 0.0), ('JK', 'D2', 0.0), ('JK', 'D3', 0.5)]

res = {
    'Edge': [],
    'RA': [],
    'JC': []
}

for i in range(len(ra)):
    res["Edge"].append( (ra[i][0], ra[i][1]) )
    res["RA"].append( ra[i][2] )
    res["JC"].append(jc[i][2])

res_df = pd.DataFrame(res)
print(res_df)

print("#")
print("# assemble_link_predictions")
print("#")


def assemble_link_predictions(labels, perdictions, edge_label="Edge"):
    """
    Convert single link perdictions into a pandas data frame.

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

res_df = assemble_link_predictions(["Resource Allocation", "Jaccard Coefficient"],[ra, jc])
print(res_df)



