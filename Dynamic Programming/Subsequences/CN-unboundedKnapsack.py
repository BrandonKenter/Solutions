'''
Memoization
'''
def unboundedKnapsack(n, w, profit, weight):
    dp = [[-1 for col in range(w + 1)] for row in range(n)]

    def helper(i, t):
        if t < 0:
            return float('-inf')
        if i == 0:
            if weight[0] <= t:
                return profit[0] * (t // weight[0])
            else:
                return 0
        if dp[i][t] != -1:
            return dp[i][t]

        take = profit[i] + helper(i,t-weight[i])
        not_take = 0 + helper(i-1, t)
        dp[i][t] = max(take, not_take)
        return dp[i][t]
    return helper(n-1, w)


'''
Tabulation
'''
def unboundedKnapsack(n, w, profit, weight):
    dp = [[-1 for col in range(w + 1)] for row in range(n)]
        
    for t in range(w + 1):
        if weight[0] <= t:
            dp[0][t] = profit[0] * (t // weight[0])
        else:
            dp[0][t] = 0
            
    for i in range(1, n):
        for t in range(w + 1):
            take = profit[i] + dp[i][t-weight[i]] if weight[i] <= t else float('-inf')
            not_take = 0 + dp[i-1][t]
            dp[i][t] = max(take, not_take)
    return dp[n-1][w]