#Happy number function to determine whether it is a happy number or not

def HappyNumber(number):    
    sum = 0;    
    #Calculates the sum of squares of digits    
    while(number > 0):    
        sum+=((number%10)*(number%10))
        number = number//10;    
    return sum;    
        
number =int(input("Enter a number:"))    
final_result=number 

#The while loop runs to check whether the result obtained is either 4 or 1

while(final_result != 1 and final_result != 4):    
    final_result = HappyNumber(final_result);    
     
#The happy number ends with 1 otherwise it is not a happy number

if(final_result == 1):    
    print("The given number is a happy number");    
else:    
    print( "The given number is not a happy number");  
