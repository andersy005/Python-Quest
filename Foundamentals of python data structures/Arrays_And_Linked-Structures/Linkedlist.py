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

print '*' * 50
# Adding nodes to the a linked list

head = None

for count in range(1,6):
    head = Node(count, head)
    
    
# Print the contents of the structure
def printList(head):

    while head != None:
        print(head.data)
        head = head.next
printList(head)

print '*' * 50



# Replacement
def replace(head, targetItem, newItem):
    current = head

    while current != None and targetItem != current.data:
        current = current.next

    if current != None:
        current.data = newItem
        return True

    else:
        return False

replace(head,5, 10)
printList(head)

