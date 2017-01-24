import customexceptions
from models import Graph
import os
from argparse import ArgumentParser    # Class used for handling command line arguments

if __name__ == "__main__":
    # User can pass arguments from the command line.
    # if none are passed, default values will be used.

    arg_parser = ArgumentParser()
    arg_parser.add_argument("-p", action="store", dest="path",
                            help="path to the network file.", default="SocialNetwork.txt")
    arg_parser.add_argument("-a", action="store", dest="a_value",
                            help="A value.", default="STACEY_STRIMPLE")
    arg_parser.add_argument("-b", action="store", dest="b_value",
                            help="B value.", default="RICH_OMLI")

    args = arg_parser.parse_args()

    try:
        if os.path.isfile(args.path):
            graph = Graph()

            # Parse file, and build the graph
            with open(args.path, "r") as file:
                for line in file:
                    first, second = line.rstrip().split(",")
                    graph.add_edge(first, second)


            # Calculate the distance between the nodes
            distance = graph.calculate_distance(args.a_value, args.b_value)
            print "No of nodes: %d" % (len(graph))
            print "Distance between '%s' and '%s': %d" % (args.a_value, args.b_value, distance)

        else:
            print "File %s does not exist." % (args.path)

    except customexceptions.NodeNotFoundException as e:
        print "Node '%s' was not found on the graph." % (e.node_name)

    except customexceptions.NoLinkBetweenNodesException as e:
        print "There is no connection between nodes '%s' and '%s'" % (e.node_a_name, e.node_b_name)

    except ValueError:
        print "Incorrect file format."
