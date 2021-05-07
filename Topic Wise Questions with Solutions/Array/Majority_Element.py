''' 
The majority element is the element that appears more than ⌊n / 2⌋ times.
Assuming that the majority element always exists in the array.
'''
def majorityElement(array):
    if len(array) == 1:
        return array[0]
    array.sort()
    return array[len(array) // 2]


n = int(input('Enter the size of the array:'))
array = list(map(int, input('Enter the elements : ').strip().split()))[:n]
print ('Majority element = ', majorityElement(array))
    
'''
Sample Output
Enter the size of the array:9
Enter the elements : 2 2 2 4 1 1 1 1 1
Majority Element = 1

'''

