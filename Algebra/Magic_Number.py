''' Magic Number
If the sum of its digits are calculated till a single digit comes by adding the sum of digits after every addition.
If single digit comes out to be 1 then the number is a magic number.
'''
# Function to check if the number is a magic number or not

def magic_num(num):
    while num > 9:
        sum1 = calsum(num)
        num = sum1
    return num

# Function to calculate the sum of digits of the number

def calsum(num):
    add = 0
    while num > 0:
        rem = num % 10
        add = add + rem
        num = num // 10
    return add

if __name__ == '__main__':
    num = int(input('Enter the numebr to be checked:'))
    if magic_num(num) == 1:
        print (num, 'is a magic number')
    else:
        print (num, 'is not a magic number')

'''
Sample Output
Enter the number to be checked:1729
1729 is a magic number

Enter the number to be checked:123
123 is not a magic number
'''
