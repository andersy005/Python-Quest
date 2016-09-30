"""A function that replaces all spaces in a string with '%20' """

def replaceSpaces(string):
    
    newString = ""
    for char in string:
        if char != " ":
            newString += char

        else:
            newString +="%20"

    return newString


print(replaceSpaces("ander son"))