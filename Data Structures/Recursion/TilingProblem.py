# we are given a 2*n board and tiles of size 2*1 . To find the number of ways possible to 
 # tile the given board

# we will be using recursion for this:

#There can be three ways in which we do this:
# 1. Using the tile vertically    2. Using the tile horizontally    3.Using both horizontally and vertically

# When we use the tile horizontally we occupy 1 space in the columns of a 2*n board
# When we use the tile vertically we occupy both spaces in the columns of a 2*n board

def TilingWays(n):
    if n==0 or n==1:     # As the ways depend on n, a 2*1(n=1) board can be tiled only in one way that is vertically
        return n
    
    return TilingWays(n-1) + TilingWays(n-2)
    # We call recursion (n-1) for tiles placed horizonatally and (n-2) for the ones placed vertically


# Driver code:

if __name__=='__main__':

    n=int(input())

    print("Ways of Tiling:", TilingWays(n))