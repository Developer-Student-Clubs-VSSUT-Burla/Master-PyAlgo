'''
Aim: To swap cases of all the characters in the entered string.

'''

def swap_case(s):
    l=[]
    ln=[]
    for i in s:
        l.append(i)
    for i in l:
        # if the case is lower, then it should be converted into upper case
        if i.lower()==i:
            ln.append(i.upper())
        # if the case is upper, then it should be converted into lower case
        elif i.upper()==i:
            ln.append(i.lower())  
    str1 = ""    
    # concatenating the elements of the list and recreating the string
    for ele in ln:  
        str1 += ele  
    # printing the result    
    print(str1)

# getting the input
s = input().strip()
# calling the function for doing the computations
swap_case(s)

'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(N)
     
Sample Input:
GooD DaY

Sample Output:
gOOd dAy

Explanation:
All the characters which were in upper case have been swapped with their lower 
case ones and vice-versa.

'''