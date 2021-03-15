#Chinese Remainder Theorem I divided the code into two files so the solution seems so non taxing and understandable
#second file
# Here in this certain code I have written system of congruences having two equations
from first import *


def CRT(n1, r1, n2, r2):
    x1 = r1 * n2 * const(n2, n1)
    x2 = r2 * n1 * const(n1, n2)
    t = x1 + x2
    return t % (n1 * n2)


def main():
    print("This programme solves a system of congruences for x such that:")
    print("t ≡ r1 (mod a) and t ≡ r2 (mod b)")
    r1 = int(input("Enter r1: "))
    mod1 = int(input("Enter first modulo (a): "))
    r2 = int(input("Enter r2: "))
    mod2 = int(input("Enter second modulo (b): "))
    print("t ≡ {} (mod {}) and t ≡ {} (mod {})".format(r1, mod1, r2, mod2))
    total = CRT(mod1, r1, mod2, r2)
    print("The smallest value that satisfies the inital conditions for t is {}".format(total))


if __name__ == '__main__':
    main()
