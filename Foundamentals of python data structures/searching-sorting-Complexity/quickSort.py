def quickSort(mylist):
    quickSortHelper(mylist, 0, len(mylist)-1)

def quickSortHelper(mylist, left, right):
    if left < right:
        pivotLocation = partition(mylist, left, right)
        quickSortHelper(mylist, left, pivotLocation - 1)
        quickSortHelper(mylist, pivotLocation + 1, right)

def partition(mylist, left, right):
    # Find the pivot and exchange it with the last item

    middle = (left + right) // 2

    pivot = mylist[middle]
    mylist[middle] = mylist[right]
    mylist[right] = pivot

    # Set boundary point to first position
    boundary = left

    # Move items less than pivot to the left
    for index in range(left, right):
        if mylist[index] < pivot:
            swap(mylist, index, boundary)
            boundary += 1

    # Exchange the pivot item and the boundary item
    swap(mylist, right, boundary)
    return boundary


def swap(mylist, i, j):
    temp = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = temp

import random

def main(size=20, sort=quickSort):
    mylist = []
    for count in range(size):
        mylist.append(random.randint(1, size + 1))

    print(mylist)
    sort(mylist)
    print(mylist)

if __name__ == "__main__":
    main()
    

