"""
python program to print initials of a name.

approach: Using Python in inbuilt functions we can split the words into a list, 
then traverse till the second last word and print the first character in capitals 
using upper() function in python and then add the last word 
using title() function in Python which automatically converts 
the first alphabet to capital.

In-build functions or methods used-
len is used to get the length of the name
.split() is used to split the words into a list
.upper() is used to convert all the letters in uppercase
.title() is to print first character in capital
"""
def name(n):
    
    # split the string into a list  
    l = s.split()
    new = "" 
   
    # traverse in the list
    for i in range(len(l)-1):
        s = l[i]
        
        # adds the capital first character
        new += (s[0].upper()+'.')
    
    # adds the capital first character l[-1] gives last item of list l. 
    new += l[-1].title() # title function to print first character in capital.      
    return new      
n=input("Enter full name: ")
print(name(n))
"""        
Average Time complexity: O(pattern length + text length)
Space complexity: O(1) 

#SAMPLE 1-
INPUT-
Enter full name: pilavullakandi thekkeparambil usha
OUTPUT-
P.T.Usha
#SAMPLE 2-
INPUT-
Enter full name: chandrasekhara venkata raman
OUTPUT-
C.V.Raman
"""