""" HEAP SORT """

## Time Complexity : O(nlogn)
## Space Complexity : O(1)

# to insert into heap tree
def insert(lis, n, item):
    n += 1
    p = n
    while (p > 1):
        parent = p // 2
        if (item <= lis[parent]):
            lis[p] = item
            return

        lis[p] = lis[parent]
        p = parent

    lis[1] = item

# to remove root node from heap tree
def delete(lis, n, item):
    item = lis[1]
    last = lis[n]
    n -= 1
    p = 1
    left = 2
    right = 3
    while(right <= n):
        if(last >= lis[left] and last >= lis[right]):
            lis[p] = last
            return

        if(lis[right] <= lis[left]):
            lis[p] = lis[left]
            p = left

        else:
            lis[p] = lis[right]
            p = right

        left = 2*p
        right = left+1

    if(left == n and last < lis[left]):
        lis[p] = lis[left]
        p = left

    lis[p] = last

#to sort the list
def heap_sort(lis, n):
    for i in range(0, n):
        insert(lis, i, lis[i + 1])
    while(n > 1):
        item = lis[1]
        delete(lis, n, item)
        n -= 1
        lis[n+1] = item
    return lis

#driver code
n = int(input())
lis = list(map(int, input().split()))
res = heap_sort(lis, n-1)
print("Sorted list: ")
for each in res:
    print(each, end=" ")

"""
Sample Input:
6
1 7 3 5 2 6

Sample Output:
Sorted list:
1 2 3 5 6 7

"""