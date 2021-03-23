# Program to check if the given number is a strong number or not

# To calculate the factorial of the number
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


# To check if the number is a strong number

def strong_number(num):
    sum1 = 0
    original_num = num
    while num > 0:
        digit = num % 10
        sum1 = sum1 + fact(digit)
        num = num // 10
    if sum1 == original_num:
        print (original_num, 'is a strong number')
    else:
        print (original_num, 'is not a strong number')


num = int(input('Enter the number to be checked:'))
x = strong_number(num)

'''
Sample Output
Enter the number to be checked:145
145 is a strong number
'''

