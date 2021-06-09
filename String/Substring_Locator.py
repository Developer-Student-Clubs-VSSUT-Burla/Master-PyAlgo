'''
Aim: To locate the position of the entered substring in the main string and output the result.

'''

def count_substring(string, sub_string):
    # for each slice of the main string, if substring is found, keeping on adding 1 for the final position
    print(sum([i for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string]))

# getting the input
string = input('Enter main string: ')
sub_string = input('Enter sub-string to be found: ')
# calling the function to compute the results
count_substring(string, sub_string)

'''

COMPLEXITY:
	
	 Time Complexity -> O(1)
	 Space Complexity -> O(1)
     
Sample Input:
Enter main string: ABCDE
Enter sub-string to be found: CD

Sample Output:
2

Explanation:
According to indexing:    
0 1 2 3 4 
A B C D E
CD substring starts from position 2, so the output is 2.

'''