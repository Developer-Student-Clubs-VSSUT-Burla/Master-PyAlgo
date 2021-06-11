'''
Aim: Remove duplicate nodes from the linked list.

'''

# initializing empty list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
class Solution: 
    # function for inserting values
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    # function to display the linked list    
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    # function from removing duplicate values from the linked list
    def removeDuplicates(self,head):
        qu = []
        if head == None:
            return 
        p = head
        qu.append(p.data)
        p = p.next
        while p is not None:
            qu.append(p.data)
            p = p.next
        qu = list(dict.fromkeys(qu))
        for item in qu:
            print(item,end=' ')

# creating an object of the class            
mylist= Solution()
# getting the input
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)   
# calling function for removing the duplicate elements    
head=mylist.removeDuplicates(head)
# printing the results
mylist.display(head)

'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(N)
     
Sample Input:
6
1
2
2
3
3
4
Sample Output:
1 2 3 4

Explaination:
All the unique elements got entered in the 'qu' list under 'removeDuplicates' function.
So, the output comes out to be --> 1 2 3 4

'''