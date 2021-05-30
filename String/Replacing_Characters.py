'''
Aim: To replace a character at a particular position in the string by the 
character entered by the user.

'''

def mutate_string(string, position, character):
    # the string is being sliced and put up again in order to insert the new character
    string = string[:position] + character + string[position+1:]
    print('\nUpdated string:',string)

# getting necessary details
s = input('Enter string: ')
char = input('Enter new character: ')
pos = input('Enter position where you want to place it: ')
# calling function to display the results
mutate_string(s.strip(), int(pos), char)

'''

COMPLEXITY:
	
	 Time Complexity -> O(1)
	 Space Complexity -> O(1)
     
Sample Input:
Enter string: Simon Bakar
Enter new character: e
Enter position where you want to place it: 9

Sample Output:
Updated string: Simon Baker

Explanation:
Character 'a' which was at position 9 in the entered string, got replaced by 
the character 'e' that was entered by user.

'''