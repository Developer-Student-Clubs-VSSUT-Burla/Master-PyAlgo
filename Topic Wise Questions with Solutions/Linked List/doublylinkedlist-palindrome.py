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
    def display(node):

        '''Reversing the string'''
        rev_string = ""
        while node:
            rev_string += node.data
            node = node.next
        return rev_string

    def __init__(self):
        self.head = None

    def add(self, new_data):

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
    string = input("Enter the string : ")

    for i in reversed(range(len(string))):
        llist.add(string[i])

    rev_string = llist.display(llist.head)

    if string == rev_string:
        print("Is Palindrome")
    else:
        print("Not a Palindrome")
