# Given an array (or string), the task is to reverse the array/string.
# Examples : 
 

# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}


def reverseList(A, start, end):
	while start < end:
		A[start], A[end] = A[end], A[start]
		start += 1
		end -= 1

# Driver function to test above function
A = list(map(int,input().split()))
print(A)
reverseList(A, 0, len(A)-1)
print(f"Reversed list is:{A}")
#print(A)
