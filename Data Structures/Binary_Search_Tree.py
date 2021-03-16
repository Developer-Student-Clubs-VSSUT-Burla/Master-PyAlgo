# A Tree is a hierarchial way of storing data

#A Binary Search Tree is a General Tree with a constraint that each node acting as a parent can have only 2 child nodes

# Things to remember for implemneting a Binary Search tree:
    # 1. The value of Left child node will always be smaller than the value of parent node
    # 2. The value of the right child node will always be greater than the value of parent node
    # 3. Elements are not duplicated in a Tree

class BinarySearchTree:
    def __init__(self,data):
     self.data=data
     self.left=None
     self.right=None        #creating the first node

    def add_child(self,child):   #adding tree
        if child==self.data:
            return              #since there are no duplicates in a tree

        if child<self.data:    # we will add the node to the left sub tree
            if self.left:      # what if there is already a left node?
                self.left.add_child(child)     #we recursively call add child function for the left sub-tree

            else:
                self.left=BinarySearchTree(child)       # else just add the left node

        if child>self.data:    #similarly we work for the right sub-tree
            if self.right:      # what if there is already a right node?
                self.right.add_child(child)     #we recursively call add child function for the right sub-tree

            else:
                self.right=BinarySearchTree(child)       # else just add the right node

    # Now there are three possible methods of traversing in a Tree:
    # The first element by default will act as the base node

    # 1. In order Traversal: We first travel the left sub tree, followed by the base node and finally the right sub-tree

    def in_order_traversal(self):
        elements=[]    # as we traverse we will be adding the elements to this empty list

        if self.left:        # visiting the left sub-tree
            elements += self.left.in_order_traversal()  

        elements.append(self.data)    # visiting the base node

        if self.right:               # visiting the right sub-tree
            elements += self.right.in_order_traversal()

        return elements  

    # 2. Pre order Traversal: We first traverse the base node followed by the left and right sub tree respectively

    def pre_order_traversal(self):
        elements=[]    # as we traverse we will be adding the elements to this empty list

        elements.append(self.data)    # visiting the base node

        if self.left:        # visiting the left sub-tree
            elements += self.left.in_order_traversal()  

        if self.right:               # visiting the right sub-tree
            elements += self.right.in_order_traversal()

        return elements

    # 3. Post Order Traversal: We first traverse the left sub-tree followed by the right sub-tree and finally by the base node

    def post_order_traversal(self):
        elements=[]    # as we traverse we will be adding the elements to this empty list

        if self.left:        # visiting the left sub-tree
            elements += self.left.in_order_traversal()  

        if self.right:               # visiting the right sub-tree
            elements += self.right.in_order_traversal()

        elements.append(self.data)    # visiting the base node

        return elements

        

    # Searching a key in the tree can be implemented in the following way:

    def Search(self, key):      #k key is the value we need to search
        if self.data==key:
            return self.data

        if key<self.data:
            if self.left:
                return self.left.Search(key)

            else:
                return False

        if key>self.data:
            if self.right:
                return self.right.Search(key)
            else:
                return False

        # Time complexity of Searching= O(logn)

def build_tree(elements):
    root=BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

# Driver code for the above:

if __name__=='__main__':

    numbers=[]

    n=int(input("Enter number of elements: "))

    print("Enter all the elements: ")
    for i in range(0,n):
        elements=int(input())

        numbers.append(elements)

    key=int(input("Enter number to be searched: "))
    
    numbers_tree=build_tree(numbers)

    print("In order: " ,numbers_tree.in_order_traversal())
    print("Pre order: " ,numbers_tree.pre_order_traversal())
    print("Post order: " ,numbers_tree.post_order_traversal())
    print(numbers_tree.Search(key))
