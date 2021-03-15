# Memoization in Fibonacci: Storing the result of the function called (fibonacci numbers already calculated) to utilize them again 
# Avoids excessive function calls

#Declaring a global list for storing fibonacci numbers
global F
F=[]
for i in range(20):
    F.append(-1)     # List initialized with all elements as -1

# Function to calculate fibonacci number at index/position 'n'
def get_fibonacci(n):
    if (n <= 1):        # Base condition 
        F[n] = n
        return n
    
    else:
        if(F[n-1] == -1):
            F[n-1] = get_fibonacci(n-1)  #Storing values on function calls
        
        if(F[n-2] ==- 1):
            F[n-2] = get_fibonacci(n-2)  #Storing values on function calls

        F[n] = F[n-1] + F[n-2]          #Calculating fibonacci number at 'n'
        return F[n]

#main
if __name__=="__main__":
    
    num = int(input("Enter Number: "))
    fib = get_fibonacci(num)              #Function call
    print("The fibonacci number is",fib) 
       

#Sample Case
#num=8
#output:21

#Time Complexity-: O(n)