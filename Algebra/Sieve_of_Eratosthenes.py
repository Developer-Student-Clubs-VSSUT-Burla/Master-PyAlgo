# Program to find all the prime numbers less than n
# using Sieve of Eratosthenes
# In this first we create a boolean list of length n and initialize it with True value
# Starting from the 2 it assign false value to all the multiple of 2
# Repeat the process with each number whose value is True in list untill the square root of n
# Finally iterate over the list and the values having value True are printed as prime numbers

def SieveOfEratosthenes(n):
   # Create a list of boolean type with True values in it.
   prime = [True for i in range(n + 1)]
   p = 2
   while (p * p <= n):
      # If it remain unchanged it is prime
      if (prime[p] == True):
         # updating all the multiples
         for i in range(p * 2, n + 1, p):
            prime[i] = False
      p += 1
   prime[0]= False
   prime[1]= False
   # Print the prime numbers.
   # if value of prime[i] is true than it is prime number 
   for p in range(n + 1):
      if prime[p]:
         print (p,end=" ")
          
# main
if __name__=='__main__':
    #Taking input from user
    print("Enter the value of n")
    n = int(input())
    print ("The prime numbers smaller than or equal to "+ str(n)+" is")
    SieveOfEratosthenes(n)

    
#Input- 63
#Output-The prime numbers smaller than or equal to 63 is
#       2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 

#Time Complexity - O(n(log(logn))
#Space Complexity- O(n^0.5)
