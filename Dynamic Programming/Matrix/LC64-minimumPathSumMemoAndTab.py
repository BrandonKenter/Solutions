'''
Memoization
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for col in range(n)] for row in range(m)]

        def helper(i, j):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
                return dp[i][j]
            if i < 0 or j < 0:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]

            
            left = grid[i][j] + helper(i,j-1)
            top = grid[i][j] + helper(i-1, j)
            dp[i][j] = min(left, top)
            return dp[i][j]
        
        return helper(m-1, n-1)

'''
Tabulation
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for col in range(n)] for row in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    left = grid[i][j] + dp[i][j-1] if j > 0 else float('inf')
                    top = grid[i][j] + dp[i-1][j] if i > 0 else float('inf')
                    dp[i][j] = min(left, top)
        
        return dp[m-1][n-1]