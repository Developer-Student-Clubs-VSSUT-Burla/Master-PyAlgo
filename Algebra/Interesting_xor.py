'''You are given an integer C. Let d be the smallest integer such that 2^d is strictly greater than C.
Consider all pairs of non-negative integers (A,B) such that A,B<2d and A⊕B=C. 
(⊕ denotes the bitwise XOR operation). 
Find the maximum value of A*B over all these pairs.
Constraints
1≤T≤10^5
1≤C≤10^9
'''

import math

def interesting_xor(c):
    x = math.log2(c)
    y = math.ceil(x)
    z = 2 ** y
    sub = z - c
    if sub == 0:
        sub = c
        num1 = z - 1
        print(num1 * (num1 + sub))
    else:
        num1 = z // 2 - 1
        print(num1 * (num1 + sub))

if __name__ == '__main__':
    t = int(input('Enter the number of testcases:'))
    while t > 0:
        c = int(input('Enter the value of c:'))
        interesting_xor(c)
        t = t - 1

'''
Sample Output
Enter the numeber of testcases:2
Enter the value of c:10
91
Enter the value of c:13
70
'''
       
