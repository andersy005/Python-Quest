
def insertionSort(mylist):
    i = 1

    while i < len(mylist):
        itemToInsert = mylist[i]
        j = i - 1

        while j >= 0:
            if itemToInsert < mylist[j]:
                mylist[j+1] = mylist[j]
                j -= 1

            else:
                break

        mylist[j+1] = itemToInsert
        i += 1



a = [1,2,8,-7,1568,5454,-1,-5668]
print a
insertionSort(a)
print a