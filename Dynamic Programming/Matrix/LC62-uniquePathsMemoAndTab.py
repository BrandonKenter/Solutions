class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        dp[(0, 0)] = 1

        def helper(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i < 0 or j < 0:
                return 0
            
            left = helper(i, j - 1)
            up = helper(i - 1, j)
            dp[(i, j)] = left + up
            return dp[(i, j)] 
        return helper(m - 1, n - 1)
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for c in range(n)] for r in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                else:
                    left = dp[i][j-1] if j > 0 else 0
                    up = dp[i - 1][j] if i > 0 else 0
                    dp[i][j] = left + up
        return dp[m-1][n-1]

        