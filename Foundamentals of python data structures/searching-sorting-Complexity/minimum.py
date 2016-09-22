
def indexOfMin(mylist):
    """Returns the index of the minimum item"""

    minIndex = 0
    currentIndex = 1

    while currentIndex < len(mylist):
        if mylist[currentIndex] < mylist[minIndex]:
            minIndex = currentIndex

        currentIndex += 1

    return minIndex


print(indexOfMin([1,2,8,7,1568,5454,-1,-5668]))