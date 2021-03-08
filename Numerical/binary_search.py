# Binary Search Algorithm
# Input: A sorted array arr and element to be searched,key
# If key is equal to the element at the middle of the array corresponding index is returned
# Else if the key is greater than the middle element search continues in the left subarray
# else the search continues in the right subarray.
# Since the size of the array is reduced to half after each iteration, Time complexity is O(logn)

def binary_search(arr,key):
    n=len(arr)
    first =0
    last = n-1
    mid =(first+last)//2
    while first<=last:
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            last =mid-1
        else :
            first =mid+1
        mid= (first+last)//2
    return -1

arr=list(map(int,input("Enter the array elements in sorted order: ").strip().split()))
key = int(input("Enter the element to be searched: "))
location = binary_search(arr,key)
if location!= -1:
    print(str(key) +" is found at index "+ str(location))
else:
    print (str(key) + " does not exist in the array")


