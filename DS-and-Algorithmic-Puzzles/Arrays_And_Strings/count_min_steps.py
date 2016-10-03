"""Count minimum steps to get the given desired array"""
"""The awards committee had planned to give n research grants this year, out of a its total yearly budget.
However, the budget was reduced to b dollars. The committee members has decided to affect the minimal number of highest grants, by applying a maximum cap c on all grants: every grant that was planned to be higher than c will now be c dollars.
Help the committee to choose the right value of c that would make the total sum of grants equal to the new budget.

Given an array of grants g and a new budget b, explain and code an efficient method to find the cap c. Assume that each grant is unique.
Analyze the time and space complexity of your solution."""


def countMinOper(target_array):

    result = 0            # Initialize result(count of minimum operations
    while True:

        zeroCount = 0
        i = 0
        n = len(target_array)
        while i < n :
            if target_array[i] & 1:
               # If odd number found
                break

            elif target_array[i] == 0:      # If 0, then increment zeroCount
                zeroCount += 1
            i += 1


        # All numbers are 0
        if zeroCount == n:      
            return result

        # All numbers are even
        if i == n: 
            # Divide the whole array by 2 and increment result                          
            for j in range(n):
                target_array[j] = target_array[j] // 2 

            result += 1

        # Make all odd numbers even by subtracting one and increment result
        j = i

        while j < n:
            if target_array[j] & 1:
                target_array[j] -= 1
                result += 1
            j += 1


print(countMinOper([2,2]))



        