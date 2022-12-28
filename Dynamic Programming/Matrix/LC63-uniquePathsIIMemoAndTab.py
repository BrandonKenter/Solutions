'''
Memoization
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1 for col in range(n)] for row in range(m)]

        if obstacleGrid[0][0] == 1: return 0

        def helper(i, j):
            if i == 0 and j == 0:
                dp[0][0] = 1
                return dp[i][j]
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            
            left = helper(i, j - 1)
            top = helper(i - 1, j)
            dp[i][j] = left + top
            return dp[i][j]
        
        return helper(m - 1, n - 1)

'''
Tabulation
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1 for col in range(n)] for row in range(m)]

        if obstacleGrid[0][0] == 1: return 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    left = dp[i][j-1] if j > 0 else 0
                    top = dp[i-1][j] if i > 0 else 0
                    dp[i][j] = left + top
                    
        return dp[m-1][n-1]