""""
Bubble Sort in Python

Time complexity : 0(n^2)
Space complexity : 0(1)
Sample Input/Output :
Enter the total number of elements : 5
Enter the elements
26
23
98
45
12
Sorted List is : [12, 23, 26, 45, 98]

"""
arr = []
num = int(input("Enter the total number of elements : "))
print("Enter the elements")
for i in range(num):
    val = int(input())
    arr.append(val)

for i in range(num - 1):
    for j in range(num - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted List is :", arr)