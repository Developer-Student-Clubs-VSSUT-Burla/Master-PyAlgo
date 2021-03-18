# Python Program for Z Algorithm to find the occurrence of a pattern in a string in linear time

# Given string
T = "abababab"

# Pattern to be found
P = "aba"

# concatenating pattern and text to create a string P$T where $ is a special character not present in text or pattern
S = P+"$"+T

# maintain an interval [L,R] which is the interval with maximum R such that  and  is a prefix-substring 
L = 0
R = 0

# variable to count number of times pattern occurs 
count = 0 

# n is length of string S
n = len(S)

# Declaring Z array having length same as that of S
Z = [None] * len(S)

#Compute Z array  and the new [L,R] by the following steps:
for i in range(1,n):

# the current position is outside of what we have processed.
    if i > R :
    	L,R = i,i
    	while ( R < n and S[R-L] == S[R]):
    		R = R+1
    	Z[i] = R-L
    	R = R-1

#the current position is inside the current segment match [L,R]
    else:
    	k = i-L
    	if Z[k] < R-i+1 :
    		Z[i] = Z[k]
    	else:
    		L = i
    		while ( R < n and S[R-L] == S[R]):
    			R = R+1
    		Z[i] = R-L
    		R = R-1
    		
# Pattern occurs at index where Z[i] i.e., the Z value is equal to length of pattern
    if (Z[i] == len(P)):
          count = count +1
          print("Pattern found at index ",i - len(P) -1) 
          
# To print number of times pattern occurs in string if it exists         
if(count>0):
    print("Number of times Pattern occurs in string: ",count);
else:
    print("Pattern does not exist in string")

   
