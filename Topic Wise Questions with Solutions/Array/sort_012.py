"""
Given an array consist of 0s, 1s and 2s. Write a function that sorts the given
array such that all 0s first, then all 1s in the middle and all 2s in last.
"""


def sort_using_three_pointers(arr):
    
    # three pointer
    # l -> tracks the 0s sorted subarray, h -> tracks the sorted 2s subarray and m -> will trace all the elements
    n = len(arr)
    
    l = 0
    m = 0
    h = n - 1
    
    
    while(m <= h):
        
        if arr[m] == 0:
            arr[m], arr[l] = arr[l], arr[m]
            l += 1
            m += 1
            
        elif arr[m] == 1:
            m += 1
        
        else:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
    
    return arr

def sort_using_counting(arr):
    
    n = len(arr)
    count_array = [0]*3 # count of 0s 1s 2s
    
    for i in range(n):
        if arr[i] == 0:
            count_array[0] += 1
        
        elif arr[i] == 1:
            count_array[1] += 1
        
        else:
            count_array[2] += 1
    
    i = 0
    for indx,count in enumerate(count_array):
        for j in range(count):
            arr[i] = indx
            i += 1
    
    return arr
            


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print("sort using three pointers : ")
print(sort_using_three_pointers(arr))
print("sort using counting : ")
print(sort_using_counting(arr))