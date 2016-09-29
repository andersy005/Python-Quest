"""this is an extension to Detect Cycle challenge.
Use the same concept of two pointers.
fastPtr moves two pointers and slowPtr moves one pointer
once a cycle is detected, slowPtr is starts from the head 
slowPtr moves one pointer at a time and
fastPtr moves one pointer at a time

SlowPtr will meet fastPtr at the beginning of the loop"""


def detectCycleStart(self):

    slow = self.head.next
    fast = slow.next

    # Each keep walking until they meet again

    while slow != fast:
        slow = slow.next

        try:
            fast = fast.next.next

        except AttributeError:
            return None     # No Cycle if NoneType reached

    
    slow = self.head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow # beginning of the cycle.