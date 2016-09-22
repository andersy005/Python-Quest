import pickle
"""pickle module is available in python 3 only"""
lyst = [60, "A string object", 1977]
fileObj = open("items.dat", "wb")

for item in lyst:
    pickle.dump(item, fileObj)

fileObj.close()


mylist = list()
fileObj = open("items.dat", "rb")
while True:
    try:
        item = pickle.load(fileObj)
        mylist.append(item)

    except EOFError:
        fileObj.close()
        break
print(mylist)