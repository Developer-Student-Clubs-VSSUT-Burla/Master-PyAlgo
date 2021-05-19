import time
def pivot(array, start, end):
    '''
We initialize low with the second element of the array
(one after the pivot) and high with the last element.
    '''
    pivot = array[start]
    low = start + 1
    high = end
    '''
To rearrange the elements we move the low towards the right and high towards the left. While doing this our motive is to make sure
that all the values greater than the pivot should move towards the right and all the values smaller than the pivot should move towards the left.

When we arrange the values in such a manner, we can find out the final position of the pivot element in the sorted array since
all the elements smaller than the pivot are on its left and all the elements on the right are greater.

Elements on right and left of the pivot may or may not be arranged in a sorted manner.
    '''
    while True: 
#moving high towards left
        while low <= high and array[high] >= pivot:
            high = high - 1
#moving low towards right 
        while low <= high and array[low] <= pivot:
            low = low + 1
#checking if low and high have crossed
        if low <= high:
#swapping values to rearrange
            array[low], array[high] = array[high], array[low]   
        else:
#breaking out of the loop if low > high
            break
#swapping pivot with high so that pivot is at its right # #position 
    array[start], array[high] = array[high], array[start]
    '''
If low is greater than high we break out of the loop and return high as the position of pivot element.
This means that we have successfully arranged the values around the pivot.
    '''
#returning pivot position
    return high
'''
After rearranging the elements around the pivot, we need to make recursive calls on the two halves of the array.
These calls will repeat themselves until we have arrays of size one
'''

def quick_sort(array, start, end):
    if start >= end:
        return
#call pivot 
    p = pivot(array, start, end)
#The same process of choosing a pivot and rearranging elements around it is repeated for the left and right halves.
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
 
array=list(map(int,input().split()))
t0 = time.perf_counter()
quick_sort(array, 0, len(array) - 1)
t1 = time.perf_counter()
print(array)
print("The time taken for rearranging the elements is ")
print((t1-t0))

'''
The worst-case time complexity of Quicksort is O(n^2) and average-case time complexity is O(nlogn).

Sample I/O and O/P
12 23 121 13
[12, 13, 23, 121]
The time taken for rearranging the elements is 
1.1500000000275179e-05
'''
