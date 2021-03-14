# Dutch National Flag is also known as DNF sort or the 0-1-2 sort and is a way of sorting an array containing only 0s , 1s and 2s.
 # The Dutch National Flag has 3 colours and in asimiliar way the array has 3 different numbers where:
  # 0s represent red, 1s represent white and 2s represent blue

# The following code is a way to implement: 
 # The array after implementation of DNF sort should look like: 0,0....1,1,1,1,....2,2,2


def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]

def dnfsort(elements,elements_size):
    low=0
    mid=0
    high=elements_size-1

    while(mid<=high):
        if elements[mid]==0:                  # if 0 swap low and mid because all 0s should be in the begining
            swap(elements,low,mid)
            low+=1 
            mid+=1

        elif (elements[mid]==1):              # since we need all the 1s in the middle position so we don't swap
            mid+=1

        else:
            swap(elements,mid,high)           # we need 2s in the end of array so we swap the high and low
            high-=1
    return elements

def print_dnf(elements):
    for i in elements:
        print(i, end=" ")

# Driver code for the above is here:

if __name__=='__main__':

    numbers=[]
    n=int(input("Enter the number of elements: "))

    print("Enter the elements: ")

    for i in range(0,n):
        elements=int(input())

        numbers.append(elements)

    numbers=dnfsort(numbers,n)
    print("After DNF Sort: ")
    print_dnf(numbers)
