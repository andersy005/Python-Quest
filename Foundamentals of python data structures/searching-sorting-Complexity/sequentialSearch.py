def sequentialSearch(target, mylist):
    """Returns the position of the target item if found or -1 otherwise"""

    position = 0

    while position < len(mylist):
        if target == mylist[position]:
            return position

        position += 1

    return -1


print(sequentialSearch(2, [1,2,8,7,1568,5454,-1,-5668]))


