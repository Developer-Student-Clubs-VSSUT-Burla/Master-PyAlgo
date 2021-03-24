class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		
	# Function to print nodes in a 
	# given linked list 
	def printlist(self):
		temp = self.head
		while (temp):
			print(temp.data, end = " ")
			temp = temp.next
			
	# Function to remove duplicates from a 
	# unsorted linked list 
	def removeDuplicates(self, head):
		
		# Base case of empty list or 
		# list with only one element
		if self.head is None or self.head.next is None:
			return head
			
		# Hash to store seen values 
		hash = set() 
		current = head
		hash.add(self.head.data)
		
		while current.next is not None:
			if current.next.data in hash:
				current.next = current.next.next
			else:
				hash.add(current.next.data)
				current = current.next
		return head

# Driver code 
if __name__ == "__main__":
	
	# Creating Empty list
	llist = LinkedList()
	llist.head = Node(int(input('Enter head Node value:')))
	second = Node(int(input('Enter second Node value:')))
	third = Node(int(input('Enter third Node value:')))
	fourth = Node(int(input('Enter fourth Node value:')))
	fifth = Node(int(input('Enter fifth Node value:')))
	sixth = Node(int(input('Enter sixth Node value:')))
	seventh = Node(int(input('Enter seventh Node value:')))
	
	# Connecting second and third
	llist.head.next = second
	second.next = third
	third.next = fourth
	fourth.next = fifth
	fifth.next = sixth
	sixth.next = seventh

	# Printing data
	print("Linked List before removing Duplicates.")
	llist.printlist()
	llist.removeDuplicates(llist.head)
	print("\nLinked List after removing duplicates.")
	llist.printlist()
	
#Linked List before removing Duplicates.
#10 12 13 11 13 11 90 
#Linked List after removing duplicates.
#10 12 13 11 90 
