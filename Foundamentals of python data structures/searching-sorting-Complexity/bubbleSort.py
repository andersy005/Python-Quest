def swap(mylist, i, j):
    temp = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = temp



def bubbleSort(mylist):
    n = len(mylist)

    while n > 1:    # Do n - 1 bubbles
        i = 1       # Start each bubble 

        while i < n:
            if mylist[i] < mylist[i-1]: 
                swap(mylist, i, i-1)

            i += 1

        n -= 1



a = [1,2,8,-7,1568,5454,-1,-5668]
print a
bubbleSort(a)
print a


def bubbleSortWithTweak(mylist):
    n = len(mylist)

    while n > 1:    # Do n - 1 bubbles
        swapped = False
        i = 1       # Start each bubble 

        while i < n:
            if mylist[i] < mylist[i-1]: 
                swap(mylist, i, i-1)
                swapped = True

            i += 1
        if not swapped:
            return              # Return if no swaps
        n -= 1



a = [1,2,8,-7,1568,5454,-1,-5668]
print a
bubbleSort(a)
print a