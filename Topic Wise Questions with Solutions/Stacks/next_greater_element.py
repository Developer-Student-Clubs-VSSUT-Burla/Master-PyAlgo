'''
Question Statement: 
You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
If it does not exist, return -1 for this number.
'''
def nextGreaterElement(nums1, nums2):
    nextGreater = {}
    stack = []
    for v in nums2:
        while stack and stack[-1] < v:
            nextGreater[stack.pop()] = v
        stack.append(v)
    
    ans = []
    
    for i in nums1:
        if i in nextGreater:
            ans.append(nextGreater[i])
        else:
            ans.append(-1)
    return ans

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(nextGreaterElement(nums1, nums2))

'''
Sample input:
nums1 = 4 1 2
nums2 = 1 3 4 2

Output = [-1, 3, -1]
'''

