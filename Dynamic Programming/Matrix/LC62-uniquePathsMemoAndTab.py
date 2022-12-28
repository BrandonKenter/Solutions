'''
Memoization - Hash map cache and no base case for starting cell (DP seeded)
'''
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
    
'''
Memoization - Matrix cache and base case for starting cell (better imo)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for col in range(n)] for row in range(m)]

        def helper(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i == 0 and j == 0:
                dp[0][0] = 1
                return dp[0][0]
            if i < 0 or j < 0:
                return 0
            
            left = helper(i, j - 1)
            up = helper(i - 1, j)
            dp[i][j] = left + up
            return dp[i][j]

        return helper(m - 1, n - 1)

'''
Tabulation
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for col in range(n)] for row in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                else:
                    left = dp[i][j-1] if j > 0 else 0
                    up = dp[i - 1][j] if i > 0 else 0
                    dp[i][j] = left + up

        return dp[m-1][n-1]

        
