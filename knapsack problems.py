def max_profits(profit,weight,capacity):
    pass

def max_profit_recursive(weights,profits,capacity,idx=0):
    if idx==len(weights):
        return 0
    elif weights[idx]>capacity:
        return max_profit_recursive(weights,profits,capacity,idx+1)
    else:
        option1 =max_profit_recursive(weights,profits,capacity,idx+1) #ignoring the element because it might not be optimal
        option2 =profits[idx]+max_profit_recursive(weights,profits,capacity-weights[idx],idx+1)

        return max(option1,option2)

def knapsack_memo(capacity,weights,profits,):
    memo={}
    def recurse(idx,remaining):
        key=(idx,remaining)

        if key in memo:
            return memo[key]
        elif idx==len(weights):
            memo[key]=0
        elif weights[key]>remaining:
            memo[key]=recurse(idx+1,remaining)
        else:
            memo[key]=max(recurse(idx+1,remaining),profits[idx]+recurse(idx+1,remaining-weights[idx]))

        return memo[key]
    return recurse(0,capacity)


def knapsack_dp(weights,profits,capacity):
    n=len(weights)
    table=[[0 for x in range(capacity+1)]for x in range(n+1)]

    for i in range(n):
        for c in range(1,capacity+1):
            if weights[i]>capacity:
                table[i+1][c]=table[i][c]
            else:
                option1=table[i][c]  #not optimal solution so taking previous value
                option2=profits[i]+table[i][c-weights[i]]
                table[i+1][c]=max(option1,option2)
    return table[-1][-1]

