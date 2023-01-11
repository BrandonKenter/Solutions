'''
Memoization
'''
def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1] * n
    
    def helper(i):
        if i == 0: return 0
        if i == 1: return abs(heights[1] - heights[0])
        if dp[i] != -1: return dp[i]
    
        one_jump = abs(heights[i] - heights[i-1]) + helper(i-1)
        two_jump = abs(heights[i] - heights[i-2]) + helper(i-2)
        dp[i] = min(one_jump, two_jump)
        return dp[i]
    return helper(n-1)


'''
Tabulation
'''
def frogJump(n: int, heights: List[int]) -> int:
    dp = [0] * n
    dp[0], dp[1] = 0, abs(heights[1] - heights[0])
    
    for i in range(2, n):
        one_jump = abs(heights[i] - heights[i-1]) + dp[i-1]
        two_jump = abs(heights[i] - heights[i-2]) + dp[i-2]
        dp[i] = min(one_jump, two_jump)
    return dp[n-1]
