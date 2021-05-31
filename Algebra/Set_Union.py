'''
Aim: To find the total number of elements in the union of the entered sets.

'''

# getting the size of set 1
n1=int(input().strip())
s1=[]
s1o=[]
# getting the elements of the set 1
s1o=(input().strip().split())
for i in s1o:
    s1.append(int(i))
# getting the size of set 2
n2=int(input().strip())    
s2=[]
s2o=[]
# getting the elements of the set 2
s2o=(input().strip().split())
for i in s2o:
    s2.append(int(i))
# adding both the sets (as of now their data type is list)
set_union=s1+s2 
# if we convert the list into set data type, then only unique elements will retain
print(len(set(set_union)))

'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(N)
     
Sample Input:
5
3 1 4 6 2
5
6 8 3 6 1

Sample Output:
5

Explanation:
Elements in the union of both the sets --> [1,2,3,4,6,8]
Total count --> 6
Hence, the output is 6.

'''