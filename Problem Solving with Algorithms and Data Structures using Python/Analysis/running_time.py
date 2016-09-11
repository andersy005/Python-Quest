import time

def sumOfN2(n):
	start = time.time()

	theSum = 0
	for i in range(1, n+1):
		theSum = theSum + i

	end = time.time()

	print theSum, end-start

sumOfN2(1000000)



def sumOfN3(n):
	start = time.time()
	return ( n * (n+1) )/ 2 ,

print(sumOfN3(1000000))