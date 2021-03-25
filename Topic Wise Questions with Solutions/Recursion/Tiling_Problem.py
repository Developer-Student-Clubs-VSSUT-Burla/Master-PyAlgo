# Given a 2*n board and 2*1 tiles. Find all the possible ways by which 
#    we can tile the board using that tiles

# Input = 4
# Output = 3


# For this issue we will be using the approach of recursion.
# There are 3 possible ways of tiling the board 2*n board:
#     1.Vertically- Using all the tiles in a vertical manner
#     2.Horizantally- Using all the tiles in a horizontal manner
#     3.Combined- Using the tiles in both horizontally and vertically


# When we use the tiles vertically, each tile occupies a column in the board
#    and for horizontal manner, each tile occupies 1 space each in two rows


# The code for the following problem :

def tilingways(n):
    
    if n==0 or n==1:     # as for 2*1 board there will be only one possible way i.e vertically
        return n

    return tilingways(n-1) + tilingways(n-2)
# we use (n-1) for the tiles used vertically and (n-2) for the ones horizontally

#Driver code for the following:

if __name__=='__main__':

    n=int(input("Enter the number of columns(n): "))

    print("Possible ways of tiling: ", tilingways(n))