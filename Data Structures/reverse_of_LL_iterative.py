class Node:                                           #creating a node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:                                      #creating a linked list
    def __init__(self):
        self.head = None

    def insertion(self, data):
        node1 = Node(data)
        if (self.head):
            present = self.head
            while (present.next):
                present = present.next
            present.next = node1
        else:
            self.head = node1

    def LLprint(self):                                      #printing the linked list
        present = self.head
        while (present):
            print(present.data)
            present = present.next


def ireverse(list):                                       # reversing the linked list
    prev = None
    present = list.head
    nextnode = present.next

    while (present):
        present.next = prev
        prev = present
        present = nextnode
        if nextnode:
            nextnode = nextnode.next
    list.head = prev

LL = linkedlist()
LL.insertion(0)
LL.insertion(1)
LL.insertion(2)
print("The original Linked List is:")
LL.LLprint()
print("The reverse Linked List using iterative approach:")
ireverse(LL)
LL.LLprint()

LL = linkedlist()
LL.insertion(10)
LL.insertion(32)
LL.insertion(12)
LL.insertion(34)
LL.insertion(56)
print("The original Linked List is:")
LL.LLprint()
print("The reverse Linked List using iterative approach:")
ireverse(LL)
LL.LLprint()

"""
enter n value = 3
enter values  = 0 1 2 
original ll = 0 1 2
reversed = 2 1 0

enter n value = 5
enter values  = 10 32 12 34 56
original ll = 10 32 12 34 56
reversed = 56 34 12 32 10

"""
