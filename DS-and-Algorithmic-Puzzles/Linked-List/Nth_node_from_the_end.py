"""Use two pointers P and N. Initially, both points to head node of the LL.
P starts moving only after N has made n moves. From there both move forward until N reaches 
the end of the list. As a result P points to nth node from the end

For example: 1->3->4->10->5->Null
find 3rd element from the end

Step 1: P starts at 1
        N starts at 1

Step 2: N makes 3 moves. therefore points to 10 

Step 3: P points to 3 when N points to 5

Step 4: P points to 4 while N reaches the end of the List and at this point, P is pointing at the 3rd Node from the end
"""

def nthNodeFromEnd(self, n):
    if n < 0:
        return None

    # Counts k units from the self.head
    
    temp = self.head
    count = 0

    while n > count and temp != None:
        temp = temp.next
        count += 1

    # If the LinkedList does not contain k elements, return None

    if n > count or temp = None:
        return None

    nth = self.head
    while temp.next != None:
        temp = temp.next
        nth = nth.next

    return nth 