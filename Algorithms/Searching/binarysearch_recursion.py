#Given a sorted array of n elements, write a binary search algorithm to search a given element x in array.
#binary serach using recursion

def binarySearch(arr, low, high, s):
    if high>=low:
        mid = (high + low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, s)
        else:
            return binarySearch(arr, mid+1, high, s)
    else:
        return -1

arr = []
n = int(input())

for i in range(n):
    #adding the sorted n elements in the array one by one
    x = int(input())
    arr.append(x)

#enter the element you want to seach
s = int(input())
ans = binarySearch(arr, 0, n-1, s)
if ans == -1:
    print(-1) #printing -1 if entered element doesn't exist
else:
    print(ans) #printing the index where the element is present

#input
# 4 (no of elements)
# 1 (1st element)
# 2 (2nd element)
# 3 (3rd element)
# 4 (4th element)
# 4 (element to be searched)

#output
# 3 (4 is present at index 3)
