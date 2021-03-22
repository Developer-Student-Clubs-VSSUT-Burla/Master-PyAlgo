class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:
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

    def LLprint(self):
        present = self.head
        while (present):
            print(present.data)
            present = present.next


def ireverse(list):
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
print("The original Linked List is:")
LL.insertion(0)
LL.insertion(2)
LL.insertion(4)
LL.insertion(6)
LL.LLprint()
print("The reverse Linked List using iterative approach:")
ireverse(LL)
LL.LLprint()
