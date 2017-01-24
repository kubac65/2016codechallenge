import customexceptions
from Queue import Queue

class Node(object):
    """
    Represents node/vertex of the graph.
    """

    def __init__(self, name):
        super(Node, self)

        self.name = name
        self.distance = -1
        self.adjacent_nodes = []
        self.parent = None


class Graph(dict):
    """
    Represents the graph.
    """

    def __init__(self):
        super(Graph, self)

    def __get_node__(self, node_name):
        """
        Gets the node from the graph.
        If node doesn't exist on the graph, it will be created.

        :param node_name: Name of the node
        :return: Node from the graph
        """

        if node_name in self:
            node = self[node_name]
        else:
            node = Node(node_name)
            self[node_name] = node

        return node


    def add_edge(self, a_name, b_name):
        """
        Adds the edge to the graph.
        If node doesn't exist on the graph it creates the new one.

        :param a_name: Name of the first node
        :param b_name: Name of the second node
        """

        node_a = self.__get_node__(a_name)
        node_b = self.__get_node__(b_name)

        node_a.adjacent_nodes.append(node_b)
        node_b.adjacent_nodes.append(node_a)


    def calculate_distance(self, a, b):
        """
        Calculates shortest distance between A and B using breadth first search algorithm.

        :param a: Name of the node
        :param b: Name of the node
        :return: Distance between A and B
        """

        if a not in self:
           raise customexceptions.NodeNotFoundException(a)
        elif b not in self:
            raise  customexceptions.NodeNotFoundException(b)

        root = self[a]
        root.distance = 0

        q = Queue()
        q.put(root)

        # Traverse the graph using breadth first search algorithm
        while not q.empty():
            current_node = q.get()

            for node in current_node.adjacent_nodes:
                # Check if node hasn't been visited
                if node.distance == -1:
                    node.distance = current_node.distance + 1
                    node.parent = current_node
                    q.put(node)

        if self[b].distance == -1:
            raise customexceptions.NoLinkBetweenNodesException(a, b)

        return self[b].distance