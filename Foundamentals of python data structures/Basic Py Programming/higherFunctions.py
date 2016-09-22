# map function
""""""
alist = [2,3,5,-1,48,-58]
print alist
blist = list(map(str, alist))
print "list of int changed into list of str: ", blist

# filter function and lambda function
"""lambda <argument list> : <expression>"""

clist = list(filter(lambda number: number > 0, alist))
print "list of positive values only: ", clist

# functools, reduce

import functools

product = functools.reduce(lambda x , y: x * y, range(1,11))
print "product of a sequence of numbers: ", product