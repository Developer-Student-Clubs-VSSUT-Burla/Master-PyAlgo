'''
A decagonal number is a figurate number that extends the concept of 
triangular and square numbers to the decagon (a ten-sided polygon).
    
The n-th decagonal number is given by the formula:
Dn = 4n^2 - 3n.
'''
def decagonalNumber (num):
    return 4 * num * num - 3* num

num = int(input("Enter the number : "))
print(num , "decagonal number :",decagonalNumber(num))

'''
Sample Output
Enter the number : 6
6 decagonal number : 126
'''

