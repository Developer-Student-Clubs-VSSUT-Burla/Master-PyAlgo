# Program to find if the number is an automorphic number or not.
# Automorphic number is a number such that its square ends in the same digit as the number itself.

def automorphic_num(num):
    sq = num ** 2
    if num % 10 == sq % 10:
        print (num, 'is an automorphic number')
    else:
        print (num, 'is not an automorhic number')

num = int(input('Enter the number to be checked:'))
automorphic_num(num)

'''
Sample Output
Enter the number to be checked:25
25 is an automorphic number

Enter the number to be checked:7
7 is not an automorphic number
'''

