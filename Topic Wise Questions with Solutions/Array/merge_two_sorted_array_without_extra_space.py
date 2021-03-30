# Python program to merge two sorted arrays with O(1) extra space.

def merge_array(a1, a2, n, m):

	# Iterate through all elements of a2[] starting from the last element
	for i in range(m-1, -1, -1):
	
	   # Find the smallest element greater than a2[i]. Move all elements one position ahead till the smallest greater
		# element is not found
		last = a1[n-1]
		j=n-2
		while(j >= 0 and a1[j] > a2[i]):
			a1[j+1] = a1[j]
			j-=1

		# If there was a greater element
		if (j != n-2 or last > a2[i]):
		
			a1[j+1] = a2[i]
			a2[i] = last

# main program
n = int(input("Enter length of first array : "))
m = int(input("\nEnter length of second array : "))
a1 = list(map(int,input("\nEnter the elements of first array : ").strip().split()))[:n]
a2 = list(map(int,input("\nEnter the elements of second array : ").strip().split()))[:n]

merge_array(a1, a2, n, m)

print("After Merging \nFirst Array:", end="")
for i in range(n):
	print(a1[i] , " ", end="")

print("\nSecond Array: ", end="")
for i in range(m):
	print(a2[i] , " ", end="")

''''
Input :
n = 6
m = 4
a1 = [1, 5, 9, 10, 15, 20]
a2 = [2, 3, 8, 13]

output :
After Merging 
First Array: 1 2 3 5 8 9 
Second Array: 10 13 15 20

Time Complexity: O(m+n)
The worst case time complexity of code/algorithm is O(m*n).

'''
