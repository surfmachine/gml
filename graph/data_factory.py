"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

import random
import numpy as np
from .graph_builder import GraphBuilder

# ---------------------------------------------------------------------------------------------------------------------
# Test data entities
# ---------------------------------------------------------------------------------------------------------------------

class GraphRoot:
    """Common root node for the entire test graph."""
    NAME = "GR"
    def __init__(self):
        """Create instance."""
        self.name = GraphRoot.NAME

class OrgRoot:
    """Organisation root node data class."""
    NAME = "OR"
    def __init__(self):
        """Create instance."""
        self.name = OrgRoot.NAME

class Employee:
    """Employee test data class.
     The test data class can return an employee object with the following edges sceanrios. Further more each edge can
     be eighter weighted or unweighted:
     - edges from the employee to its childs (the id, firstname and lastname) or only a part of them
     - edges from the employee to its childes and from the childs to another node
     - edges from the employee to its childes and from the employee to another node
     - edges from the employee to its childes and from the childs to another node and the employee to another node
    """
    NAME_PREFIX = "EM"
    ID_PREFIX = "I"
    FIRSTNAME_PREFIX = "F"
    LASTNAME_PREFIX = "L"
    TYPE_POSTFIX = "Type"

    def __init__(self, i, add_id=True, add_fn=True, add_ln=True, add_type_nodes=False,
                 weighted=False, weight_id=1.0, weight_fn=0.5, weight_ln=0.5, weight_type_nodes=1.0):
        """Create test data employee instance."""
        # employee node
        self.name = Employee.NAME_PREFIX + str(i)
        # employee child nodes
        self.id = Employee.ID_PREFIX + str(i) if add_id else None
        self.fn = Employee.FIRSTNAME_PREFIX + str(i) if add_fn else None
        self.ln = Employee.LASTNAME_PREFIX + str(i) if add_ln else None
        # embed type node between employee and child nodes
        self.add_type_nodes = add_type_nodes
        # optional weitgts for the edges
        self.weighted = weighted
        self.weight_id = weight_id
        self.weight_fn = weight_fn
        self.weight_ln = weight_ln
        self.weight_type_nodes = weight_type_nodes
        # type nodes
        self.id_type_node = Employee.ID_PREFIX + Employee.TYPE_POSTFIX
        self.fn_type_node = Employee.FIRSTNAME_PREFIX + Employee.TYPE_POSTFIX
        self.ln_type_node = Employee.LASTNAME_PREFIX + Employee.TYPE_POSTFIX

    @staticmethod
    def create_name(i):
        return Employee.NAME_PREFIX + str(i)

    def edges(self):
        return self.connect_to_childs(self.name, self.add_type_nodes)

    def edges_connected(self, to_parent, to_childs, weight_to_parent=1.0):
        result = self.edges_connected_to_parent(to_parent, weight=weight_to_parent)
        child_connections = self.connect_to_childs(to_childs)
        result.extend(child_connections)
        return result

    def edges_connected_to_parent(self, to_parent, weight=1.0):
        result = self.edges()
        result.append(self.create_edge(self.name, to_parent, weight))
        return result

    def edges_connected_to_childs(self, to_childs):
        result = self.edges()
        child_connections = self.connect_to_childs(to_childs)
        result.extend(child_connections)
        return result

    def connect_to_childs(self, to, add_type_nodes=False):
        edges= []
        if self.id:
            if add_type_nodes:
                edges.append(self.create_edge(to, self.id_type_node, self.weight_type_nodes))
                edges.append(self.create_edge(self.id_type_node, self.id, self.weight_id))
            else:
                edges.append(self.create_edge(to, self.id, self.weight_id))
        if self.fn:
            if add_type_nodes:
                edges.append(self.create_edge(to, self.fn_type_node, self.weight_type_nodes))
                edges.append(self.create_edge(self.fn_type_node, self.fn, self.weight_fn))
            else:
                edges.append(self.create_edge(to, self.fn, self.weight_fn))
        if self.ln:
            if add_type_nodes:
                edges.append(self.create_edge(to, self.ln_type_node, self.weight_type_nodes))
                edges.append(self.create_edge(self.ln_type_node, self.ln, self.weight_ln))
            else:
                edges.append(self.create_edge(to, self.ln, self.weight_ln))
        return edges

    def create_edge(self, from_node, to_node, weight=None):
        if self.weighted:
            return (from_node, to_node, weight)
        else:
            return (from_node, to_node)


