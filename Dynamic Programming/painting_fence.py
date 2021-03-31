"""
Painting Fence problem

In a fence, with n posts and k available colours, we need to find out in how many different 
ways we can paint the fence so that at most two adjacent posts have the same colour.
Output the answer modulo 10^9 + 7
"""


def count(n, k):

    mod = 1000000007
    # Initialize the dp array with 0.
    dp = [0] * (n + 1)
    dp[1] = k
    dp[2] = k * k

    for i in range(3, n+1):
        dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod

    return dp[n]


if __name__ == '__main__':
    print("How many posts are there in the fence? ", end="")
    n = int(input())
    if(n == 0):
        print("\nNo posts present in the fence!!!")
        exit()
    print("How many colours are available? ", end="")
    k = int(input())
    if(k == 0):
        print("\nNo colour is available to paint!!!")
        exit()

    res = count(n, k)
    print("\nThe number of ways to colour the given posts is " + str(res))

"""
SAMPLE INPUT AND OUTPUT

SAMPLE I
How many posts are there in the fence? 3
How many colours are available? 7

The number of ways to colour the given posts is 336

SAMPLE II
How many posts are there in the fence? 5
How many colours are available? 0

No colour is available to paint!!!


Time Complexity: O(n) where 'n' is the number posts to paint
Space Complexity: O(n)
"""
