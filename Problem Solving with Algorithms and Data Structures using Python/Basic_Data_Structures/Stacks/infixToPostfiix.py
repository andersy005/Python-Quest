from pythonds.basic.stack import Stack 

def infixToPostfix(infixepr):
	"""Create an empty stack called opstack for keeping operators. Create an empty list for output.
Convert the input infix string to a list by using the string method split.
Scan the token list from left to right.
If the token is an operand, append it to the end of the output list.
If the token is a left parenthesis, push it on the opstack.
If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.
"""
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1

	opStack = Stack()

	postfixList = []
	tokenList = infixepr.split()

	for token in tokenList:
		  if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
		  	postfixList.append(token)
		  elif token == '(':
		  	opStack.push(token)
		  elif token ==')':
		  	topToken = opStack.pop()
		  	while topToken != '(':
		  		postfixList.append(topToken)
		  		topToken = opStack.pop()

		  else:
		  	while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
		  		postfixList.append(opStack.pop())

		  	opStack.push(token)


	while not opStack.isEmpty():
		postfixList.append(opStack.pop())

	return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))






