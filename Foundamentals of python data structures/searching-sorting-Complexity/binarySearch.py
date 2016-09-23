def BinarySearch(target, sortedlist):
    left = 0
    right = len(sortedlist) - 1

    while left <= right:
        midpoint = (left + right)//2

        if target == sortedlist[midpoint]:
            return midpoint

        elif target < sortedlist[midpoint]:
            right = midpoint - 1

        else:
            left = midpoint - 1

    return -1


print(BinarySearch(2, [1,3,5,9]))