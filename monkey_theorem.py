import random

def generateOne(strlen):
	alphabet ="abcdefghijklmnopqrstuvwxyz"
	res = ""
	for i in range(strlen):
		res = res + alphabet[random.randrange(25)]

	return res

def score(goal, teststring):
	numscore = 0
	for i in range(len(goal)):
		if goal[i] == teststring[i]:
			numscore = numscore + 1

	return numscore // len(goal)


def main():
	goalstring = 'Welcome to the new World!'
	newstring = generateOne(28)
	best = 0
	newscore = score(goalstring,newstring)

	while newscore < 1:
		if newscore > best:
			print newscore, newstring
			best = newscore

		newstring = generateOne(28)
		newscore = score(goalstring, newstring)

main()




