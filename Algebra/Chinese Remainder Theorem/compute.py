# Chinese Remainder Theorem I divided the code into two files so the solution seems so non taxing and understandable
# second file
# Here in this certain code I have written system of congruences having two equations
from compute_inverse import *
def ChineseRemainderTheorem(n1, r1, n2, r2):
    x1 = r1 * n2 * compute_inverse(n2, n1)
    x2 = r2 * n1 * compute_inverse(n1, n2)
    x = x1 + x2
    return x % (n1 * n2)


def main():
    print("This programme solves a system of congruences for x such that:")
    print("x ≡ r1 (mod a) and x ≡ r2 (mod b)")
    r1 = int(input("Enter r1: "))
    mod1 = int(input("Enter first modulo (a): "))
    r2 = int(input("Enter r2: "))
    mod2 = int(input("Enter second modulo (b): "))
    print("x ≡ {} (mod {}) and x ≡ {} (mod {})".format(r1, mod1, r2, mod2))
    result = ChineseRemainderTheorem(mod1, r1, mod2, r2)
    print("The smallest value that satisfies the inital conditions for x is {}".format(result))

if __name__ == '__main__':
    main()

#Function Name	                NLOC	Complexity	Token
#ChineseRemainderTheorem	      5	       1	     48
#   main	                     10        1	     84