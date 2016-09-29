"""Select one list and traverse it while add each node pointer to a dictionary
Traverse the second list to see if any node pointer is also present in the dictionary
"""

def mergingNode(self, list1, list2):

    intersect = {}
    current = list1
    

    while current != None:
        intersect[current] = True
        current = current.next

    # First duplicate is the intersection
    current = list2
    while current != None:
        if intersect.get(current) != None:
            return current
        
        current = current.next

    return None
        