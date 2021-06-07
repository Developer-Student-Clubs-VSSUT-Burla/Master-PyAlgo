"""
Chef and N−1 more of his friends go to the night canteen. The canteen serves only three items (well, they serve more, but only these three are edible!), which are omelette, chocolate milkshake, and chocolate cake. Their prices are A, B and C respectively.

However, the canteen is about to run out of some ingredients. In particular, they only have E eggs and H chocolate bars left. They need:

2 eggs to make an omelette
3 chocolate bars for a chocolate milkshake
1 egg and 1 chocolate bar for a chocolate cake
Each of the N friends wants to order one item. They can only place an order if the canteen has enough ingredients to prepare all the ordered items. Find the smallest possible total price they have to pay or determine that it is impossible to prepare N items.

Input:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains six space-separated integers N, E, H, A, B and C.
Output:
For each test case, print a single line containing one integer ― the minimum cost of N items, or −1 if it is impossible to prepare N items.

Constraints
1≤T≤2⋅105
1≤N≤106
0≤E,H≤106
1≤A,B,C≤106
the sum of N over all test cases does not exceed 106
"""

for testcase in range(int(input())):
    items,eggs,chocolates,costometlette,costShake,costCake=map(int,input().split())
    ans=10**18
    for cakes in range(items+1):
        if eggs<cakes or chocolates<cakes:
            break
        omelettes=int((eggs-cakes)/2)
        shake=int((chocolates-cakes)/3)
        if cakes+omelettes+shake<items:
            continue
        if costometlette<costShake:
            omelettesReq=min(omelettes,items-cakes)
            shakeReq=items-cakes-omelettesReq
        else:
            shakeReq=min(shake,items-cakes)
            omelettesReq=items-cakes-shakeReq

        finalcost=(costCake*cakes)+(costometlette*omelettesReq)+(costShake*shakeReq)
        ans=min(ans,finalcost)
    if ans==10**18:
        print(-1)
    else:
        print(ans)

""" 
Example Input
3
5 4 4 2 2 2
4 5 5 1 2 3
4 5 5 3 2 1
Example Output
-1
7
4 
"""