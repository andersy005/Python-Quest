
def reverseList(self):
    last = None
    current = self.head

    while current is not None:
        nextNode = current.next
        current.next = last
        last = current
        current = nextNode

    self.head = last


"""
1->5->8->10
step 1: last = None                     
        current = 1
        
        nextNode = 5
        current.next = None            ->5->1->None
        last = 1
        current = 5


step 1: last = 1
        current = 1
        
        nextNode = 5
        current.next = None 
        last = 1
        current = 5
         
        """