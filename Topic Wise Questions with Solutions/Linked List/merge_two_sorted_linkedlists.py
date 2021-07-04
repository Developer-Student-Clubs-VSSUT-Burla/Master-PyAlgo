class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
  
    def insertnode(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            return
        
        last = self.head
        while last.next:
            last = last.next
  
        last.next = newnode

def mergeLists(headA, headB):
    dummyNode = Node(0)
    tail = dummyNode

    while True:
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
  

        tail = tail.next
    return dummyNode.next

       
       
        
listA = LinkedList()
listB = LinkedList()
# n = int(input('Enter the number of nodes in linked list '))
# print('Enter the values')
# for i in range(n):
#     x = int(input())
#     listA.insertnode(x)
# listA.printlist()

listA.insertnode(10)
listA.insertnode(12)
listA.insertnode(14)
listA.insertnode(15)
listA.insertnode(19)


listB.insertnode(9)
listB.insertnode(11)
listB.insertnode(12)
listB.insertnode(13)
listB.insertnode(21)

listA.head = mergeLists(listA.head, listB.head)
listA.printlist()

