# Shell sort is an improvised version of insertion sort, where we move
# elements by more than one positions
def shellSort(arr, n):

    gap = n // 2

    while(gap > 0):
        for i in range(gap, n):
            ele = arr[i]
            index = i
            while index >= gap and arr[index-gap] > ele:
                arr[index] = arr[index-gap]
                index -= gap
            arr[index] = ele
        gap //= 2


if __name__ == '__main__':
    print("How many numbers do you want to sort? ", end="")
    n = int(input())
    print("Enter elements of array: ", end="")
    arr = [int(x) for x in input().split(' ')]
    res = shellSort(arr, n)
    print("The sorted array is:", end=" ")
    for i in arr:
        print(str(i), end=" ")

"""
SAMPLE INPUT AND OUTPUT

How many numbers do you want to sort? 7
Enter elements of array: 31 52 37 24 16 14 53
The sorted array is: 14 16 24 31 37 52 53 

Time Complexity: O(n^2) where 'n' is the number of elements to sort
Space Complexity: O(n)
"""
