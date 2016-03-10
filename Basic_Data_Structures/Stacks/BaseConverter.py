from pythonds.basic.stack import Stack

def baseConverter(decNumber,base):
	digits = "0123456789ABCDEF"
	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % base
		remstack.push(rem)
		decNumber = decNumber // base


	binString =''
	while not remstack.isEmpty():
		binString += digits[(remstack.pop())]


	return binString

print(baseConverter(256,16))