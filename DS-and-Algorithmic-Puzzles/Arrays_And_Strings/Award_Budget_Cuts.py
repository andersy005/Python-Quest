from __future__ import division
"""Assuming g isn't empty and b is indeed smaller than the sum of all grants, we need to find the cap c.
To compute effectively, we sort the array first. Let r be the index of the lowest grant to be capped, hence: g[r-1] <= c <= g[r]. The capped sum is: capped(cap) = sum(g[0], g[1], ..., g[r-1]) + (n - r)*cap, 
for such r. Clearly capped(c) = b, and by our definition of r: capped(g[r-1]) <= b <= capped(g[r]). Once we find r, we can calculate c easily from the capped sum equation.

Linear scan for r is possible but not optimal. A better approach to find r is by a something similar to binary search. This can work because the array is sorted. 
We can apply the inequality capped(g[r-1]) <= b <= capped(g[r]) as our stopping condition for the search. For each middle index on the search we compute capped(g[m]) and capped(g[m-1]) and 
direct the search accordingly."""


"""Runtime Complexity: Since we know nothing about the grants, sorting the grants takes O(n*log n). Pre-computation over the grants is a linear O(n). 
Binary search is O(log n) because the reminder to search in is divided by 2 at each iteration. Total complexity is a linear O(n) for sorted grants or O(n * log n) for non-sorted.

Space Complexity: O(n) for using another array for pre-computations. If short in memory space to store this, we avoid the pre-computation and do a linear iteration for each cappedSum calculation. 
This would make the space complexity O(1) and the runtime complexity O(n*log n).

"""


def findGrantsCap(grants, budget):
    if (len(grants) == 0):
        return 0

    n = len(grants)

    partialSums = [0] * n
    tempSum = 0

    for i in range(n):
        tempSum += grants[i]
        partialSums[i] = tempSum
        print "temp sum", tempSum
        print "partial Sums", partialSums
        print "*" * 100

    if partialSums[n-1] <= budget:
        return grants[n-1]


    def cappedSum(i):
        print "partialSums[i-1]", partialSums[i-1], "grants[i]", grants[i], "i", i , "n", n, "n-i", n-i
        return partialSums[i-1] + grants[i] * (n-i)

    start = 0
    end = n - 1

    while(end > start):
        r = (start + end) // 2
        print "r", r 
        if r > 0:
            if cappedSum(r) > budget:
                print "capped Sum(r)", cappedSum(r)
                print "capped sum(r-1)", cappedSum(r-1)
                if cappedSum(r-1) < budget:
                    break

                else:
                    end = r - 1
                    
            else:
                start = r + 1
    print "*" * 100
    print "budget", budget
    print "partialSums[r-1]", partialSums[r-1]
    print "n-r", n-r           
    c = (budget - partialSums[r-1]) / (n - r)
    print "cap", c
    return c

grants = [10000, 20000, 30000, 40000, 120000, 150000, 200000]

findGrantsCap(grants, 100000)



   



