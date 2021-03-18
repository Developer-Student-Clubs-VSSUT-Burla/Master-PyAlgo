# Given a square matrix A (n*n) & its number of rows (or columns) N, return the Transpose of A.

# The transpose of a matrix is the matrix flipped over its main diagonal,
#    switching the row and column indices of the matrix

# Constraints: 1<=N<=1000

# input = 1 2 3
#         4 5 6
#         7 8 9

# output =  1 4 7
#           2 5 8
#           3 6 9

if __name__=='__main__':

    N=int(input("Input the value of N: "))

    A=[]   #initialising the matrix
    print("Enter the elements row wise: ")

    for i in range(N):
        a=[]
        for j in range(N):
            a.append(int(input()))
        A.append(a)

    # For the matrix transpose:
    for row in A: 
        print(row) 
    print("\n") 
    transpose = zip(*A) 
    for row in transpose: 
        print(row) 


