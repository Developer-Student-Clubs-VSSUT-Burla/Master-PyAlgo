'''
Aim: Sort the entered array without using inbuilt functions.

'''

# getting the input
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# swapping elements and keeping a counter to check on the number of swaps done
nofswap = 0
for i in range(0,n-1):
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            # swapping
            a[i],a[i+1] = a[i+1],a[i]
            nofswap +=1

# printing results            
print("Array is sorted in", nofswap, "swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])

'''

COMPLEXITY:
	
	 Time Complexity -> O(N^2)
	 Space Complexity -> O(N)
     
Sample Input:
4
4 3 1 2
Sample Output:
Array is sorted in 5 swaps.
First Element: 1
Last Element: 4

Explaination:
a = [4,3,1,2]
original a: 4 3 1 2
round 1 --> a: 3 1 2 4 swaps this round: 3
round 2 --> a: 1 2 3 4 swaps this round: 2
round 3 --> a: 1 2 3 4 swaps this round: 0
Hence, 3+2 = 5.

'''