"""
Remove Element
Given a linked list nums and a value val, remove all instances of that value in-place and return the new linked list.
Do not allocate extra space for another linked list, you must do this by modifying the input linked list in-place with O(1) extra memory.
Input: 3 -> 2 -> 2 -> 3
Output: 2 -> 2
Input: 0 -> 1 -> 2 -> 2 -> 3 -> 0 -> 4 -> 2
Output: 0 -> 1 -> 3 -> 0 -> 4
Iterate the linked list and jump the values that needs to be deleted (change the next pointer).
    Time Complexity:    O(N)
    Space Complexity:   O(1)

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100


"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count

"""
EXAMPLE : 1

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

"""