def insertionSort(alist):
	for index in range(1,len(alist)):

		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position-1] > currentvalue:
			alist[position] = alist[position-1]
			position = position - 1


		alist[position] = currentvalue

alist = [ 54, 26,93,17,97,100,34,55,84,20,5]
insertionSort(alist)
print(alist)