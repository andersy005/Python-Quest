"""An Algorithm to determine if a string has all unique characters
Assume that the string is an ASCII string. what if it was a unicode string?"""

def hasUniqueChars(string):
    if len(string) > 128:
        return False

    chars = [None] * 256
    for i in range(len(string)):
        val = string[i]
    

        if chars[ord(val)]:
            return False

        chars[ord(val)] = True

    return True


print(hasUniqueChars("brenda"))

# uses a dictionary instead of a list
def hasUniqueChars1(string):
    if len(string) > 128:
        return False

    chars = {}
    for i in range(len(string)):
        val = string[i]

        if val in chars:
            return False

        chars[val] = True

    return True


print(hasUniqueChars1("brenda"))

print '#' * 70


# the following does it in constant space and uses a bit vector
def hasUniqueChars2(string):
    checker = 0
    for i in range(len(string)):
        val = ord(string[i]) - ord('a')
        print val

        if (checker & (1 << val)) > 0 :
            return False

        checker |= (1 << val)

    return True

print(hasUniqueChars2("brenda"))