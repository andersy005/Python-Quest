"""Detect a cycle and then Initialize a counter and move slowPtr one pointer at a time while keeping
fastPtr static and incrementing the counter. When slowPtr meets fastPtr. That should give us the length
of the cycle """


def findLoopLength(self):
    slow = self.head.next
    fast = slow.next

    if self.head == None or self.head.next == None:
        return None

    while slow != fast:
        slow = slow.next
        try:
            fast = fast.next.next

        except AttributeError:
            return None

        
    LoopLength = 0
    slow = slow.next

    while slow != fast:
        slow = slow.next
        LoopLength += 1

    return LoopLength