'''
Program to find union of two sorted arrays

'''

def printunion(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j])
            j += 1
        else:
            print(arr2[j])
            j += 1
            i += 1

    # Print remaining elements of the larger array
    while i < m:
        print(arr1[i])
        i += 1

    while j < n:
        print(arr2[j])
        j += 1


# Driver program
arr1 = []
arr2 = []
m = int(input("Enter the number of elements of array 1 :"))
print("Enter the elements of array 1 :")
for i in range(m):
    val = int(input())
    arr1.append(val)
n = int(input("Enter the number of elements of array 2 :"))
print("Enter the elements of array 2 :")
for i in range(n):
    val = int(input())
    arr2.append(val)
print("Union of the two arrays is :")
printunion(arr1, arr2, m, n)

'''
Time complexity of the program : 0(n+m)

Sample Test Case :
Enter the number of elements of array 1 : 4
Enter the elements of array 1 :
1
3
4
5
Enter the number of elements of array 2 : 2
Enter the elements of array 2 :
7
9
Union of the two arrays is :
1
3
4
5
7
9
'''
