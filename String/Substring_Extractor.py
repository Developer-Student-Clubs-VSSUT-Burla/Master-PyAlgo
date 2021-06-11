'''
Aim: Consider a database table, Emails, which has the attributes First Name 
and Email ID. Given N rows of data simulating the Emails table, print an 
alphabetically-ordered list of people whose email address ends in '@gmail.com'.

'''

# getting the total test cases as input
N = int(input())

l = []
# loop for going through the complete string and extracting the desired substring
for N_itr in range(N):
    firstNameEmailID = input().split()
    firstName = firstNameEmailID[0] 
    emailID = firstNameEmailID[1]
    
    # checking for substring
    if '@gmail.com' in emailID:
        l.append(firstName)
    
    # printing out names of people with 'gmail' account
    l = sorted(l)
    for i in l:
        print(i)
        
'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(1)
     
Sample Input:
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
julia julia@gmail.com

Sample Output:
julia
julia
riya
samantha
tanya

Explanation:
Only the names of people having the substring '@gmail.com' in their mail ids 
are printed.

'''