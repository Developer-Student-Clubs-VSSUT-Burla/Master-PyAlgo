'''
Aim: To print the symmetric difference of two sets in ascending order.

'''

# getting the size of set 1
M=int(input().strip())
mo=[]
m=[]
# getting the elements of the set 1
mo=(input().strip().split())
for i in mo:
    m.append(int(i))
# getting the size of set 2
N=int(input().strip())
no=[]
n=[]
# getting the elements of the set 2
no=(input().strip().split())
for i in no:
    n.append(int(i))
# when entered the data type is 'list', so converting into 'set' data type
ms=set(m)
ns=set(n)
# list having set difference 'M-N'
x=list(ms.difference(ns))
# list having set difference 'N-M'
y=list(ns.difference(ms))
# summing up all the differences
z=x+y
# sorting the resulting list as we want the results in ascending order
z.sort()
# printing out all the elements of the list
for i in z:
    print(i)   

'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(N)
     
Sample Input:
4
2 3 4 5
4
2 3 11 1

Sample Output:
1
4
5
11

Explanation:
M-N = [4,5]
N-M = [11,1]
List 'z' will have elements --> [4,5,11,1]
After sorting --> [1,4,5,11]

'''