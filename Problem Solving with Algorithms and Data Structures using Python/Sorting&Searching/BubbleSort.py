def BubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

alist = [54,26,93,17,18,77,31,44,55,20]
BubbleSort(alist)
print(alist)
