import random
f = open("integers.txt", 'w')

for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + "\n")
f.close()