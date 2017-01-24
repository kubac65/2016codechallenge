class NodeNotFoundException(Exception):
    """
    Exception thrown when node can not be found on the graph.
    """

    def __init__(self, node_name):
        super(NodeNotFoundException, self)
        self.node_name = node_name


class NoLinkBetweenNodesException(Exception):
    """
    Exception thrown when there is no connection between two nodes.
    """

    def __init__(self, node_a_name, node_b_name):
        super(NoLinkBetweenNodesException, self)
        self.node_a_name = node_a_name
        self.node_b_name = node_b_name