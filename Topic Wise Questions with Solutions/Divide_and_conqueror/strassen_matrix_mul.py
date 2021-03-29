"""
	Computes matrix product by divide and conquer approach, recursively.
	Input: nxn matrices x and y
	Output: nxn matrix, product of x and y
"""

import numpy as np

def strassen(x, y):
	
	# Base case when size of matrices is 1x1
	if len(x) == 1:
		return x * y # simply returning product of the two no.

	# Splitting the first into quadrants.

  row, col = x.shape # getting row and column of the matrix
	half_row, half_col = row//2, col//2 # dividing them into halves
	a = x[:half_row, :half_col] #first matrix
  b = x[:half_row, half_col:] #second matrix
  c = x[half_row:, :half_col] #third matrix
  d = x[half_row:, half_col:] #fourth matrix

    # Splitting the second into quadrants.
  row, col = y.shape 
	half_row, half_col = row//2, col//2 # dividing them into halves
	e = y[:half_row, :half_col] #first matrix
  f = y[:half_row, half_col:] #second matrix
  g = y[half_row:, :half_col] #third matrix
  h = y[half_row:, half_col:] #fourth matrix

  """
  For multiplying two matrices of size n x n, we make 8 recursive calls above,
  each on a matrix/subproblem with size n/2 x n/2.
  Each of these recursive calls multiplies two n/2 x n/2 matrices, which are then added together.
  """
  
	m1 = strassen(a, f - h)
	m2 = strassen(a + b, h)		
	m3 = strassen(c + d, e)		
	m4 = strassen(d, g - e)		
	m5 = strassen(a + d, e + h)		
	m6 = strassen(b - d, g + h)
	m7 = strassen(a - c, e + f)

	# Computing the values of the 4 quadrants of the final matrix c
	c11 = m5 + m4 - m2 + m6
	c12 = m1 + m2		
	c21 = m3 + m4			
	c22 = m1 + m5 - m3 - m7

	# Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.

	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

	return c
