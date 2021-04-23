'''
    Sieve of Atkin is a modern algorithm for finding all prime numbers up to a
	specified integer. Compared with the ancient Sieve of Eratosthenes, which
	marks off multiples of primes, the Sieve of Atkin does some preliminary work
	and then marks off multiples of squares of primes, thus achieving a better 
	theoretical asymptotic complexity.
 	
 	We are going to check the following condition and according to that we
 	decide prime numbers
 	a) a = (4*i*i)+(j*j) has odd number of  
       solutions, i.e., there exist 
       odd number of distinct pairs (i, j)  
       that satisfy the equation and 
        n % 12 = 1 or n % 12 = 5. 
    b) n = (3*i*i)+(j*j) has odd number of  
       solutions and n % 12 = 7 
    c) n = (3*i*i)-(j*j) has odd number of  
       solutions, i > j and n % 12 = 11
'''

#For using .sqrt() method
import math

def sieveOfAtkin(limit):
    #Creating a empty list.
    P=[]
    if limit ==2:
        return P
    P=[2]
    if limit==3:
        return P
    #Adding 2 and 3 as prime numbers
    P = [2,3]
    #Creating a list of boolean type of size n and
	#initialize it with false value     
    sieve=[False]*(limit+1)

    #Iterating over the numbers
	#If it is prime we make sieve[a]=true
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            #Making equations for prime numbers
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) :
                sieve[n] = not sieve[n]

            n = 3*x**2+y**2
            if n<= limit and n%12==7 :
                sieve[n] = not sieve[n]

            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : 
                sieve[n] = not sieve[n]

    #Mark all multiples of squares as non-prime 
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    #Appending all the prime numbers in a list
    for p in range(5,limit):
        if sieve[p] : 
            P.append(p)
    return P

n=int(input("Enter the value upto you want the prime numbers\n"))
print(sieveOfAtkin(n))


'''
    Sample Input:
     43
    Sample Output:
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41

    Time Complexity: O(n/log(log(n)))
    Space Complexity:O(n^0.5)
'''
