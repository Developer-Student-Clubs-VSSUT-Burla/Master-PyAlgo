'''
Pollard's Rho Algorithm is a very interesting and quite accessible algorithm for factoring numbers. It is not the fastest algorithm by far but in practice it outperforms trial
division by many orders of magnitude. It is based on very simple ideas that can be used in other contexts as well.
It is an algorithm for integer factorization.The algorithm is very fast for numbers with small factors, but slower in cases where all factors are large.
The ρ algorithm's most remarkable success was the factorization of the Fermat number F8 = 1238926361552897 * 93461639715357977769163558199606896584051237541638188580280321
The algorithm is used to factorize a number n =ab, where a is a non-trivial factor. A polynomial modulo n, called f(x) (e.g., f(x)= (x*x+1) mod n) is used to generate a pseudorandom
sequence . A starting value say 2, is chosen , and the sequence continues as x1 = f(2), x2=f(f(2)), x3 = f(f(f(2))), etc. The sequence is related to another sequence {xk mod p}.
 Since p is not known beforehand, this sequence cannot be explicitly computed in the algorithm. Yet, in it lies the core idea of the algorithm.
**How the algorithm work
    x ← 2   #take any value of x and make y=x
    y ← 2
    d ← 1

    while d = 1:
        x ← g(x)     #g(x)=(x*x+c)%n, n is the number whose factor we are evaluating
        y ← g(g(y))   # update x=g(y) ,repeat this process till the gcd not become the factor 
        d ← gcd(|x - y|, n)   # gcd of absolute difference of x & y and of num is taken

    if d = n:       #if gcd is equal to n then there no factor exist other one and itself
        return failure
    else:
        return d
'''
#import needed library
from itertools import count
from fractions import gcd
import sys
#take input "number" whose factor we have to determine
#take any value for x and c, here c=1 is taken
number=int(input())
x=2
# run the loop till you don't find the factor 
for cycle in count(1):
#here we assign y=x
    y = x
    for i in range(2 ** cycle):
# we use polynomial function to find factor 
# function, y=(x*x+c)%number
        x = (x * x + 1) % number
#take gcd of absolute difference of x&y and number
#gcd is treated as a factor if it is not unity
        factor = gcd(x - y, number)
        if factor > 1:
            print("factor is", factor)
            sys.exit()

''' INPUT 

    10403
    
    OUTPUT
    
    factor is 101
'''
