"""Created by debjitpal5040

  This is the program to count total number of divisors of an integer

  Time Complexity is O(n^1/3)

  The algorithm can be stated as :
      Split number n in two numbers x and y such that n=x*y
      where x contains only prime factors in range 2 <= x <= n^(1/3) and
      y deals with higher prime factors greater than n^(1/3).
      Count total factors of x using the naive trial division method. Let this count be F(x).
      Count total factors of y using the following three cases. Let this count be F(y). 
        If y is a prime number then factors will be 1 and y itself. That implies, F(y) = 2.
        If y is square of a prime number, then factors will be 1, sqrt(y) and y itself. That implies, F(y) = 3.
        If y is the product of two distinct prime numbers, then factors will be 1, both prime numbers and number y itself. That implies, F(y) = 4.
      Since F(x*y) is a multiplicative function and gcd(x, y) = 1, that implies, F(x*y) = F(x)*F(y) 
      which gives the count of total distinct divisors of n.

"""
def Eratosthenes(n, prime,primesquare, a):
	for i in range(2,n+1):
		prime[i] = True
	for i in range((n**2 + 1)+1):
		primesquare[i] = False
	prime[1] = False
	p = 2
	while(p**2 <= n):
		if (prime[p] == True):
			i = p * 2
			while(i <= n):
				prime[i] = False
				i += p
		p+=1
	j = 0
	for p in range(2,n+1):
		if (prime[p]==True):
			a[j] = p
			primesquare[p**2] = True
			j+=1
def countDivisors(n):
	if (n == 1):
		return 1
	prime = [False]*(n + 2)
	primesquare = [False]*(n**2 + 2)
	a = [0]*n
	Eratosthenes(n, prime, primesquare, a)
	ans = 1
	i=0
	while(1):
		if(a[i]**3 > n):
			break
		cnt = 1 
		while (n % a[i] == 0): 
			n //= a[i]
			cnt += 1 
		ans *= cnt
		i+=1
	if (prime[n]==True):
		ans *= 2
	elif (primesquare[n]==True):
		ans *= 3
	elif (n != 1):
		ans *= 4
	return ans 
x=int(input("Please enter the integer : "))
print("Total number of divisors of "+ str(x) + " is :",countDivisors(x))

"""
Please enter the integer : 
#Input : 36
#Output : Total number of divisors of 36 is : 9

Please enter the integer : 
#Input : 80
#Output : Total number of divisors of 80 is : 10

Please enter the integer : 
#Input : 60
#Output : Total number of divisors of 60 is : 12
"""

