#insertion sort results in sorting the given list/array in ascending order of their value
def insertion_sort(array):
    for i in range(1, len(array)):     #Traversing through 1 to length of the array i.e. calculated by len(arr) 
        key_item = array[i]
        #Moving elements of array that are greater than the key, to one position ahead of their current position 
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
            
        array[j + 1] = key_item
            


if __name__ == "__main__":
    
    array = list(map(int, input().split()))   #to get integer list as input from user
    
    print("The original array :")   #printing the actual array so that we can compare the sorted and original arrays at the end.
    for i in range(len(array)):
        print ("%d" %array[i]) 
        
    insertion_sort(array)     #calling function of insertion sort
    print ("The sorted array :")   #printing sorted array 
    for i in range(len(array)):
        print ("%d" %array[i]) 
      
      
      """
      *Some sample input and output for the above code*
      
1) custom input : 2 34 56 89 9
output: 
The original array :
2
34
56
89
9
The sorted array :
2
9
34
56
89

2) custom input : 34 67 91 3 11 45 209
output:
The original array :
34
67
91
3
11
45
209
The sorted array :
3
11
34
45
67
91
209


3) custom input : 8 76 44 21 4 1 
output: 
The original array :
8
76
44
21
4
1
The sorted array :
1
4
8
21
44
76

      """
