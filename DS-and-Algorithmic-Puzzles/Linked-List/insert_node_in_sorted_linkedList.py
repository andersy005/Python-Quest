def orderedInsert(self, item):
    current = self.head
    previous = None

    stop = False

    while current != None and not stop:
        if current.data > item:
            stop = True

        else:
            previous = current
            current = current.next


    temp = Node()
    if previous == None:
        temp.next = self.head
        self.head = temp

    else:
        temp.next = current
        previous.next = temp

        