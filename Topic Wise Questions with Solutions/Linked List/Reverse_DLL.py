
# Sample Output:

# Original List: 9 —> 8 —> 7 —> 6 —> 5 —> 4 —> 3 —> 2 —> 1 —> None
# Reversed List: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> 8 —> 9 —> None

# Original List: 4 —> 3 —> 2 —> 1 —> None
# Reversed List: 1 —> 2 —> 3 —> 4 —> None



# A Doubly Linked List Node Class
class Node:
    next = prev = None
 
    def __init__(self, data):
        self.data = data
 
 
# function to push a node at the beginning of the doubly linked list
def push(head, key):
 
    node = Node(key)
    node.next = head
 
    # change `prev` of the existing head node to point to the new node
    if head:
        head.prev = node
 
    # update head and return
    head = node
    return head
 
 
# function to print nodes of a doubly linked list
def printDDL(msg, head):
 
    print(msg, end='')
    while head:
        print(head.data, end=" —> ")
        head = head.next
    print("None")
 
 
# Function to swap `next` and `prev` pointers of the given node
def swap(node):
 
    prev = node.prev
    node.prev = node.next
    node.next = prev
 
 
# Recursive function to reverse a doubly-linked list
def reverse(head, curr):
 
    # last node
    if curr.next is None:
        # swap `next` and `prev` pointers for the current node
        swap(curr)
 
        # update head
        head = curr
        return head
 
    # swap `next` and `prev` pointers for the current node
    swap(curr)
 
    # recur with the next node
    head = reverse(head, curr.prev)
    return head
 
 
# Function to reverse a doubly-linked list
def reverseDDL(head):
 
    # stores the previous node and the current node
    curr = head
 
    # pass current and previous node information in the recursion itself
    head = reverse(head, curr)
    return head
 
 
if __name__ == '__main__':
 
    head = None
    for key in range(1, 10):
        head = push(head, key)
 
    printDDL("Original List: ", head)
    head = reverseDDL(head)
    printDDL("Reversed List: ", head)
 