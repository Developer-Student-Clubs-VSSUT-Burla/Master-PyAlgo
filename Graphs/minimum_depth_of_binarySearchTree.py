""" utility that allocates a newNode 
with the given val """
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
'''
inserting the nodes (according to the rules of binary search tree)
'''
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
'''
getting the minimum depth of binary search tree
'''
def minDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return minDepth(root.right)+1
    if root.right is None:
        return minDepth(root.left) +1
    return min(minDepth(root.left), minDepth(root.right))+1
'''
driver code
'''
def main():
    print("how many nodes to be inserted")
    n=int(input())
    no_of_nodes=n
    i=1
    list_of_nodes=[]
    print("enter the nodes to be inserted to binary tree")
    while(n):
        list_of_nodes.append(int(input()))
        n-=1
    root = Node(list_of_nodes[0])
    while(i<=no_of_nodes-1):
        root=insert(root,list_of_nodes[i])
        i+=1
    print("Minimum depth of the binary search tree is")
    print(minDepth(root)-1)
 
main()
'''
Sample I/O and O/P for the binary tree

        10
       /  \
      3    14
     / \
    1   5
   /
  0
how many nodes to be inserted
6
enter the nodes to be inserted to binary tree
10
14
3
5
1
0
Minimum depth of the binary search tree is
1

Time complexity is given by O(n) where n is no of nodes
Space complexity i sgiven by O(h) where h is height of the tree
'''
