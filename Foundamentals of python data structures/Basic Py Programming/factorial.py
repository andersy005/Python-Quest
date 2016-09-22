def factorial(n, product=1):
    """Returns the factorial of n."""
    if n == 1:
        return (product)
    else:
        return factorial(n-1, n * product)


factorial(5,1)