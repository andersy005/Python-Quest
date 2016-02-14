

def fibonacci(n):
    if n == 0:
        return  0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n - 2)
        print result
        return result

fibonacci(5)

def factorial(n):
    space = ' ' * (4 * n)
    print space, 'factorial', n

    if n == 0:
        print space, 'returning 1'
        return 1
    else:
        recurse = factorial(n-1)
        res = n * recurse
        print space, 'returning', res
        return res

factorial(10)
