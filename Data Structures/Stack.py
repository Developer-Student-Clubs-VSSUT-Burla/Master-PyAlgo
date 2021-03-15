"""Stack is Last in First out data structure"""


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
            raise Exception("topping from an empty stack")
        return self.data[-1]

    def pop(self):
        """
        remove the last element in stack and save it
        if stack is empty print stack is empty
        """
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        return self.data.pop()


if __name__ == "__main__":
    stack = Stack()
    n = int(input("Enter size of stack: "))
    for i in range(n):
        element = int(input("Enter number: "))
        stack.push(element)
    print(f"is stack empty: {stack.is_empty()}")
    print(f"Stack length: {len(stack)}")
    print("\n\nreverse order stack")
    for i in range(n):
        print(f"{stack.pop()}", end= " ")
    print(f"\nis stack empty: {stack.is_empty()}")
    print(f"Stack length: {len(stack)}")

#Sample Input


#Enter array size: 5
#Enter arry elements : 
#4
#5
#6
#2
#1

#input to stack : 4 5 6 2 1
#output of stack.pop() is reverse stack order: 2 5 7 10 12 21 23 34
#output checks if stack empty: True
#output length of stack: 0 


