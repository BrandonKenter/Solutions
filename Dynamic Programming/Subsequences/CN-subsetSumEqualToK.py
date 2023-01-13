'''
Memoization
'''
def subsetSumToK(n, k, nums):
    dp = [[None for col in range(k+1)] for row in range(n)]
    
    def helper(i, k):
        if k < 0: return False
        if k == 0: return True
        if i == 0: return nums[0] == k
        if dp[i][k] is not None: return dp[i][k]
    
        take = helper(i-1, k-nums[i])
        skip = helper(i-1, k)
        dp[i][k] = take or skip
        return dp[i][k]
    return helper(n-1, k)


'''
Tabulation
'''
def subsetSumToK(n, k, nums):
    dp = [[None for col in range(k+1)] for row in range(n)]
    
    for i in range(n): dp[i][0] = True
    for k in range(1, k+1): dp[0][k] = False
    if nums[0] <= k: dp[0][nums[0]] = True
    
    for i in range(1, n):
        for k in range(1, k+1):
            take = dp[i-1][k-nums[i]] if k >= nums[i] else False
            skip = dp[i-1][k]
            dp[i][k] = take or skip
    return dp[n-1][k]
