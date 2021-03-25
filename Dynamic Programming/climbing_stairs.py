# DP algorithm to find total ways to reach the n'th stair from the bottom
# when a person is allowed to climb either 1 or 2 stairs at a time
def totalWays(n):
    # create dp array of n+1 size for storing solutions to the subproblems
    dp = [0 for _ in range(n + 1)]

    # base case 1 way (with no steps)
    dp[0] = 1

    # There is only 1 way to reach the 1st stair
    dp[1] = 1

    # fill the dp array in a bottom-up manner
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    print("Enter the Number of Stairs")
    n = int(input())
    print("Number of ways to reach the " + str(n) + "'th stair is ", totalWays(n))

# Sample I/O :
# Enter the Number of Stairs
# 4
# Number of ways to reach the 4'th stair is  5