class DoubleEmployee(Employee):
    """Create an two employee's with the same first and/or lastname. One of the employee's may also have an id """

    DOUBLE_NAME_POSTFIX = "x"

    def __init__(self, i, add_id=True):
        super().__init__(i, add_id=add_id, add_fn=True, add_ln=True)
        self.double_name = self.name + DoubleEmployee.DOUBLE_NAME_POSTFIX

    def edges(self):
        result =  self.connect_to_childs(self.name)
        result.append( self.create_edge(self.double_name, self.fn) )
        result.append( self.create_edge(self.double_name, self.ln) )
        return result

class DataRoot:
    """Data root test data class."""
    NAME = "DR"
    def __init__(self):
        """Create instance."""
        self.name = DataRoot.NAME


class DataCollection:
    """Data collection test data class."""
    NAME_PREFIX = "DC"
    def __init__(self, i):
        """Create instance."""
        self.name = DataCollection.NAME_PREFIX + str(i)

    @staticmethod
    def create_name(i):
        return DataCollection.NAME_PREFIX + str(i)


class MatchingCluster:
    """MatchingCluster test data class."""
    NAME_PREFIX = "MC"
    def __init__(self, i):
        """Create instance."""
        self.name = MatchingCluster.NAME_PREFIX + str(i)

    @staticmethod
    def create_name(i):
        return MatchingCluster.NAME_PREFIX + str(i)


class Direction:
    """Direction test data class."""
    NAME_PREFIX = "DIR"
    def __init__(self):
        """Create instance."""
        self.name = Direction.NAME_PREFIX

class GeneralAgency:
    """General agency test data class."""
    NAME_PREFIX = "GA"
    def __init__(self):
        """Create instance."""
        self.name = GeneralAgency.NAME_PREFIX



# ---------------------------------------------------------------------------------------------------------------------
# Test data factory
# ------------------------------------f---------------------------------------------------------------------------------

