"""

Time complexity : 0(n)
Space complexity : 0(1)

Sample Input/Output :
- Test case 1:
Enter the string : keys
Not a Palindrome
- Test case 2:
Enter the string : mom
Is a Palindrome
- Test case 3:
Enter the string : telephone
Not a Palindrome

"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    @staticmethod
    def print(node):

        '''Reversing the string'''
        rev_key = ""
        while node:
            rev_key += node.data
            node = node.next
        return rev_key

    def __init__(self):
        self.head = None

    def push(self, new_data):

        ''' Adding new node in the front of the list '''
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last
        return


if __name__ == "__main__":

    llist = DoublyLinkedList()
    keys = input("Enter the string : ")

    for i in reversed(range(len(keys))):
        llist.push(keys[i])

    rev_keys = llist.print(llist.head)

    if keys == rev_keys:
        print("Is Palindrome")
    else:
        print("Not a Palindrome")