import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
pw_length = 8
mypassword = ""

# first generate a password of all lower case letters
for i in range(pw_length):
	next_index = random.randrange(len(alphabet))
	mypassword = mypassword +  alphabet[next_index]

#randomly replace 1 or 2 characters with a number
#To make sure we don't accidentaly replace numbers with uppercase characters or vice-versa,
#We put numbers in the first half of the password and capital letters in the second  half
for i in range(random.randrange(1,3)):
	replace_index = random.randrange(len(mypassword)//2)
	mypassword = mypassword[0:replace_index]+ str(random.randrange(10))+ mypassword[replace_index+1:]


#randomly replace 1 or 2 letters with an uppercase letter
for i in range(random.randrange(1,3)):
	replace_index = random.randrange(len(mypassword)//2, len(mypassword))
	mypassword = mypassword[0:replace_index]+ mypassword[replace_index].upper()+ mypassword[replace_index+1:]
print(mypassword)


