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


print(anagramSolutuion1('abcd','dcba'))