# The Following is O(N^2) Solution to Find if two strings are Anagrams

def anagramSolutuion1(str1, str2):
	aList = list(str2)

	pos1 = 0
	stillOK = True

	while pos1 < len(str1) and stillOK:
		pos2 = 0
		found = False

		while pos2 < len(aList) and not found:
			if str1[pos1] == aList[pos2]:
				found = True

			else:
				pos2 = pos2 + 1


		if found:
			aList[pos2] = None
		else:
			stillOK = False

		pos1 = pos1 + 1


	return stillOK


print(anagramSolutuion1('abcd','fcba'))



# Solution 2: Sort and Compare

def anagramSolution2(str1, str2):
	aList1 = list(str1)
	aList2 = list(str2)

	aList1.sort()
	aList2.sort()

	pos = 0
	matches = True

	while pos < len(str1) and matches:
		if aList1[pos] == aList2[pos]:
			pos =  pos + 1

		else:
			matches = False

	return matches

print(anagramSolution2('abcde', 'abmde'))


#Solution 3: Count and Compare Linear Solution:

def anagramSolution3(str1, str2):
	c1 = [0]*26
	c2 = [0]*26

	for i in range(len(str1)):
		pos = ord(str1[i]) - ord('a')
		c1[pos] = c1[pos] + 1

	
	for i in range(len(str1)):
		pos = ord(str2[i]) - ord('a')
		c2[pos] = c2[pos] + 1

	j = 0
	stillOK = True

	while j < 26 and stillOK:
		if c1[j] == c2[j]:
			j = j + 1

		else:
			stillOK = False

	return stillOK

print(anagramSolution3('apple', 'pleap'))
		