#!/usr/bin/python

# str = input("Enter your input: ")
# print("Received input is: ", str)

# Open a file
fo = open("python.txt", "w")

print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)

# Write any string to an open file
fo.write("This is The Flash! How May I help you Cortana?");

# Close opened file
fo.close()


# Read File
fo = open("python.txt", "r+")
mystr = fo.read(20)
print(" The File Contains: ",mystr)

# File position
position = fo.tell()
print("Current file Position: ", position)

# Reposition Pointer at the beginning  once again
position = fo.seek(0,0)
str = fo.read(10)
print("Again read String is: ", str)

fo.close()






