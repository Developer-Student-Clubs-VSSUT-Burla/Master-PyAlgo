'''
Aim: For the given integer 'n', print 'i^2' such that 'i' is a non-negative 
integer less than 'n'.

'''

# getting the integer input
n = int(input().strip())

# loop for going through all non-negative integers less than n
for i in range(0,n):
    # calculating the square
    print(i*i)
    
'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(N)
     
Sample Input:
5

Sample Output:
0
1
4
9
16

Explanation:
Non-negative integers less than 5 --> 0, 1, 2, 3, 4
Their squares --> 0, 1, 4, 9, 16

'''