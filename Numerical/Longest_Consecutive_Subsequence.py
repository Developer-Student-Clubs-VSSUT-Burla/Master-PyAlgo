"""
    Given an array of positive integers. Find the length of the longest sub-sequence
    such that elements in the subsequence are consecutive integers,
    the consecutive numbers can be in any order.
"""

def LargeSubseq(A):
 
    # Create a set to remove the duplicacy
    S = set(A)
 
    # initialize result by 1
    maxlength = 1
 
    # Iterate over each element
    for i in A:
 
        # Check the previous element `i-1` exist in the set or not 
        if (i - 1) not in S:
 
            # `len` stores the length of subsequence, starting with the current element
            len = 1
 
            # checking the element subsequence
            while (i + len) in S:
                len += 1
 
            # update result with the length of current consecutive subsequence
            maxlength = max(maxlength, len)
 
    return maxlength
 
 
#Driver Code 
if __name__ == '__main__':
 
    arr=list(map(int,input("Enter the numbers: ").split()))
    print("The length of the maximum consecutive subsequence is:",LargeSubseq(arr))
    
'''
    Sample Input:
    Enter the numbers: 6 4 7 9 1 3 2 4
    Sample Output:
    The length of the maximum consecutive subsequence is: 4

    Time complexity= O(n)
    Space complexity=O(n)
'''
