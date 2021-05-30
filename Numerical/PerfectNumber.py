'''
A Perfect number is a number which is equal to the sum of all of its factors For example:6
    The number 6 has factors 1,2,3 and the sum results in the number6  so 6 is a perfect number
'''



def perfectnumber(number):
    #initializing total to 0
    total = 0
    for numbers in range(1, n):
        #condition to check whther the number is a factor of given number or not
        if(number % numbers == 0):
            #if it is a factor it is added to the sum
            total = total + numbers
    #if the total is equal to the number given it returns true
    #else returns false
    if (total == number):
        return 1
    else:
        return 0
        
        
n=int(input("Enter a number to check whether its perfect or not:"))
if(perfectnumber(n)):
    print("The given number is a perfect number")
elif(perfectnumber(n)==0):
    print("The given number is not a perfect number")

'''
Sample Output:
Enter a number to check whether its perfect or not:10
The given number is not a perfect number

Enter a number to check whether its perfect or not:6
The given number is a perfect number
'''
