# Radix Sort algorithm using count sort algorithm. it is a non-comparative sorting algorithm. 
#It avoids comparison by creating and distributing elements into buckets according to their radix.
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
    arr = []
    digits_num =  int(input("Enter max num of digits: "))
    n = int(input("Enter size of array: "))
    for i in range(n):
        arr.append(int(input("Enter number: ")))
    RadixSort(arr, digits_num)
    print(arr)
# Complexity: O(d*(n+b))
#Sample Input
""" Input :-Enter max num of digits: 2
Enter size of array: 5
Enter number: 3
Enter number: 2
Enter number: 10
Enter number: 43
Enter number: 22
Output :-[2, 3, 10, 22, 43]
"""
