# 0/1 knapSack Dynamic Programming
'''
Input1 : profit = [5,3,3,3,3]
        weight = [1,1,1,1,1]
        W = 10
Output1 :Weight Array: [1, 1, 1, 1, 1]
        Profit Array: [5, 3, 3, 3, 3]
        Weight Limit: 10
        Maximum Profit: 17

Input2 : profit = [1,3,4,5,7]
        weight = [3,4,1,2,0]
        W = 10
Output2 : Weight Array: [3, 4, 1, 2, 0]
        Profit Array: [1, 3, 4, 5, 7]
        Weight Limit: 10
        Maximum Profit: 20

Time Complexity : O(N*W), where ‘N’ is the number of weight element and ‘W’ is capacity.
Space Complexity :  O(N*W), The use of 2-D array of size ‘N*W’.
'''


def knapSack(profit, weight, W, i, dp):
    if i == 0:
        return 0
    if W == 0:
        return 0
    if dp[W][i] != -1:
        return dp[W][i]
    if W>=weight[i-1]:
        a = knapSack(profit, weight, W - weight[i - 1], i - 1, dp) + profit[i - 1]
    else:
        a = 0
    b = knapSack(profit, weight, W, i - 1, dp)
    dp[W][i] = max(a,b)
    # print("function cll for", W, i,max(a,b))
    return max(a,b)

def main():
    profit = [5,3,3,3,3]
    weight = [1,1,1,1,1]
    W = 10
    n = len(profit)
    dp = [[-1]*(n+1) for i in range(W+1)]
    max_p = knapSack(profit,weight,W,n,dp)
    print('Weight Array:', weight)
    print('Profit Array:', profit)
    print('Weight Limit:',W)
    print('Maximum Profit:',max_p)


if __name__ == '__main__':

    main()
