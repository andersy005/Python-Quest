from pythonds.basic.stack import Stack

s = Stack()

str = 'my python Script'

for i in range(len(str)):
	s.push(str[i])


mystr=''


while not s.isEmpty():
	mystr += s.peek()
	s.pop()

print mystr