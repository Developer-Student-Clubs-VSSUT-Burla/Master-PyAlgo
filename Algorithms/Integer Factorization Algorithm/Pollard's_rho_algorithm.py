Pollard's rho algorithm is an algorithm for integer factorization.The algorithm is very fast for numbers with small factors, but slower in cases where all factors are large.
The ρ algorithm's most remarkable success was the factorization of the Fermat number F8 = 1238926361552897 * 93461639715357977769163558199606896584051237541638188580280321
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

CODE:
#import needed library
from itertools import count
from math import gcd
import sys
#take input "number" whose factor we have to determine
#take any value for x and c, here c=1 is taken
number, x = 10403, 2
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
