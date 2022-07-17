import random
import numpy as np
from gml.graph.data_factory import EdgeLabelFactory

def pick(n, p=1):
    """Pick percent p numbers of n numbers from range 0 to n-1."""
    result = set()
    size = int(n*p)
    while len(result) < size:
        i = np.random.randint(0, n)
        result.add(i)
    return result

def pick_to_n(from_n, n):
    to_n = np.random.randint(0,n)
    while from_n == to_n:
        to_n = np.random.randint(0,n)
    return to_n

def sample_positive(from_name, to_name, n, p=1):
    result = []
    swap = False
    for i in pick(n,p):
        s = str(i)
        f = from_name + s
        t = to_name + s
        if swap:
            result.append((t,f))
        else:
            result.append((f,t))
        swap = not swap
    return result

def sample_negative(from_name, to_name, n, p=1):
    """Pick percent p number pairs of n from range 0 to n-1, where each pair has uneven numbers."""
    result = []
    swap = False
    for i in pick(n,p):
        j = pick_to_n(i,n)
        f = from_name + str(i)
        t = to_name + str(j)
        if swap:
            result.append((t,f))
        else:
            result.append((f,t))
        swap = not swap
    return result

def sample(from_name, to_name, n, p=1):
    edges = []
    labels= []
    ps = sample_positive(from_name, to_name, n, p/2.0)
    ns = sample_negative(from_name, to_name, n, p/2.0)
    edges.extend(ps)
    labels.extend( [1] * len(ps) )
    edges.extend(ns)
    labels.extend( [0] * len(ns) )
    return edges, labels

def shuffle(edges, labels):
    # combine edges and labels and shuffle
    l = []
    for edge, label in zip(edges, labels):
        l.append((edge, label))
    random.shuffle(l)
    # extract edges and labels
    res_edges = []
    res_labels= []
    for t in l:
        res_edges.append(t[0])
        res_labels.append(t[1])
    return res_edges, res_labels


edges, labels = sample("EM", "MC", 100, 0.1)
print(edges)
print(labels)

edges, labels = shuffle(edges, labels)
print(edges)
print(labels)

print("------------")

elf = EdgeLabelFactory()

edges, labels = elf.sample("EM", "MC", 100, p=0.1, shuffle=False)
print(edges)
print(labels)

edges, labels = elf.shuffle(edges, labels)
print(edges)
print(labels)


print("------------")

edges, labels = elf.sample("EM", "MC", 100, p=0.1)
print(edges)
print(labels)

