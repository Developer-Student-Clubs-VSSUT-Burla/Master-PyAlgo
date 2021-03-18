"""  
    WIGGLE SORT
    This program accepts an array of unsorted numbers and
    sorts the array such that arr[0]<arr[1]>arr[2]<arr[3]...

    arr is sorted and stored in second array res
    res is partitioned into two such that left sub-array 
    contains elements less than the elements in right sub-array
    Elements in the left sub-array  are added to the even indices of arr
    Elements in the right sub-array are added to the odd indices of arr
"""

# to wiggle sort arr
def wiggle_sort(n, arr):
    res = sorted(arr)
    print(res)
    left = (n - 1) // 2
    right = n - 1

    for k in range(0, n, 2):
        arr[k] = res[left]
        left -= 1
    for i in range(1, n, 2):
        arr[i] = res[right]
        right -= 1
    print("Wiggle sorted array")
    print(arr)


# driver code
arr = list(map(int, input().split()))
no_of_elements = len(arr)
wiggle_sort(no_of_elements, arr)


#   1. Sample input:
#      1 3 2 2 3 1
#      Sample output:
#      [2,3,1,3,1,2]

#   2. Sample input:
#      1 4 6 2 3 7 9 2 1 0
#      Sample Output:
#      [2, 9, 2, 7, 1, 6, 1, 4, 0, 3]
#

#    Time Complexity : O(nlogn)   (Sorting takes O(n logn) and traversal takes O(n))
#    Space Complexity : O(n)   (New array to store the wiggle sorted elements)
