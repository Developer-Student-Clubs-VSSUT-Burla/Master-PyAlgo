class ConstructNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LLConstruct:
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
    
    def Merge(self, list1, list2):
        result = None
         
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
             
        
        if list1.data <= list2.data:
            result = list1
            result.next = self.Merge(list1.next, list2)
        else:
            result = list2
            result.next = self.Merge(list1, list2.next)
        return result

    def mergeSort(self, start):
        if start == None or start.next == None:
            return start
 
        
        middle = self.getMiddle(start)
        nexttomiddle = middle.next
 
        
        middle.next = None
 
       
        left = self.mergeSort(start)
         
        
        right = self.mergeSort(nexttomiddle)
 
       
        sortedlist = self.Merge(left, right)
        return sortedlist 
   
  
    def getMiddle(self, head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
             
        return slow       

def Display(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = " -> ")
        curr_node = curr_node.next
    print('.')
     

if __name__ == '__main__':
    ll = LLConstruct()
     
    n = int(input());
    Elements = list(map(int,input().split()));
    
    for i in range (n):
        ll.appendatlast(Elements[i]);
     
    ll.head = ll.mergeSort(ll.head)
    Display(ll.head)
