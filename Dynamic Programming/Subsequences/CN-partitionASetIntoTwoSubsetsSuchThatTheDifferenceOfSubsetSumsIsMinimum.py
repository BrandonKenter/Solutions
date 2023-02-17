'''
Memoization
'''
def minSubsetSumDifference(nums, n):
    nums_sum = sum(nums)
    n, k = len(nums), nums_sum
    dp = [[None for col in range(k+1)] for row in range(n)]

    def helper(i, targ):
        if targ < 0: return False
        if targ == 0: 
            dp[i][targ] = True
            return True
        if i == 0: return nums[0] == targ
        if dp[i][targ] is not None: return dp[i][targ]

        take = helper(i-1, targ-nums[i])
        skip = helper(i-1, targ)
        dp[i][targ] = take or skip
        return dp[i][targ]
   
    for i in range((nums_sum//2)+1): 
        helper(n-1, i)
        
    mini = float('inf')                          
    for s1 in range((nums_sum//2)+1):
        if dp[n-1][s1] == True:
            mini = min(mini, abs( (nums_sum - s1) - s1))
    return mini 


'''
Tabulation
'''
def minSubsetSumDifference(nums, n):
    nums_sum = sum(nums)
    n, k = len(nums), nums_sum
    dp = [[None for col in range(k+1)] for row in range(n)]

    for i in range(n): dp[i][0] = True
    for k in range(1, k+1): dp[0][k] = True if nums[0] == k else False

    for i in range(1, n):
        for k in range(1, k+1):
            take = dp[i-1][k-nums[i]] if k >= nums[i] else False
            skip = dp[i-1][k]
            dp[i][k] = take or skip

    mini = float('inf')
    for s1 in range((nums_sum//2)+1):
        if dp[n-1][s1] == True:
            mini = min(mini, abs( (nums_sum - s1) - s1))
    return mini