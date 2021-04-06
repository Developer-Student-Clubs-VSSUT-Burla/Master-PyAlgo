# In Spiral Traversal of matrix, first you need to traverse in following order top row -> last column -> last row -> first column
# After that second row -> last second column -> last second row -> second column and so on till no elements are left for traversal 

def spiral_matrix(m, n, matrix):
	k=0
	l=0

	while (k < m and l < n):
	    
		for i in range(l,n):
			print(matrix[k][i],end=" ")
		k=k+1

		for i in range(k,m):
			print(matrix[i][n-1],end=" ")
		n=n-1

		if (k<m):
			for i in range(n-1,l-1,-1):
				print(matrix[m-1][i],end=" ")
			m=m-1

		if (l<n):
			for i in range(m-1,k-1,-1):
				print(matrix[i][l],end=" ")
			l=l+1
      

R=int(input())
C=int(input())
matrix=[]

for i in range(0,R):
    temp=list(map(int,input().split()))
    matrix.append(temp)
        
spiral_matrix(R, C, matrix)

''' 
INPUT:
2
3
1 2 3
4 5 6
OUTPUT:
1 2 3 4 5 6 

INPUT:
2
2
1 2
3 4
OUTPUT:
1 2 3 4

Time Complexity: O(R*C)
Space complexity: O(1)
'''

