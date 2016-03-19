def sequentialSearch(alist, item):
    pos = 0 
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True

        else:
            pos = pos + 1


    return found

testlist =[1,15,18,16,5,7,8,83,20,14,57]
print(sequentialSearch(testlist,3))
print(sequentialSearch(testlist,20))