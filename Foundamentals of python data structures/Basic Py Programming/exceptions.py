
def safeIntegerInput(prompt):
    inputString = input(prompt)

    try:
        number = int(inputString)
        return number

    except ValueError:
        print ("Error in number format:", inputString)
        return safeIntegerInput(prompt)

if __name__ == "__main__":
    age = safeIntegerInput("Enter your age: ")
    print("Your age is ", age)
