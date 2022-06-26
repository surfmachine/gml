"""Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten"""

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
        # otional weitgts for the edges
        self.weighted = weighted
        self.weight_id = weight_id
        self.weight_fn = weight_fn
        self.weight_ln = weight_ln
        self.weight_type_nodes = weight_type_nodes

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
                type_node = Employee.ID_PREFIX + Employee.TYPE_POSTFIX
                edges.append(self.create_edge(to, type_node, self.weight_type_nodes))
                edges.append(self.create_edge(type_node, self.id, self.weight_id))
            else:
                edges.append(self.create_edge(to, self.id, self.weight_id))
        if self.fn:
            if add_type_nodes:
                type_node = Employee.FIRSTNAME_PREFIX + Employee.TYPE_POSTFIX
                edges.append(self.create_edge(to, type_node, self.weight_type_nodes))
                edges.append(self.create_edge(type_node, self.fn, self.weight_fn))
            else:
                edges.append(self.create_edge(to, self.fn, self.weight_fn))
        if self.ln:
            if add_type_nodes:
                type_node = Employee.LASTNAME_PREFIX + Employee.TYPE_POSTFIX
                edges.append(self.create_edge(to, type_node, self.weight_type_nodes))
                edges.append(self.create_edge(type_node, self.ln, self.weight_ln))
            else:
                edges.append(self.create_edge(to, self.ln, self.weight_ln))
        return edges

    def create_edge(self, from_node, to_node, weight=None):
        if self.weighted:
            return (from_node, to_node, weight)
        else:
            return (from_node, to_node)


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

    def create_names(self, name, n=10):
        """Create a list of n names with the name and number."""
        return [name + str(i) for i in range(0, n)]

# ---------------------------------------------------------------------------------------------------------------------
# The end.