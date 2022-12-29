'''
Memoization
'''
def getMaxPathSum(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[-1 for col in range(n)] for row in range(m)]
    
    def helper(i, j):
        if j < 0 or j >= n:
            return float('-inf')
        if i == 0:
            dp[i][j] = matrix[i][j]
            return dp[i][j]
        
        top_l = matrix[i][j] + helper(i-1, j-1)
        top_m = matrix[i][j] + helper(i-1, j)
        top_r = matrix[i][j] + helper(i-1, j+1)
        dp[i][j] = max(top_l, top_m, top_r)
        return dp[i][j]
    
    max_path = float('-inf')
    for j in range(n):
        max_path = max(max_path, helper(m-1, j))
    return max_path

'''
Tabulation
'''
def getMaxPathSum(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[-1 for col in range(n)] for row in range(m)]
    
    for j in range(n):
        dp[0][j] = matrix[0][j]
    
    for i in range(1, m):
        for j in range(n):
            top_l = matrix[i][j] + dp[i-1][j-1] if j > 0 else float('-inf')
            top_m = matrix[i][j] + dp[i-1][j] 
            top_r = matrix[i][j] + dp[i-1][j+1] if j < n - 1 else float('-inf')
            dp[i][j] = max(top_l, top_m, top_r)
    return max(dp[m-1])