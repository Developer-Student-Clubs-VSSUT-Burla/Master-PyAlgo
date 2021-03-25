# Queue data structure is first in first out data structure

class Queue:
    Capacity = 10

    def __init__(self):
        self.data = [None] * Queue.Capacity
        self.size = 0
        self.front = 0

    def __len__(self):
        """Gives length of Queue"""
        return self.size

    def is_empty(self):
        """Checks if queue is empty"""
        return self.size == 0

    def resize(self, cap):
        """resizes self.data array if number of  elements exceed its size"""
        old = self.data
        self.data = [None] * cap
        f = self.front
        for i in range(cap):
            self.data[i] = old[f]
            f = (f + 1) % len(old)
        self.front = 0

    def Enqueue(self, x):
        """Enter new element to queue"""
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.size + self.front) % len(self.data)
        self.data[avail] = x
        self.size += 1

    def Dequeue(self):
        """Delete and return first element in queue"""
        if self.is_empty():
            Exception("Queue is empty")
        answer = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return answer

    def first(self):
        """Return element in front of queue
        Raise Empty exception if the queue is empty. """

        if self.is_empty():
            raise Exception("Queue is Empty")
        return self.data[self.front]


if __name__ == "__main__":
    queue = Queue()
    n = int(input("Enter size of queue: "))
    for i in range(n):
        element = int(input("Enter number: "))
        queue.Enqueue(element)
    print(f"is queue empty: {queue.is_empty()}")
    print(f"Queue length: {len(queue)}")
    print("\n\nPrint queue in same order, and delete elements")
    for i in range(n):
        print(f"{queue.Dequeue()}", end=" ")
    print(f"\nis Queue empty: {queue.is_empty()}")
    print(f"Queue length: {len(queue)}")

# Sample Input


# Enter array size: 5
# Enter arry elements :
# 4
# 5
# 6
# 2
# 1

# input to queue : 4 5 6 2 1
# output of queue.dequeue() is same queue order:  4 5 6 2 1
# output checks if stack empty: True
# output length of queue: 0
