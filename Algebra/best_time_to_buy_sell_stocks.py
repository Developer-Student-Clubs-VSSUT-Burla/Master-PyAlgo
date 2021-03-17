"""
Problem Statement: Given the prices of stocks over a certain period of time, find out the maximum profit that can be earned.

Solution: We will be using Kadane's algorithm to solve this problem.
Time Complexity: O(n)
Space Complexity: O(1)

"""

print("Enter the number of days-", end = " ")
n = int(input())
print("Enter the stock prices(seperated by a space)-", end = " ")
prices = list(map(float, input().split()))

if n<1:
    print("0")
else:
    min_price = prices[0]    #initially, the minimum price is the first one
    profit, max_profit = 0,0

    for i in range(1,n):
        min_price = min(prices[i], min_price)
        profit = prices[i]-min_price
        max_profit = max(profit, max_profit)

    print("The maximum profit would be {}".format(max_profit))
        
