'''
In a circular Singly linked list, the last node of the list contains a pointer to the first node of the list.
The circular singly liked list has no beginning and no ending.
There is no null value present in the next part of any of the nodes.
'''

class node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)


class circular_linked_list:
    def __init__(self, head=None):
        self.head = head

    def pretty_print(self):

        cir_list_str = ''

        current_node = self.head

        while current_node:
            cir_list_str += '-({0:1d})-'.format(current_node.key)
            current_node = current_node.next
            if current_node == self.head:
                break

        return cir_list_str

    def append(self, key):
        new_node = node(key)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node = self.head
        
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = new_node
            new_node.next = self.head

   
    def prepend(self, key):
        new_node = node(key)

        
        current_node = self.head
        new_node.next = self.head

        
        if self.head is None:
            new_node.next = new_node
        else:
            
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = new_node

        self.head = new_node

    
    def insert_after_node(self, afterkey, key):
        current_node = self.head
        while current_node:

            if current_node.next == self.head and current_node.key == afterkey:
                
                self.append(key)
                return
            elif current_node.key == afterkey:
                new_node = node(key)
                next_node = current_node.next

                
                current_node.next = new_node
                new_node.next = next_node

                return
            else:
                if current_node.next == self.head:
                    break
            current_node = current_node.next

    def delete(self, deletekey):
        current_node = self.head
        prev_node = None
        while current_node:

            
            if current_node.key == deletekey and current_node == self.head:

                
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return

                else:
                    while current_node.next != self.head:
                        current_node = current_node.next
                    current_node.next = self.head.next
                    self.head = self.head.next
                    current_node = None
                    return

            elif current_node.key == deletekey:
                prev_node.next = current_node.next
                current_node = None
                return

            else:
                if current_node.next == self.head:
                    break

            prev_node = current_node
            current_node = current_node.next


if __name__ == "__main__":

    cir_list = circular_linked_list()

    data = [5, 8, 10, 12]

    for value in data:
        cir_list.append(value)

    print('\n----- Insert Operations ----- ')

    print('\nCircular linked list elements using append --->',cir_list.pretty_print())

    cir_list1 = circular_linked_list()

    cir_list1.prepend(4)

    print('\nPrepend on empty list  ---> ', cir_list1.pretty_print())

    cir_list1.prepend(0)

    print('\nPrepend on an existing list  ---> ', cir_list1.pretty_print())

    cir_list2 = circular_linked_list()
    cir_list2.append(17)

    print('\nAppend on empty list  ---> ', cir_list2.pretty_print())

    cir_list2.insert_after_node(17, 20)

    print('\nInserting 20 after 17 - Append   ---> ', cir_list2.pretty_print())

    cir_list2.insert_after_node(17, 18)

    cir_list2.insert_after_node(18, 19)
    print('\nInserting 19 after 18  ---> ', cir_list2.pretty_print())

    print('\n----- Delete Operations ----- ')

    del_cir_list0 = circular_linked_list()
    del_cir_list0.append(77)

    print('\nSingle element circular linked list before deletion --->',
          del_cir_list0.pretty_print())

    del_cir_list0.delete(77)

    print('\nNo linked list present after deleting only node  --->',
          del_cir_list0.pretty_print())

    del_cir_list = circular_linked_list()
    del_cir_list.append(16)
    del_cir_list.prepend(11)
    del_cir_list.insert_after_node(11, 19)
    del_cir_list.prepend(9)
    del_cir_list.append(22)
    del_cir_list.prepend(5)


    print('\nCircular linked list before deletion --->',
          del_cir_list.pretty_print())

    del_cir_list.delete(5)


    print('\nCircular linked list after deletion of head--->',
          del_cir_list.pretty_print())


    del_cir_list.delete(19)
    print('\nList after deletion of in between node 19 --->',
          del_cir_list.pretty_print())


    del_cir_list.delete(22)
    print('\nList after deletion of last node 22 --->',
          del_cir_list.pretty_print())


    del_cir_list.delete(88)
    print('\nNo change in circular linked list when trying to delete non existing key',
          del_cir_list.pretty_print())

'''
Sample Output
----- Insert Operations ----- 

Circular linked list elements using append ---> -(5)--(8)--(10)--(12)-

Prepend on empty list  --->  -(4)-

Prepend on an existing list  --->  -(0)--(4)-

Append on empty list  --->  -(17)-

Inserting 20 after 17 - Append   --->  -(17)--(20)-

Inserting 19 after 18  --->  -(17)--(18)--(19)--(20)-

----- Delete Operations ----- 
Single element circular linked list before deletion ---> -(77)-

No linked list present after deleting only node  ---> 

Circular linked list before deletion ---> -(5)--(9)--(11)--(19)--(16)--(22)-

Circular linked list after deletion of head---> -(9)--(11)--(19)--(16)--(22)-

List after deletion of in between node 19 ---> -(9)--(11)--(16)--(22)-

List after deletion of last node 22 ---> -(9)--(11)--(16)-

No change in circular linked list when trying to delete non existing key -(9)--(11)--(16)-

'''

