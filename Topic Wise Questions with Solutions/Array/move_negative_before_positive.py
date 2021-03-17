# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers
# Examples : 
 

# Input  : arr = [-1, 1, -2, 2, 3, -3]
# Output : arr = [-1, -2, -3, 1, 2, 3]

# Input :  arr = [1, 2, 3, -1, -2, -3]
# Output : arr = [-1, -2, -3, 1, 2, 3]


def move_negative_before_positive(arr):
		
    # using two pointers
    
    n = len(arr)
    
    l = 0
    r = n - 1
    
    while (l < r):
        
        if arr[l] < 0 and arr[r] < 0:
            l += 1
        
        elif arr[l] > 0 and arr[r] > 0:
            r -= 1
        
        elif arr[l] < 0 and arr[r] > 0:
            l += 1
            r -= 1
        
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    
    return arr


# Driver function to test above function
#input = "-1, 1, 2, -2, 3, -3"
arr = list(map(int,input().split(",")))
print("input array :")
print(arr)
print("output array:")
print(move_negative_before_positive(arr))

