from gml.graph.graph_viz import GraphViz
from gml.graph.data_factory import DataFactory, EdgeLabelFactory

elf = EdgeLabelFactory()

n = 20

# edges, labels = elf.sample("EM", "DC", n, p=1, shuffle=False)
# print(edges)
# print(labels)

#
# Create all positive edges
#
all_edges = elf.sample_positive("EM", "DC", n, p=1)
print("All positive edges:")
print(all_edges)

#
# Prepare test data
#
l = len(all_edges)
test_edges   = []
test_samples = []
test_labels  = []
picks = elf.pick(l, p=0.1)
for i in range(l):
    if i in picks:
        test_samples.append(all_edges[i])
        test_labels.append(1)
    else:
        test_edges.append(all_edges[i])

test_samples_n = elf.sample_negative("EM", "DC", l, p=0.1)
test_labels_n  = [0 for i in range(len(test_samples_n))]

print("Test data (positive edges):")
print(test_edges)
print(test_samples)
print(test_labels)
print(test_samples_n)
print(test_labels_n)

#
# Prepare train data
#
l = len(test_edges)
train_edges   = []
train_samples = []
train_labels  = []
picks = elf.pick(l, p=0.1)
for i in range(l):
    if i in picks:
        train_samples.append(test_edges[i])
        train_labels.append(1)
    else:
        train_edges.append(test_edges[i])

train_samples_n = elf.sample_negative("EM", "DC", l, p=0.1)
train_labels_n  = [0 for i in range(len(train_samples_n))]


print("Train data (positive edges):")
print(train_edges)
print(train_samples)
print(train_labels)
print(train_samples_n)
print(train_labels_n)


print("#")
print("# edge_splitter")
print("#")

def edge_splitter(from_name, to_name, all_edges, p=0.1, shuffle=True):
    # init
    n = len(all_edges)
    picks = elf.pick(n, p=p)
    edges = []
    pos_samples = []
    # create edges and positive edge samples
    for i in range(n):
        if i in picks:
            pos_samples.append(all_edges[i])
        else:
            edges.append(all_edges[i])
    # create negative edge samples
    neg_samples = elf.sample_negative(from_name, to_name, n, p=p)
    # create labels
    pos_labels = [1 for _ in range(len(pos_samples))]
    neg_labels = [0 for _ in range(len(neg_samples))]
    # combine and shuffle samples
    samples = pos_samples
    samples.extend(neg_samples)
    labels = pos_labels
    labels.extend(neg_labels)
    if shuffle:
        samples, labels = elf.shuffle(samples, labels)
    # return all edges, sample edges and sample labels
    return edges, samples, labels

all_edges = elf.sample_positive("EM", "DC", n, p=1)
print("All positive edges:")
print(all_edges)

test_edges, test_samples, test_labels = edge_splitter("EM", "DC", all_edges, p=0.1, shuffle=False)
print("Test data:")
print(test_edges)
print(test_samples)
print(test_labels)

train_edges, train_samples, train_labels = edge_splitter("EM", "DC", test_edges, p=0.1, shuffle=False)
print("Train data:")
print(train_edges)
print(train_samples)
print(train_labels)






# graph = DataFactory().create_graph_with_doubles(n=1, add_dc=True)
# graph.draw(layout=GraphViz.SPIRAL_LAYOUT)
#
# graph = DataFactory().create_graph_with_doubles(n=1, add_id=False, add_dc=True)
# graph.draw(layout=GraphViz.SPIRAL_LAYOUT)



