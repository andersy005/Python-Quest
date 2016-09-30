"""An Algorithm to determine if a string has all unique characters
Assume that the string is an ASCII string. what if it was a unicode string?"""

def hasUniqueChars(string):
    if len(string) > 128:
        return False

    chars = [None] * 256
    for i in range(len(string)):
        val = string[i]
        print val

        if chars[ord(val)]:
            return False

        chars[ord(val)] = True

    return True


print(hasUniqueChars("brenda"))


def hasUniqueChars1(string):
    if len(string) > 128:
        return False

    chars = {}
    for i in range(len(string)):
        val = string[i]
        print val

        if val in chars:
            return False

        chars[val] = True

    return True


print(hasUniqueChars1("brenda"))