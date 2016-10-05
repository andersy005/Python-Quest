"""
* Given an array of int, count number of sub arrays (of size more than one) that are 
strictly increasing

* Time Complexity O(n)

* Space complexity O(1)


Ex: arr = [1,4,3] 
output 1
one subarrat=y [1,4]

arr = [1,2,3,4]
output 6
6 subarrays [1,2], [1,2,3], [1,2,3,4], 
            [2,3], [2,3,4], [3,4]"""


def count_subarrays(arr):
    # Initialize result
    count = 0
    
    # Initialize length of current increasing subarray
    length = 1


    # Traverse through the array 
    for i in range(len(arr)-1):
        # if arr[i+1] is greater than arr[i], increment the length

        if arr[i+1] > arr[i]:
            length += 1

        # Else Update count and reset length
        else:
            count += (((length-1) * length)/ 2)
            length = 1


    # If last lenth is more than 1

    if length > 1:
        count += (((length-1) * length)/ 2)

    return count


print(count_subarrays([10,20,30,40,31]))