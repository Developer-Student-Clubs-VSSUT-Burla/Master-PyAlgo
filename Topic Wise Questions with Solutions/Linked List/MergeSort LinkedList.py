''' 
The function is expected to return a list sorted using MergeSort.

MergeSort is a sorting Technique Based on  Divide and Conquer algorithm.It repeatedly breaks down a list into several sublists until each sublist consists of a single element
and combines the sublists in a manner that results into a sorted list using merge function. 
'''
class ConstructNode:                                # Node class
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LLConstruct:                                  # Contruction of Linked List
    def __init__(self):
        self.head = None
    def appendatlast(self,data):
         
        new_node = ConstructNode(data)
         
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
             
       
        curr_node.next = new_node
    
def Merge(list1, list2):                          # Merge function takes two sorted lists and merge them in sorted manner
        result = None
         
        if list1 == None:                        # if any of the list is empty return the non empty list
            return list2
        if list2 == None:
            return list1
             
        
        if list1.data <= list2.data:                     # findind minmum value of both list will be at 1st index so selecting minimum out of them     
            result = list1
            result.next = Merge(list1.next, list2)       # placing the minimum value and calling merge again
        else:
            result = list2
            result.next = Merge(list1, list2.next)
        return result                                    # return the sorted merged Lists

def mergeSort(start):                                    # MergeSort Function
        if start == None or start.next == None:          # empty lists or list with one elements are already sorted
            return start
 
        
        middle = getMiddle(start)                        # get middle for dividing list in two parts
        
        nexttomiddle = middle.next                      # create two sublist from start to middle and middle+1 to end
 
        middle.next = None                              
 
        left = mergeSort(start)                        # MergeSort for divided lists
         
        right = mergeSort(nexttomiddle)
 
        sortedlist = Merge(left, right)              # call merge function for merging lists in sorted manner
        return sortedlist                            # return sorted LinkedList
   
def getMiddle(head):                                 # to get middle element of a list
        if (head == None):                           # Base Case
            return head
 
        slow = head           
        fast = head
 
        while (fast.next != None and fast.next.next != None):   # move fast 2 steps and slow 1 step
            slow = slow.next
            fast = fast.next.next
             
        return slow                                            # when fast will reach end slow will reach middle of the Linked List
         

def Display(head):                                      # Function to display Linked List
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = " -> ")
        curr_node = curr_node.next
    print('.')
     

if __name__ == '__main__':                               # Driver Code
    ll = LLConstruct()
     
    n = int(input());                                    # taking input for size of Linked List
    Elements = list(map(int,input().split()));           # taking input of list elements
    
    for i in range (n):
        ll.appendatlast(Elements[i]);                    # construction of Linked List
     
    ll.head = mergeSort(ll.head)                         # calling mergeSort for Sorting the Linked List
    Display(ll.head)                                     # Display the Linked List
    
'''
Test case 1 :
input : 6
        10 2 19 22 3 7
output : 2 -> 3 -> 7 -> 10 -> 19 -> 22 -> .

Test case 2 : 
input : 10
        6 7 2 9 12 31 1 4 19 20
output : 1 -> 2 -> 4 -> 6 -> 7 -> 9 -> 12 -> 19 -> 20 -> 31 -> .

Time Complexity : O(n*log(n))
Space Complexity : O(n)
'''
    
