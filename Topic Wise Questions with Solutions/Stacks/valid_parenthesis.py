'''
Question Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

def isValid(self, s: str) -> bool:
    d = {'(':')', '{':'}','[':']'}        
    stack = []
    for i in s:
        if i in d:  
            stack.append(i)
        elif len(stack) == 0 or d[stack[-1]] != i:  
            return False
        else:
            stack.pop()
    return len(stack) == 0

s = input()
print(isValid(s))

'''
Sample Input 1:
s = "()[]{}"
output = True

Sample Input 2:
s = "([)]"
output = False
'''