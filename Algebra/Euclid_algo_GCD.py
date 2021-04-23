# Implementation of Euclid Algorithm to find GCD in Python3

def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


print("\nEnter two numbers to find their GCD: ", end=" ")
num1, num2 = [int(i) for i in input().split()]

gcdNum = gcd(num1, num2)
print("\nGCD of", num1, "and", num2, "is:", gcdNum)

# Sample output :
# Enter two numbers to find their GCD: 60 36          

# GCD of 60 and 36 is: 12
