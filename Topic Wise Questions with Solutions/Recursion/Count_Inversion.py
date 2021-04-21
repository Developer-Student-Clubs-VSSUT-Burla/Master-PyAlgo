''' Count the inversion in an given array.
    Two elements a[i] and a[j] form an inversion if:
     a[i] > a[j]   and    i < j                         '''


# We will find the total number of inversion in an given array with the help of merge sort algorithm

def Count_Inversion(arr):
    return Sort(arr)[1]


def Sort(arr):

    n = len(arr) # defining the size of the array

    # Base Case: if length of the array is 1
    if(n == 1):
        return arr, 0

    # initialising the count with zero
    inv = 0

    # Sorting and counting the first and second half of the array
    left, x = Sort(arr[:n // 2]) # Sorting left array which consists elements right before mid
    right, y = Sort(arr[n // 2:]) # Sorting right array which consists elements from mid
    inv += x + y

    i, j = 0, 0
    n1 = n // 2
    n2 = n - n // 2
    temp_arr = []

    # Counting the inversion after merging both halves
    while(i < n1 and j < n2):
        if(left[i] <= right[j]):  # if left is less than right we append the elements to the empty array
            temp_arr.append(left[i])
            i += 1
        else:
            temp_arr.append(right[j])
            j += 1
            inv += n1 - i  # since the array is sorted if arr[j]< arr[i] then arr[j]<arr[i]<arr[i+1]......

    # To keep appending elements in the other array if one of the array is completed
    while(i < n1):
        temp_arr.append(left[i])
        i += 1

    while(j < n2):
        temp_arr.append(right[j])
        j += 1

    # Return the sorted array and inversion count
    return temp_arr, inv

# Driver code for the function:

if __name__ == '__main__':

    nums = list(map(int, input("Enter elements here:").split(",")))
    print("Total inversions are: ", Count_Inversion(nums))


''' Sample input : 
        Enter elements here: 3,5,6,9,1,2,7,8
    Sample output : 
        Total inversions are : 10

    Explanation: (3,1),(3,2),(5,1),(5,2),(6,1),(6,2),(9,1),(9,2),(9,7),(9,8) '''