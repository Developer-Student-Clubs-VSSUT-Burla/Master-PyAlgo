class Node:                                     #node creation
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:                               #intially node head is pointing to null
    def __init__(self):
        self.head = None

    def _reverse(self, previous, current):      #recursive call 
        if current is None:                     #if present node is null then head will point to previous node
            self.head = previous
        else:
            self._reverse(current, current.next)  #else it will call the function again and again until it reaches the termination condition
            current.next = previous

    def reverse(self):
        self._reverse(None, self.head)

    def insert(self, data):                         #pushing the data back inito linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def LLprint(self): #print the list 
        current = self.head
        reverselist = []
        while current:
            reverselist.append(current.data)         #appending the value to the list from backside
            current = current.next
        return reverselist
LL = linkedlist()
print("Enter the size of ll:  ")
n = int(input())
print("Enter the values of of Linked List: ")
for i in range(0,n):
    LL.insert(input())
print("The original Linked List is:")
print(LL.LLprint())
print("The reverse Linked List using iterative approach:")
LL.reverse()
print(LL.LLprint())


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
