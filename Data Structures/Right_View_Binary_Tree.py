'''
Given a binary tree, the task is to print its right view. Right view of
a binary tree is defined as the nodes which will be visible if the tree
is viewed from the right side. The input for the binary tree is in the
form of preorder and entering '-1' denotes a null node.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BuildTree():
    d = int(input())
    if d == -1:
        return None
    root = Node(d)
    root.left = BuildTree()
    root.right = BuildTree()
    return root


def RightView(root, level, maxlevel):
    # base case
    if root is None:
        return
    if level > maxlevel[0]:
        print(root.data, end=" ")
        maxlevel[0] = level
    RightView(root.right, level + 1, maxlevel)
    RightView(root.left, level + 1, maxlevel)


print("Enter values in a binary tree:")
root = BuildTree()
maxlevel = [-1]
print("Right view of the binary tree is:")
RightView(root, 0, maxlevel)

'''
Sample Output
Enter values in a binary tree:
2
4
7
8
-1
-1
-1
5
-1
-1
3
9
-1
6
-1
1
-1
-1
-1
Output:
Right view of the binary tree is:
2 3 9 6 1
'''
