import customexceptions
from models import Graph, Node
import unittest

class GraphTests(unittest.TestCase):
    def test_get_non_existent_node(self):
        """
        Adds new node to the graph and returns it
        """

        node_name = "TestNode"
        graph = Graph()

        # Check if graph has no nodes
        self.assertEqual(len(graph), 0)
        node = graph.__get_node__(node_name)

        # Check if graph contains new node
        self.assertEqual(len(graph), 1)
        self.assertTrue(node != None)


    def test_get_existent_node(self):
        """
        Returns a node from the graph
        """

        node_name = "TestNode"
        graph = Graph()

        self.assertEqual(len(graph), 0)

        node = Node(node_name)
        graph[node_name] = node
        self.assertEqual(len(graph), 1)

        n = graph.__get_node__(node_name)
        self.assertEqual(node, n)


    def test_add_edge_to_the_graph(self):
        """
        Adds an edge to the graph
        """

        node_a_name = "TestNode1"
        node_b_name = "TestNode2"
        graph = Graph()

        self.assertEqual(len(graph), 0)

        graph.add_edge(node_a_name, node_b_name)

        self.assertEqual(len(graph), 2)

        node_a = graph.__get_node__(node_a_name)
        node_b = graph.__get_node__(node_b_name)

        self.assertTrue(node_a in node_b.adjacent_nodes)
        self.assertTrue(node_b in node_a.adjacent_nodes)


    def test_calculate_shortest_distance(self):
        """
        Calculates the shortest path between 2 nodes
        """

        graph = Graph()

        graph.add_edge("jakub", "john")
        graph.add_edge("jakub", "gerard")
        graph.add_edge("john", "shane")
        graph.add_edge("shane", "lenny")
        graph.add_edge("ciaran", "eoin")

        distance = graph.calculate_distance("jakub", "lenny")

        self.assertEqual(distance, 3)

        # Reset the nodes
        for node in graph.values():
            node.distance = -1
            node.parent = None

        with self.assertRaises(customexceptions.NodeNotFoundException):
            graph.calculate_distance("jakub", "test")

        with self.assertRaises(customexceptions.NoLinkBetweenNodesException):
            graph.calculate_distance("jakub", "ciaran")


if __name__ == "__main__":
    unittest.main()
