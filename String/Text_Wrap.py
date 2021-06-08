'''
Aim: Given a string 's' and width 'w', the task is to wrap the string into a 
paragraph of width 'w'.

'''

def wrap(string, max_width):
    # printing the string as a paragraph
    print("\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)]))

s = input('Enter string: ')
w = int(input('Enter max width: '))
wrap(s,w)

'''

COMPLEXITY:
	
	 Time Complexity -> O(1)
	 Space Complexity -> O(1)
     
Sample Input:
Enter string: yuhqwiudhvcgycxfsag
Enter max width: 3

Sample Output:
yuh
qwi
udh
vcg
ycx
fsa
g

Explanation:
At every third character in the string, slicing takes place and the rest of 
the string is getting printed in a newline.

'''