class DataFactory:
    """Synthetic test data factory.

    Abbreviations of the node names:
    - GR: Graph root (used for connected graphs)
    - DR: Data root (used for connected graphs)
    - OR: Organisation root (used for connected graphs)
    - DC: Data Collection (Datensammlung)
    - MC: Matching Cluster
    - EM: Employee (Mitarbeiter)
    - A:  Atomic Value
    - I:  Atomic Value for an Identiy of an Employee (U-Nummer)
    - F:  Atomic Value for a Firstname of an Employee
    - L:  Atomic Value for a Lastname of an Employee

    Abbreviations of the type node names:
    - IType: Identiy Type
    - FType: Firstname Type
    - LType: Lastname Type
    """

    def __init__(self):
        """Create new data factory builder instance."""
        pass

    def create_names(self, name, n=10):
        """Create a list of n names with the name and number."""
        return [name + str(i) for i in range(0, n)]

    def create_graph(self, n=1, connected=False, directed=False, add_dc=False,
                     add_id=True, add_fn=True, add_ln=True, typed=False, weighted=False):
        """Create n single graphs with MC/DC on one site and EM on the other side.

        If the connected option is enabled, the n single graphs with MC/DC on one site and EM on the other side  will
        get a root on each side. All MC/DC nodes share a common parent and all EM nodes as well. These two parents
        will then be connected as well. So all together one single graph will be created!
        """
        # init graph builder
        graph_builder = GraphBuilder()
        # init root elements for connected graph
        if connected:
            graph_root = GraphRoot()
            org_root = OrgRoot()
            data_root = DataRoot()
            graph_builder.append_edge((graph_root.name, org_root.name))
            graph_builder.append_edge((graph_root.name, data_root.name))
        # create n subgraphs
        for i in range(0, n):
            # create em and mc
            em = Employee(i, add_id=add_id, add_fn=add_fn, add_ln=add_ln, add_type_nodes=typed, weighted=weighted)
            mc = MatchingCluster(i)
            edges = em.edges_connected_to_childs(mc.name)
            # add data cluster (if enabled)
            if add_dc:
                dc = DataCollection(i)
                edges.append((dc.name, mc.name))
            # add root nodes (if enabled)
            if connected:
                edges.append((org_root.name, em.name))
                if add_dc:
                    edges.append((data_root.name, dc.name))
                else:
                    edges.append((data_root.name, mc.name))
            # add edges
            graph_builder.append_edges(edges)
        # create graph and return result
        if directed:
            return graph_builder.create_directed()
        return graph_builder.create()

    def create_edges_with_doubles(self, n=1, add_id=True, add_dc=False, add_org=True):
        """Create edges for n single graphs with MC/DC on one site and EM on the other side.

        If the connected option is enabled, the n single graphs with MC/DC on one site and EM on the other side  will
        get a root on each side. All MC/DC nodes share a common parent and all EM nodes as well. These two parents
        will then be connected as well. So all together one single graph will be created!
        """
        result = []
        # init direction and general agency
        dir = Direction()
        ga = GeneralAgency()
        # create n subgraph edges
        for i in range(0, n):
            em = DoubleEmployee(i, add_id)
            mc = MatchingCluster(i)
            edges = em.edges_connected_to_childs(mc.name)
            # add connections to direction and agency
            if add_org:
                edges.append((dir.name, em.name))
                edges.append((dir.name, mc.name))
                edges.append((ga.name, em.double_name))
            # add data cluster (if enabled)
            if add_dc:
                dc = DataCollection(i)
                edges.append((dc.name, mc.name))
                if add_org:
                    edges.append((dir.name, dc.name))
            result.extend(edges)
        # return result
        return result

    def create_graph_with_doubles(self, n=1, add_id=True, add_dc=False, add_org=True):
        """Create n single graphs with MC/DC on one site and EM on the other side.

        If the connected option is enabled, the n single graphs with MC/DC on one site and EM on the other side  will
        get a root on each side. All MC/DC nodes share a common parent and all EM nodes as well. These two parents
        will then be connected as well. So all together one single graph will be created!
        """
        edges = self.create_edges_with_doubles(n=n, add_id=add_id, add_dc=add_dc, add_org=add_org)
        return GraphBuilder().append_edges(edges).create()

# ---------------------------------------------------------------------------------------------------------------------
# Edge label factory
# ------------------------------------f---------------------------------------------------------------------------------

