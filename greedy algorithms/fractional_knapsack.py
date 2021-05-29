"""
Author : Robin Singh
Implementation Of Fractional Knapsack
Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack
n Fractional Knapsack, we can break items for maximizing the total value of knapsack
This problem in which we can break an item is also called the fractional knapsack problem
An efficient solution is to use Greedy approach. The basic idea of the greedy approach is to calculate
the ratio value/weight for each item and sort the item on basis of this ratio. Then take the item with
the highest ratio and add them until we can’t add the next item as a whole and at the end add the next item as much as we can
Which will always be the optimal solution to this problem
Time Complexity  : O(nLogn)
"""
import operator


def fractional_knapsack(p, w, capacity):

    n = len(p)
    new_list = []
    for i in range(n):
        new_list.append([p[i], w[i], p[i]*1.0/w[i]])

    new_list = sorted(new_list, reverse=True, key=operator.itemgetter(2))
    max_profit = 0
    fractional_val = 0
    table_profit = []
    table_weight = []
    ratio_table = []

    for i in range(n):
        if capacity > 0 and new_list[i][1] < capacity:
            capacity -= new_list[i][1]
            max_profit += new_list[i][0]
            table_profit.append(new_list[i][0])
            table_weight.append(new_list[i][1])
            ratio_table.append(new_list[i][2])

        else:
            fractional_val = i
            table_profit.append(new_list[i][0])
            table_weight.append(new_list[i][1])
            ratio_table.append(new_list[i][2])

            break

    if capacity > 0:
        max_profit += capacity * \
            (new_list[fractional_val][0])/(new_list[fractional_val][1])

    o = len(table_profit)
    print("Fractional Knapsack")
    for x in range(o):
        print(
            f"Profit :{table_profit[x]}\t\tWeight  : {table_weight[x]}\t\tProfit/Weight : {ratio_table[x]}")
    print("Total Profit :", max_profit)


if __name__ == '__main__':

    profit = list(map(int, input("Entre Profit Value : ").split()))
    weight = list(map(int, input("Entre weight  Values  : ").split()))
    capacity = int(input("Entre Capacity of the knapsack"))
    fractional_knapsack(profit, weight, capacity)

"""
Entre Profit Value : 12 8 9 6 14 30
Entre weight  Values  : 98 45 32 69 10 3
Entre Capacity of the knapsack28
Fractional Knapsack
Profit :30              Weight  : 3             Profit/Weight : 10.0
Profit :14              Weight  : 10            Profit/Weight : 1.4
Profit :9               Weight  : 32            Profit/Weight : 0.28125
Total Profit : 48.21875
"""
