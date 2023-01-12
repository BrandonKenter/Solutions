'''
Memoization
'''
def getMaxPathSum(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[-1 for col in range(n)] for row in range(m)]
    
    def helper(i, j):
        if j < 0 or j > n-1: return float('-inf')
        if i == 0: return matrix[i][j]
        if dp[i][j] != -1: return dp[i][j]
        
        up = helper(i-1, j)
        up_left = helper(i-1, j-1)
        up_right = helper(i-1, j+1)
        dp[i][j] = matrix[i][j] + max(up, up_left, up_right)
        return dp[i][j]
    
    maxi = float('-inf')
    for j in range(n):
        maxi = max(maxi, helper(m-1, j))
    return maxi


'''
Tabulation
'''
def getMaxPathSum(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[-1 for col in range(n)] for row in range(m)]
    
    for j in range(n): dp[0][j] = matrix[0][j]
    
    for i in range(1, m):
        for j in range(n):
            up = dp[i-1][j]
            up_left = dp[i-1][j-1] if j > 0 else float('-inf')
            up_right = dp[i-1][j+1] if j < n-1 else float('-inf')
            dp[i][j] = matrix[i][j] + max(up, up_left, up_right)
    return max(dp[m-1])