#Given a string of lowercase ASCII characters, find all distinct continuous palindromic sub-strings of it.

def DistinctPalindromeSubStrs(st): 
	w = dict() 
	stringlen = len(st) 

	# table for storing results (2 rows for odd- and even-length palindromes 
	R = [[0 for x in range(stringlen+1)] for x in range(2)] 

	# Find all sub-string palindromes from the given input string insert 'guards' to iterate easily over s 
	st = "@" + st + "#"

	for j in range(2): 
		rp = 0 # length of 'palindrome radius' 
		R[j][0] = 0

		i = 1
		while i <= stringlen: 

			# Attempt to expand palindrome centered at i 
			while st[i - rp - 1] == st[i + j + rp]: 
				rp += 1     # Incrementing the length of palindromic radius as and when we find valid palindrome 

			# Assigning the found palindromic length to odd/even length array 
			R[j][i] = rp 
			k = 1
			while (R[j][i - k] != rp - k) and (k < rp): 
				R[j][i+k] = min(R[j][i-k], rp - k) 
				k += 1
			rp = max(rp - k, 0) 
			i += k 

	# remove guards 
	st = st[1:len(st)-1] 

	# Put all obtained palindromes in a hash map to find only distinct palindrome 
	w[st[0]] = 1
	for i in range(1,stringlen): 
		for j in range(2): 
			for rp in range(R[j][i],0,-1): 
				w[st[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
		w[st[i]] = 1

	# printing all distinct palindromes from hash map 
	print ("Below are " + str(len(w)) + " palindromic sub-strings")
	for k in w: 
		print (k) 

s = input("Enter string ")		
DistinctPalindromeSubStrs(s) 

''''
Input: str = "abaaa"

Output:  Below are 5 palindromic sub-strings
a
aa
aaa
aba
b
'''
