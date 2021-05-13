'''
A special number is a number is the sum of factorial 
of digits is equal to the number itself
Example-145 is a special number as 145=1!+4!+5!
'''

def special(a):
    sum=0
    t=a
    while(a>0):
        b=a%10
        f=1
		#Calculating Factorial of each digit
        for i in range(1,b+1):
            f=f*i
		#Sum of the factorial of digits
        sum=sum+f
        a=a//10
	#Checking if the number is equal or not
    if sum==t:
        return 1
    else:
        return 0

#Driver's Code
def main():
    n=int(input("Enter a number to check special or not\n"))
    s=special(n)
    if s==1:
        print("It is a special number")
    else:
        print("It is not a special number")
if __name__=="__main__":
    main()

'''
Time Complexity:O(n)
Space Complexity:O(1)

Input/Output:
Enter a number to check special or not 145
It is a special number
'''


