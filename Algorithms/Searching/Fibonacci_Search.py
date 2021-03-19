# Python3 program on Fibonacci search.

# Time complexity O(log(n))
# Fibonacci Search is a comparison-based technique that uses Fibonacci numbers to search an element in a sorted array.
def fSearch(arr, x, n):
 
    
    f2 = 0  # Fibonacci No at (-2)
    f1 = 1  # Fibonacci No at (-1)
    f = f2 + f1  # Fibonacci No at (0) 
 
    # Fibonacci number greater than or equal to n
    while (f < n):
        f2 = f1
        f1 = f
        f = f2 + f1
 
    offset = -1
 
    while (f > 1):
        i = min(offset+f2, n-1)
        
        if (arr[i] < x):
            f = f1
            f1 = f2
            f2 = f - f1
            offset = i
 
        elif (arr[i] > x):
            f = f2
            f1 = f1 - f2
            f2 = f - f1
            
        else:
            return i
 
    # comparing the last element with x 
    if(f1 and arr[n-1] == x):
        return n-1
 
    # element not found. 
    return -1
 
 
# main
n = int(input("Enter the length of the Array: "))
arr = list(map(int, input("Enter the elements of the Array: ").split()))     
x = int(input("Enter the element which you want to check in the array: "))
index = fSearch(arr, x, n)
if index>=0:
  print(x," is found at index: ",index)
else:
  print(x,"isn't present in the array")
 

