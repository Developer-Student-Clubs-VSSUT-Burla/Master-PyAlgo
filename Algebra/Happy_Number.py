'''
    Starting with any positive integer, replace the number with the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle
    which does not include 1. Those numbers for which this process ends in 1 are happy number.
'''

'''
    Happy number- A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.
    Example- 13 is a happy number
    1^2+3^2=10
    1^2+0^2=1.
    It reaches to 1 hence It is a happy number.
'''

#Function check the happy number
def checkHappyNumber(n):
  #Loop for getting the sum of digits
    while(n != 1 and n != 4):    
        n = digitSum(n)
    if n==1:
        return True
    else:
        return False   

#Function return the sum of sqaure of digits
def digitSum(n):    
    digit = sum = 0
    #Calculating the sum of sqaure of digits
    while(n > 0):    
        digit = n % 10 
        sum = sum + (digit * digit)    
        n = n // 10   
    return sum    

#Driver code        
num = int(input("Enter a number: "))
if checkHappyNumber(num):
    print(f'{num} is a Happy Number')
else:
    print(f"{num} is not a Happy number")

'''
    Sample Input/Output:
    Enter a number: 19
    Output: 19 is a Happy number

    Enter a number: 24
    Output: 24 is not a Happy number
'''
