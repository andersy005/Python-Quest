def isPalindrome(str):
	if len(str) < 2:
		return True
	if str[0] != str[-1]:
		return False

	else:
		return isPalindrome(str[1:-1])

print(isPalindrome('wassamassaw'))
