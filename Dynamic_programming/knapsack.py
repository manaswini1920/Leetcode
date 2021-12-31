def knapsack(profits,weights,capacity):
    dp=[[-1 for i in range(capacity+1)]for j in range(len(profits))]
    return knap_recur(dp,profits,weights,capacity,0)
def knap_recur(dp,profits,weights,capacity,i):
    #base case
    if capacity<=0 or i>=len(profits):
        return 0
    #check if subprob solution exists
    if dp[i][capacity]!=-1:
        return dp[i][capacity]
    #check the weight
    profit1=0
    if weights[i]<=capacity:
        profit1=profits[i]+knap_recur(dp,profits,weights,capacity-weights[i],i+1)
    profit2=knap_recur(dp,profits,weights,capacity,i+1)
    dp[i][capacity]=max(profit1,profit2)
    return dp[i][capacity]

print(knapsack([4,5,3,7], [2,3,1,4], 5))