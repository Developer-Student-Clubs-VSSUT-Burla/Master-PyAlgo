'''
Aim: Given two integers n and p, the goal is to output n^p if and only if n 
and p both are positive integers, else, print 'n and p should be non-negative'.

'''

# class to compute the valid results
class Calculator:
    def power(self,n,p):
        if n>=0 and p>=0:
            return(n**p)
        else:
            return('n and p should be non-negative')
# creating an object of class
myCalculator=Calculator()
# getting input
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        # if power calculation is possible then this block will be executed
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        # if power calculation is not possible then this block will be executed
        print(e)
        
'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(1)
     
Sample Input 1:
1
-1 3
Sample Output 1:
n and p should be non-negative

Sample Input 2:
1
4 5
Sample Output 2:
1024

Explaination:
The necessary condition in the 1st test case is not satisfied, hence 'n and p 
should be non-negative' is printed. Whereas in the 2nd test case both n and p 
are positive, so n^p i.e., 4^5 = 1024 is printed.

'''