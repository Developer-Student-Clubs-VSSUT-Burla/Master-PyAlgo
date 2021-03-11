# Find the maximum and minimum value in the binary search tree
  # numbers= [19.45,67,34,7,56,42,6,87,11,12]

  # OUTPUT 
  # Minimum = 6
  # Maximum = 87


def max_val(self):

  if self.right is None:
    return self.data
  return self.right.max_val()


def min_val(self):
    if self.left is None:
        return self.left
    return self.left.min_val()

# Driver code for the following function 

numbers= [19.45,67,34,7,56,42,6,87,11,12]
print("Minimum:", numbers.min_val())
print("Maximum:", numbers.max_val())

# Remember: We need to build a tree first for using BST





  
       