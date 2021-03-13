# Given a string s, return the longest palindromic substring in s.

# longestPalindrome function
class String(object):
    def longestPalindrome(self, s):
        res = ""
        for itr in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, itr, itr)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, itr, itr+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    # get the longest palindrome, 
    # left, right are the middle indexes   
    # from inner to outer
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1; right += 1
        return s[left+1:right]

inp = input("Enter the string: ")
obj = String()
print("Longest Palindromic substring is: " + obj.longestPalindrome(inp))

# TIME COMPLEXITY : O(N)

# Enter the string: wonderwow
# Longest Palindromic substring is: wow

# Enter the string: AABBCDEGGGAAHHUHHB
# Longest Palindromic substring is: HHUHH
