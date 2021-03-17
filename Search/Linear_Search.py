"""
Take an array as input and the element to search
Search for the element by iterating through each element in array and 
return the corresponding index of element if it is found .
"""

def linearsearch(arr,ele):
    for i in range(len(arr)):
        if(arr[i]==ele):
            return i
    return -1

array=list(map(int,input('Input some numbers : ').split()))
element=int(input('Enter element to search : '))
a=linearsearch(array,element)
if(a>0):
    print('Element is found at index ',a)
else:
    print('Element is not present in array')

# Time Complexity : O(n)
# Space Complexity : O(1)

# TestCase 1:
# Input some numbers : 5 4 1 3 2
# Enter element to search : 3
# Element is found at 3

# TestCase 2:
# Input some numbers : 2 8 4 6 1 6 3 5 2
# Enter element to search : 9
# Element is not present in array
