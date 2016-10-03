""""""
def stringCompression(string):
    mystr = ""
    last = string[0]
    count = 1

    for i in range(1,len(string)):
        if string[i] == last:
            count += 1
        else:
            mystr = mystr + last +"" + str(count) 
            last = string[i] 
            count = 1

    return mystr + last + str(count)

print(stringCompression("aabccccaaaa"))
