import math

# def isPrime(num):
# 	if num == 2 or num == 3:
# 		return True
# 	elif num % 2 == 0 or num % 3 == 0:
# 		return False
# 	else:
# 		return True

# print(isPrime(123))



def get_next_prime_factor(n):
	# see if the number is divisible  by 2. If so then return 2
	if n % 2 == 0 :
		return 2
	# check all of the odd numbers up to n // 2	
	for x in range(3,n//2,2):
		if n % x == 0:
			return x

	return n


def get_prime_factors(n):
	factors = []

	while n > 1:
		factor = get_next_prime_factor(n)
		factors.append(factor)
		n = n // factor

	return factors

print(get_prime_factors(100))

# The following is another way of generating prime factors

def primegen(n):
	yield 2

	primes = []
	primeCandidate = 3

	while primeCandidate < n:
		plist = [primeCandidate % p for p in primes]
		if all(plist):
			primes.append(primeCandidate)
			yield primeCandidate

		primeCandidate += 2

primelist = primegen(100)
print list(primelist)

