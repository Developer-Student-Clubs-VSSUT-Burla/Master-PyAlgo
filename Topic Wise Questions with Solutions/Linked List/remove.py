"""
Remove Element
Given a linked list nums and a value val, remove all instances of that value in-place and return the new linked list.
Do not allocate extra space for another linked list, you must do this by modifying the input linked list in-place with O(1) extra memory.
Iterate the linked list and jump the values that needs to be deleted (change the next pointer).
    Time Complexity:    O(N)
    Space Complexity:   O(1)

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100


"""
print(" Enter the values for nums to store in an linkedist :")
nums=list(map(int,input().split()))
print("Enter the value of val to delete :")
val=int(input())

class Solution:
    def removeElement(self, nums: list , val: int) -> int:
        a=nums.count(val)
        i=1
        while i <=a:
            nums.remove(val)
            i+=1
        print(nums)
        
        
s = Solution()
s.removeElement(nums, val) 

"""
EXAMPLE : 1

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

"""
