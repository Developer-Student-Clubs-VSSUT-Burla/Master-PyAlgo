"""Stack is Last in last out data structure"""


class Stack:
    def __init__(self):
        """Create empty stack"""
        self.data = []

    def __len__(self):
        """return stack length"""
        return len(self.data)

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.data) == 0

    def push(self, x):
        """Push new element to stack"""
        self.data.append(x)

    def top(self):
        """
        Get the last element in stack
        if stack is empty print stack is empty
        """
        if self.is_empty():
            print("Stack is empty.")
        else:
            return self.data[-1]

    def pop(self):
        """
        remove the last element in stack and save it
        if stack is empty print stack is empty
        """
        if self.is_empty():
            print("Stack is empty.")
        else:
            return self.data.pop()
