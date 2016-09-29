"""Use two pointers moving at different speeds
fastPtr moves two pointers while slowPtr moves one pointer at a time.
Once they enter the loop they are expected to meet"""

def detectCycle(self):
    fastPtr = self.head
    slowPtr = self.head


    while(fastPtr and slowPtr):
        fastPtr = fastPtr.next

        if fastPtr == slowPtr:
            return True

        if fastPtr = None:
            return False


        fastPtr = fastPtr.next

        if fastPtr == slowPtr:
            return True

        slowPtr = slowPtr.next