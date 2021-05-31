'''
Aim: Given an integer, n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

'''

def print_formatted(n):
    results = []
    for i in range(1,n+1):
        # decimal would be same as the entered number
        decimal = str(i)
        # using oct for converting into octal
        octal = str(oct(i)[2:])
        # using hex for converting into hexadecimal
        hex_ = str(hex(i)[2:]).upper()
        # using bin for converting into binary
        binary = str(bin(i)[2:])
        # appending the results in a list for printing
        results.append([decimal, octal, hex_, binary])
        width = len(results[-1][3])
    for i in results:
        # printing the conversions for all the numbers from i to n
        print(*(rep.rjust(width) for rep in i))
        
# getting the input
n = int(input('Enter integer: '))
print_formatted(n)

'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(N)
     
Sample Input:
15

Sample Output:
   1    1    1    1
   2    2    2   10
   3    3    3   11
   4    4    4  100
   5    5    5  101
   6    6    6  110
   7    7    7  111
   8   10    8 1000
   9   11    9 1001
  10   12    A 1010
  11   13    B 1011
  12   14    C 1100
  13   15    D 1101
  14   16    E 1110
  15   17    F 1111

Explanation:
For all integers, their decimal, octal, hexadecimal and binary forms are printed.

'''