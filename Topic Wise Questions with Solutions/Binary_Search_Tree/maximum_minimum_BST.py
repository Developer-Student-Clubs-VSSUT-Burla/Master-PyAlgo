# Find the maximum and minimum element in a given array using Binary Search Tree


  # Sample input = [19.45,67,34,7,56,42,6,87,11,12]


class BinarySearchTree:
    def __init__(self,data):
     self.data=data
     self.left=None
     self.right=None        

    def add_child(self,child):   
        if child==self.data:
            return              

        if child<self.data:    
            if self.left:      
                self.left.add_child(child)     

            else:
                self.left=BinarySearchTree(child)      

        if child>self.data:    
            if self.right:      
                self.right.add_child(child)     

            else:
                self.right=BinarySearchTree(child)      

 # CODE FOR FINDING THE MAXIMUM & MINIMUM VALUE IN A BINARY TREE:

 # Here we will be using the recursion approach for finding the max element
    def max_val(self):
        if self.right is None:   # the utmost right element will be the maximum by the property of Binary Tree
            return self.data
        return self.right.max_val()
 
    def min_val(self):
        if self.left is None:   # the utmost left element will be the minimum by the property of Binary Tree
            return self.data
        return self.left.min_val()

def build_tree(elements):
    root=BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

# Driver code for the following function 
if __name__=='__main__':

    numbers=[]

    n=int(input("Enter number of elements: "))

    print("Enter all the elements: ")
    for i in range(0,n):
        elements=int(input())

        numbers.append(elements)

    number_tree=build_tree(numbers)

    print("Minimum:", number_tree.min_val())
    print("Maximum:", number_tree.max_val())

  # SAMPLE OUTPUT 
  # Minimum = 6
  # Maximum = 87



