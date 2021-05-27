"""
Author : Robin Singh
Implementation of Eqyption Fraction
Every positive fraction can be represented as sum of unique unit fractions
A fraction is unit fraction if numerator is 1 and denominator is a positive integer, for example 1/3 is a unit fraction
Such a representation is called Egyptian Fraction as it was used by ancient Egyptians
"""

import math


def egyptianFraction(numerator, denominator):
    ef = []
    while numerator != 0:

        x = math.ceil(denominator / numerator)  # Main
        ef.append(x)
        numerator = x * numerator - denominator
        denominator = denominator * x
    for i in range(len(ef)):
        if i != len(ef) - 1:
            print(f" 1/{ef[i]} +", end=" ")

        else:
            print(f"1/{ef[i]}", end=" ")


if __name__ == '__main__':
    nr = int(input("Enter  numerator"))
    dr = int(input("Enter  denominator"))
    print(f"Egyptian Fraction of {nr}/{dr} : ")
    egyptianFraction(nr, dr)


# Enter  numerator 25
# Enter  denominator 78
#  Egyptian Fraction of 25/78 :
# 1/4 +  1/15 + 1/260
