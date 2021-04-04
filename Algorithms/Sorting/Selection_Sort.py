'''
SELECTION SORT
This algorithm sorts an array by repeatedly finding the minimum element 
(considering ascending order) from unsorted part and putting it at the beginning.

TIME COMPLEXITY : O(n²)
SPACE COMPLEXITY : O(1)
'''

def selection_sort(array):
	size = len(array)
	for start in range(size):
		minpos = start
		for index in range(start, size):
			if array[index] < array[minpos]:
				minpos = index
		array[start], array[minpos] = array[minpos], array[start]

array = list(map(int,input("Enter the elements of Array : ").split())) 
selection_sort(array)
print('After running selection_sort : ', array)

'''
OUTPUT

Enter the elements of Array : 43 32 123 67 3 76
After running selection_sort :  [3, 32, 43, 67, 76, 123]
'''