import random

def main():
    
    smaller = int(input("Enter the small number:"))
    larger = int(input("Enter the larger number "))

    myNum = random.randint(smaller, larger)

    count = 0

    while True:

        count += 1
        userNumber = int(input("Enter your guess:"))
        if userNumber < myNum:
            print("Too Small")

        elif userNumber > myNum:
            print("Too large")

        else:
            print("You have got it in", count, "tries!")
            break

if __name__ == "__main__":
    main()

