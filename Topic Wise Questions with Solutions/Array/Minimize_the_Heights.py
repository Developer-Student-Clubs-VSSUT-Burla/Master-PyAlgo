'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once.
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.
'''
def minimize_the_heights(arr,k):
    # let's sort arrays
    arr.sort()
    
    mindiff = arr[-1]-arr[0]
    for i in range(1,len(arr)):
        minval=min(arr[0]+k,arr[i]-k)
        maxval=max(arr[i-1]+k,arr[-1]-k)
        if minval<0:
            continue
        mindiff=min(mindiff,maxval-minval)
    return mindiff

if __name__ == "__main__":          
    arr = list(map(int, input("Enter the elements: ").split()))
    k = int(input("Enter K: "))
    print(minimize_the_heights(arr,k))

'''
Time Complexity: O(N*logN)
Space Complexity: O(N)

INPUT:

Enter the elements: 3 9 12 16 20 
Enter K: 3

OUTPUT:
11

Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between 
the largest and the smallest is 17-6 = 11.

'''