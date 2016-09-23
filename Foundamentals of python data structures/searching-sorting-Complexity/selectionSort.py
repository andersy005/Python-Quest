
def swap(mylist, i, j):
    temp = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = temp


def selectionSort(mylist):

    i = 0

    while i < len(mylist) - 1:  # Do n - 1 searches

        minIndex = i            # for the smallest
        j = i + 1

        while j < len(mylist):  # Start a search 
            if mylist[j] < mylist[minIndex]:
                minIndex = j

            j += 1

        if minIndex != i:   # Exchange if needed 
            swap(mylist, minIndex, i)

        i += 1


a = [1,2,8,-7,1568,5454,-1,-5668]
print a
selectionSort(a)
print a