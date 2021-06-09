'''
Aim: The task is to sort the string S in the following manner:

1. All sorted lowercase letters are ahead of uppercase letters.
2. All sorted uppercase letters are ahead of digits.
3. All sorted odd digits are ahead of sorted even digits.

'''

# initializing empty lists for separating out lowercase letters, uppercase 
# letters, odd numbers and even numbers.
l,u,o,e=[],[],[],[]
for i in sorted(input()):
    # checking case of letters and sorting accordingly
    if i.isalpha():
        x = u if i.isupper() else l
    # Checking for even/odd numbers
    else:
        x = o if int(i)%2 else e
    x.append(i)
# joining all the lists according to the 3 conditions
print("".join(l+u+o+e))

'''

COMPLEXITY:
	
     Time Complexity -> O(N)
	 Space Complexity -> O(N)
     
Sample Input:
Sorting1234

Sample Output:
ginortS1324

Explanation:
First, according to condition 1, all letters in lowercase are printed in 
sorted form. Then, the uppercase letters are printed according to condition
2. At last, numbers are printed as per condition 3, first odd and then even
digits.

'''