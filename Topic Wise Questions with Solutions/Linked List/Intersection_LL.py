

# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'



# Definition for Singly Linked-List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution class 
class Solution:
    # Method for getting node at which intersection has started
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
	# Assign a pointer to head of Lists
        curA,curB = headA,headB  
	
	# Initially lenght is zero
        lenA,lenB = 0,0

	# Iterate Till the end point of LL using pointer A
        while curA is not None:
            lenA += 1
            curA = curA.next

	#Iterate Till the end point of LL using pointer B
        while curB is not None:
            lenB += 1
            curB = curB.next
	

	# Move pointers back to head
        curA,curB = headA,headB

	# if lenA is greater then move curA to intersection point
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next

	# if lenB is greater then move curB to intersection point
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next

	# if they are not at same point then move them till the are pointing at same node
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA


        