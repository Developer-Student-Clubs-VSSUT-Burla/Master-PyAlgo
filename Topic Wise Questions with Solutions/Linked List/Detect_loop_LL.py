'''
Given a linked list of N nodes. 
Check if the linked list has a loop. 
'''

class Node:
    # initializing the Node
     def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    # Initializing the LinkedList
    def __init__(self):
        self.head = None
 

    # To insert a node at the last position (Pushing)
    def insert_at_end(self, new_data):
        # If the linked list is empty
        if self.head is None:
            self.head = Node(new_data)

        # Adding the new node at the end of the linked list
        else:
            new_node = Node(new_data)
            current = self.head

            # Traversing the linked list till we reach the last node
            while current.next:
                current = current.next

            current.next = new_node


    def last_node(self):
        current = self.head

        while current.next:
            current = current.next

        return current     

    
    # Function to create loop in linked list
    def create_loop(self, position):
        # Variable to traverse 
        current = self.head

        # Traversing to the node
        if position >= 0:
            while position > 0:
                current = current.next
                position -= 1

            # assigning the given position node to last node
            last = self.last_node()
            last.next = current
 

    # Function to detect loop in linked list  
    def detect_loop(self):
        # Initializing pointers at head of linked list

        # traverses one node at a time
        one_step_p = self.head

        # traverses two nodes at a time
        two_step_p = self.head

        # Traversing till the two_step_p doesnt't approach the end of linked list
        while (two_step_p.next and two_step_p.next.next):
            one_step_p = one_step_p.next
            two_step_p = two_step_p.next.next

            # if both pointers become equal, indicating the presence of a loop
            if one_step_p == two_step_p:
                return 1

        return 0
 

if __name__ == '__main__':

    # Creating a linked list instance
    ll_obj = LinkedList()

    # Pushing elements to the Linked List
    n = int(input('Enter length of Linked List: '))
    for i in range (n):
        ele = int(input(f'Enter element {i+1}: '))
        ll_obj.insert_at_end(ele)
    
    # Creating a loop within the Linked List
    pos = int(input('Enter position from where you want to loop the Linked list or Enter -1: '))
    ll_obj.create_loop(pos)

    if(ll_obj.detect_loop()):
        print('Found Loop')
    else:
        print('No Loop')


'''
    For detect loop function:
        Time Complexity: O(N).
        Space Complexity: O(1).

    Sample I/O:
    Enter length of Linked List: 4
    Enter element 1: 1
    Enter element 2: 8
    Enter element 3: 3
    Enter element 4: 4
    Enter position from where you want to loop the Linked list or Enter -1: 2
    Found Loop

    Here, node at 4th position is looped back to the 2nd position)
    1 -> 8 -> 3 -> 4     
         |_ _ _ _ _|
'''

