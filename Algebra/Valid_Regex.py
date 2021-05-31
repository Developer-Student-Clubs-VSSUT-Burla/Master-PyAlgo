'''
Aim: Given a string S. The task is to find out whether S is a valid regex or not.

A RegEx, or Regular Expression, is a sequence of characters that forms a search 
pattern. RegEx can be used to check if a string contains the specified search pattern.

'''

# importing module
import re

def isvalidregex(regex):
    # if the expression is valid then try block gets executed
    try: re.compile(regex)
    # if there is an error in it, then except block gets executed and 'False' gets printed
    except re.error: return False
    # if no error is encounted, 'True' gets printed
    return True

# loop for taking the input and calling the function for checking the expression
for i in range(int(input())):
    print(isvalidregex(input()))
    
'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(1)
     
Sample Input:
2
.*\+
.*+

Sample Output:
True
False

Explanation:
.*\+ --> Valid regex.
.*+ --> Has the error multiple repeat. Hence, it is invalid.

'''