'''
Memoization
'''
def cutRod(prices, maxWeight):
    n = len(prices)
    dp = [[-1 for col in range(maxWeight + 1)] for row in range(n)]
    
    def helper(i, w):
        rod_len = i + 1
        if w < 0:
            return float('-inf')
        if i == 0:
            if i + 1 <= w:
                return prices[i] * (w // rod_len)
            else:
                return 0
        if dp[i][w] != -1:
            return dp[i][w]
        
        take = prices[i] + helper(i, w-rod_len)
        not_take = 0 + helper(i-1, w)
        dp[i][w] = max(take, not_take)
        return dp[i][w]
    return helper(n - 1, maxWeight)


'''
Tabulation
'''
def cutRod(prices, maxWeight):
    n = len(prices)
    dp = [[-1 for col in range(maxWeight + 1)] for row in range(n)]
    
    for w in range(maxWeight + 1):
        # 1 is the length of the 0th index rod
        if 1 <= w:
            dp[0][w] = prices[0] * (w // 1) # explicitly using "// 1" for easier understanding
        else:
            dp[0][w] = 0
     
    for i in range(1, n):
        for w in range(maxWeight + 1):
            rod_len = i + 1
            take = prices[i] + dp[i][w-rod_len] if rod_len <= w else float('-inf')
            not_take = 0 + dp[i-1][w]
            dp[i][w] = max(take, not_take)
    return dp[n-1][maxWeight]