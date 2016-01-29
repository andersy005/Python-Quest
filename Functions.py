
def printme(str):
    " This prints a passed string into this function"
    print(str)
    return
print("Hello,")
print("Good Morning!")

# All Parameters are passed by reference

def changeme(mylist):
    " This changes a passed list into this function "
    mylist.append([1, 2, 3, 4])
    print("values inside the function : ", mylist)
    return

mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function : ", mylist)
