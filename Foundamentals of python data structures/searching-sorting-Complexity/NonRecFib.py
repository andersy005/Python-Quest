def fib(n, counter):
    sum = 1
    first = 1
    second = 1
    count = 3

    while count <= n:
        counter +=1
        sum = first + second
        first = second
        second = sum 
        count += 1

    return sum 


print(fib(6,0))