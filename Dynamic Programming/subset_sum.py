"""
SAMPLE INPUT AND OUTPUT

Enter size of array:
6
Enter elements of array: 
3 34 4 12 5 2
Enter sum: 
9
Subset with given sum is present

Time Complexity: O(sum * size of array)
Space Complexity: O(sum * size of array)
"""

def subsetSum(arr, size, S):
    # A 2D List containing boolean values, True and False
    # Fill every element of the 2D list with False as value
    dp = ([[False for i in range(S + 1)] for i in range(n + 1)])

    for i in range(0, size + 1):
        for j in range(0, S + 1):

            # Sum = 0 is always possible, by taking no elements in the subset
            if j == 0:
                dp[i][0] = True

            if i > 0:
                # If the value of the current element is less than the sum j, then either
                # include it and the current element or leave it and take the previous best
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                # Else take the previous best
                else:
                    dp[i][j] = dp[i - 1][j]

    return dp[size][S]


if __name__ == '__main__':
    print("Enter size of array: ")
    n = int(input())
    print("Enter elements of array: ")
    arr = [int(x) for x in input().split(' ')]
    print("Enter sum: ")
    S = int(input())
    res = subsetSum(arr, n, S)
    if res == False:
        print("No subset adds upto given sum")
    else:
        print("Subset with given sum is present")
