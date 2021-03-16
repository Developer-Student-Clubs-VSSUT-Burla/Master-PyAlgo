#Given a sorted array of n elements, write a binary search algorithm to search a given element x in array.
#binary serach using recursion
#Time complexity: O(log(n))
def binarySearch(arr, low, high, x):
    if high>=low:
        mid = (high + low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)
        else:
            return binarySearch(arr, mid+1, high, x)
    else:
        return -1

arr = []
print("Enter the number of elements you want to enter in the sorted array: ")
n = int(input())

for i in range(n):
    #adding the sorted n elements in the array one by one
    print("Enter element number {}:".format(i+1))
    x = int(input())
    arr.append(x)

print("Enter the element you want to search")
s = int(input())
ans = binarySearch(arr, 0, n-1, s)
if ans == -1:
    print("Entered element not found") #printing -1 if entered element doesn't exist
else:
    print("Entered element is found at index ", ans) #printing the index where the element is present

#input
# 4 (no of elements)
# 1 (1st element)
# 2 (2nd element)
# 3 (3rd element)
# 4 (4th element)
# 4 (element to be searched)

#output
# 3 (4 is present at index 3)
