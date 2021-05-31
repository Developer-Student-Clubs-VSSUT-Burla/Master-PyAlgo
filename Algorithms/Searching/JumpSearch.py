'''
Jump Search only works on sorted lists.It creates a block and tries to find the element in that block. 
If the item is not in the block, it shifts the entire block. The block size is based on the size of the list. 
If the size of the list is n then block size will be √n. 
After finding a correct block it finds the item using a linear search technique.
'''

import math
#defining jump_search with function
def jump_search (mylist,value,length):
    step=int(math.sqrt(len(mylist)))
    previous=0
    while(mylist[min(step, length)-1]<value):
          previous=step
          step=step+int(math.sqrt(len(mylist)))
          if(previous>=length):
              return -1
    while(mylist[previous] < value):
        previous+=1
        if(previous==min(step,length)):
           return -1
    if(mylist[previous]==value):
        return previous
    return -1

#defining a list of random values
mylist=[1,4,5,12,13]

number_to_be_searched=int(input("Enter number to be searched:"))
found_index=jump_search(mylist,number_to_be_searched,len(mylist))
if(found_index!=-1):
    print("Element found at index:",found_index)
else:
    print("Element not found in list")

'''
 Time Complexity: O(√n)
 Space Complexity: O(1)
'''
'''Sample Output
Enter number to be searched:13
Element found at index: 4

Enter number to be searched:2
Element not found in list
'''
