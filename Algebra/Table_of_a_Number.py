'''
Aim: The aim is to print the first 10 multiples of the number entered.

'''

# getting the input
n = int(input().strip())      

# looping from 1 to 11 because we want first 10 multiples only
for i in range(1,11):          
    # printing the table for the number
    print(str(n) + ' x ' + str(i) + ' = ' + str(n*i))  
    
'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(1)
     
Sample Input:
4

Sample Output:
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

Explanation:
Any random iteration(like the 5th one) would look like this--> str(4) + 'x' + str(5) + '=' + str(4*5) 
Hence, the output will be--> 4 x 5 = 20
In a similar manner, all the lines are printed.

'''