'''
Memoization
'''
def subsetSumToK(n, k, arr):
    dp = [[None for col in range(k + 1)] for row in range(n)]
    
    def helper(i, k):
        if k == 0:
            return True
        if k < 0:
            return False
        if i == 0:
            return arr[i] == k
        if dp[i][k]:
            return dp[i][k]
        
        pick = helper(i-1, k-arr[i])
        not_pick = helper(i-1,k)
        dp[i][k] = pick or not_pick
        return dp[i][k]
    return helper(n-1,k)


'''
Tabulation
'''
def subsetSumToK(n, k, arr):
    dp = [[False for col in range(k + 1)] for row in range(n)]
    
    for i in range(n):
        dp[i][0] = True
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    for i in range(1, n):
        for k in range(1, k + 1):
            take = dp[i-1][k-arr[i]] if k >= arr[i] else False
            not_take = dp[i-1][k]
            dp[i][k] = take or not_take
    return dp[n-1][k]