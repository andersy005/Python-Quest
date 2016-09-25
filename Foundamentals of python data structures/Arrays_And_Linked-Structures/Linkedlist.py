# Defining a Singly Linked Node class

class Node(object):
    """Represents a singly linked node"""

    def __init__(self, data, next= None):
        """Instantiates a Node with a default next of None"""
        self.data = data
        self.next = next


# Using the LinkedList Node class

node1 = None
node2 = Node("A",None)
node3 = Node("B", node2)