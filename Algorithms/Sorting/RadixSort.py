# Radix Sort algorithm using count sort algorithm
def RadixSort(arr, n):
    maxElement = int(max(arr))
    place = 1
    # Invoke Count sort on digits by place attribute
    while maxElement // place > 0:
        CountingSort(arr, place)
        place *= 10


def CountingSort(arr, place):
    """Count sort algorithm that sort
       number based on digits represented by place"""
    n = len(arr)
    count = [0] * 10
    result = [0] * n
    for i in range(n):
        count[(arr[i] // place) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n-1, -1, -1):
        index = (arr[i] // place) % 10
        result[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(0, n):
        arr[i] = result[i]


if __name__ == "__main__":
    arr = [53, 10, 0, 31, 85, 25, 13, 10]
    RadixSort(arr, 2)
    print(arr)
# Complexity: O(d*(n+b))
#Sample Input
#input array: [53, 10, 0, 31, 85, 25, 13, 10]
#output array: [0, 10, 10, 13, 25, 31, 53, 85]