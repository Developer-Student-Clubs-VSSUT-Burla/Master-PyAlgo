'''
Program to find intersection of two sorted arrays

Time complexity : 0(m+n)

Sample Test Case:
Enter the number of elements of array 1 : 2
Enter the elements of array 1 :
1
2
Enter the number of elements of array 2 : 3
Enter the elements of array 2 :
1
3
4
Intersection of the two arrays is :
1

'''

def printintersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr2[j])
            j += 1
            i += 1


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
print("Intersection of the two arrays is :")
printintersection(arr1, arr2, m, n)