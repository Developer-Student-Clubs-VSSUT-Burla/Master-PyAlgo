'''
Question Statement:
Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.
'''

from collections import defaultdict

def removeDuplicateLetters(s):
    frequency = defaultdict(int)
    for i in s:
        frequency[i] += 1
        
    stack = []
    ans = ""
    for i in s:
        if i in stack:
            frequency[i] -= 1
            continue
        if len(stack) == 0:
            stack.append(i)
            frequency[i] -= 1
        else:
            while (len(stack) != 0 and i < stack[-1]):
                if frequency[stack[-1]] > 0:
                    stack.pop()
                else:
                    break        
            stack.append(i)
            frequency[i] -= 1
       
    return "".join(i for i in stack)

s = input()
print(removeDuplicateLetters(s))

'''
Sample Input 1:
s = "bcabc"
Output = "abc"

Sample Input 2:
s = "cbacdcbc"
Output = "acdb"

'''