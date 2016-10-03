"""Given two arrays of US social security numbers: Arr1 and Arr2 of lengths n and m respectively, how can you most efficiently compute an array of all persons included on both arrays?

Solve and analyze the complexity for 2 cases:
1. m  n - lengths are approximately the same
2. m  n - one is much longer than the other  """


'''def findDuplicates(Arr1, Arr2):
    duplicates = []

    i = 0
    j = 0

    while i < len(Arr1) and j < len(Arr2):
        if Arr1[i] == Arr2[j]:
            duplicates.append(Arr1[i])

            i += 1
            j += 1

        elif Arr1[i] < Arr2[j]:
            i += 1
        
        else:
            j += 1

    return duplicates


print(findDuplicates([2,3,5], [1,2,3,4]))
'''
# Time Complexity is O(n +m)


# When One array is much longer than the other we should avoid a liner iteration over the longer one
# Since the arrays are sorted, we can do a linear iteration over the shorter and perform binary search for it on the longer array


def findDuplicates(Arr1, Arr2):
    duplicates = []

    for number in Arr1:
        if binarySearch(Arr2, number) != -1:
            duplicates.append(number)

    return duplicates
    

def binarySearch(arr, num):
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        mid = (begin + end) // 2

        if arr[mid] == num:
            return mid

        elif arr[mid] < num:
            begin = mid + 1

        else:
            end = mid - 1

    return - 1
    

print(findDuplicates([2,3,5], [1,2,3,4]))
