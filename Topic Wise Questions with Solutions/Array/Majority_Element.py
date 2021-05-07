''' 
The majority element is the element that appears more than ⌊n / 2⌋ times.
Assuming that the majority element always exists in the array.
'''
def majorityElement(array):
    for i in range(0, len(array)):
        count = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                count += 1
        if count > int(len(array) / 2):
            return array[i]
    return -1

n = int(input('Enter the size of the array:'))
array = list(map(int, input('Enter the elements : ').strip().split()))[:n]
element = majorityElement(array)
if element == -1:
    print ('No Majority Element found')
else:
    print ('Majority Element = ', element)
    
'''
Sample Output
Enter the size of the array:9
Enter the elements : 2 2 2 4 1 1 1 1 1
Majority Element = 1

'''

