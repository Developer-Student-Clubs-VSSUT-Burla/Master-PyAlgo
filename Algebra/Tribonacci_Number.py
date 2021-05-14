'''
It is a series of numbers where each term is the sum of preceeding 3 numbers of the sequence.

T(n) = T(n-1) + T(n-2) + T(n-3)
'''
def tribonacciNumber(number):
    if number <= 0:
        return -1
    elif number == 1:
        return 0
    elif number == 2:
        return 0
    elif number == 3:
        return 1
    return tribonacciNumber(number - 1) + tribonacciNumber(number - 2) + tribonacciNumber(number - 3)


number = int(input('Enter the position : '))
print ('Tribonacci Number at position', number, 'is',tribonacciNumber(number))

'''
Sample Output
Enter the position : 10
Tribonacci Number at position 10 is 44

'''