class EdgeLabelFactory:
    """Create possible edges and the corresponding labels."""

    def pick(self, n, p=1):
        """Pick percent p numbers of n numbers from range 0 to n-1."""
        result = set()
        size = int(n*p)
        while len(result) < size:
            i = np.random.randint(0, n)
            result.add(i)
        return result

    def pick_to_n(self, from_n, n):
        """Pich a number from range 0 to n-1, not even to the given from_n."""
        to_n = np.random.randint(0,n)
        while from_n == to_n:
            to_n = np.random.randint(0,n)
        return to_n

    def sample_positive(self, from_name, to_name, n, p=1):
        """Create percent p possible edges of n from range 0 to n-1 together with positive labels."""
        result = []
        swap = False
        for i in self.pick(n,p):
            s = str(i)
            f = from_name + s
            t = to_name + s
            if swap:
                result.append((t,f))
            else:
                result.append((f,t))
            swap = not swap
        return result

    def sample_negative(self, from_name, to_name, n, p=1):
        """Create percent p possible edges of n from range 0 to n-1 together with negative labels."""
        result = []
        swap = False
        for i in self.pick(n,p):
            j = self.pick_to_n(i,n)
            f = from_name + str(i)
            t = to_name + str(j)
            if swap:
                result.append((t,f))
            else:
                result.append((f,t))
            swap = not swap
        return result

    def sample(self, from_name, to_name, n, p=1, shuffle=True):
        """Create percent p edges of n from range 0 to n-1. Half of them with positive lables, the other half with
        negative labels. together with negative labels. The edges and labels are shuffeld per default.
        """
        edges = []
        labels= []
        ps = self.sample_positive(from_name, to_name, n, p/2.0)
        ns = self.sample_negative(from_name, to_name, n, p/2.0)
        edges.extend(ps)
        labels.extend( [1] * len(ps) )
        edges.extend(ns)
        labels.extend( [0] * len(ns) )
        if shuffle:
            return self.shuffle(edges,labels)
        return edges, labels

    def shuffle(self, edges, labels):
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

    def edge_splitter(self, from_name, to_name, all_edges, p=0.1, shuffle=True):
        """Split percent p edges from the original list of all_edges and return the new edge list, together with
        p percent positive and negative samples and labels.
        """
        # init
        n = len(all_edges)
        picks = self.pick(n, p=p)
        edges = []
        pos_samples = []
        # create edges and positive edge samples
        for i in range(n):
            if i in picks:
                pos_samples.append(all_edges[i])
            else:
                edges.append(all_edges[i])
        # create negative edge samples
        neg_samples = self.sample_negative(from_name, to_name, n, p=p)
        # create labels
        pos_labels = [1 for _ in range(len(pos_samples))]
        neg_labels = [0 for _ in range(len(neg_samples))]
        # combine and shuffle samples
        samples = pos_samples
        samples.extend(neg_samples)
        labels = pos_labels
        labels.extend(neg_labels)
        if shuffle:
            samples, labels = self.shuffle(samples, labels)
        # return all edges, sample edges and sample labels
        return edges, samples, labels

# ---------------------------------------------------------------------------------------------------------------------
# Edge label factory
# ------------------------------------f---------------------------------------------------------------------------------

class TestTrainDataFactory():
    """Create complete graphs including test- and train graphs with samples and labels. The class assembles the
    capabilities of the TestDataFactory and EdgeLabelFactory to generate all needed data sets for some experiments.
    """
    def __init__(self):
        self.df = DataFactory()
        self.ef = EdgeLabelFactory()

    def create_testdata(self, n, from_node="EM", to_node="DC", p=0.5, shuffle=True,
                        add_id=False, add_dc=True, add_predict_edges=True, add_org=True):

        # create fully linked graph
        base_edges = self.df.create_edges_with_doubles(n=n, add_id=add_id, add_dc=add_dc,
                                                       add_org=add_org)         # graph edges without predict edges
        link_edges = self.ef.sample_positive(from_node, to_node, n, p=1)        # graph predict edges (positive)
        if add_predict_edges:
            graph = GraphBuilder().append_edges(base_edges).append_edges(link_edges).create()
        else:
            graph = GraphBuilder().append_edges(base_edges).create()

        # create test data
        test_edges, test_samples, test_labels = self.ef.edge_splitter(from_node, to_node, link_edges, p=p, shuffle=shuffle)
        if add_predict_edges:
            test_graph = GraphBuilder().append_edges(base_edges).append_edges(test_edges).create()
        else:
            test_graph = GraphBuilder().append_edges(base_edges).create()

        # create train data
        train_edges, train_samples, train_labels = self.ef.edge_splitter(from_node, to_node, test_edges, p=p, shuffle=shuffle)
        if add_predict_edges:
            train_graph = GraphBuilder().append_edges(base_edges).append_edges(train_edges).create()
        else:
            train_graph = GraphBuilder().append_edges(base_edges).create()

        # return results
        return graph, test_graph, test_samples, test_labels, train_graph, train_samples, train_labels





# ---------------------------------------------------------------------------------------------------------------------
# The end.