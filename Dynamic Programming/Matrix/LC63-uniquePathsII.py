'''
Memoization
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1 for col in range(n)] for row in range(m)]

        def helper(i, j):
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1 : return 0
            if i == 0 and j == 0: return 1
            if dp[i][j] != -1: return dp[i][j]

            up = helper(i-1, j)
            left = helper(i, j-1)
            dp[i][j] = up + left
            return dp[i][j]
        return helper(m-1, n-1)


'''
Tabulation - Seeding base cases before iterative procedure 
I prefer this method because it follows the base case translation that I
use for most problems.
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for col in range(n)] for row in range(m)]
        
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m): dp[i][0] = 1 if dp[i-1][0] and not obstacleGrid[i][0] else 0
        for j in range(1, n): dp[0][j] = 1 if dp[0][j-1] and not obstacleGrid[0][j] else 0 

        for i in range(1, m):
            for j in range(1, n):
                up = dp[i-1][j]
                left = dp[i][j-1]
                dp[i][j] = up + left if obstacleGrid[i][j] != 1 else 0
        return dp[m-1][n-1]


'''
Tabulation - Encoding base cases into for loop
This is kind of an ad hoc approach. We want the inside of the double for
loop to look like the memoization approach, which it does not here. This 
is why I prefer the above approach. 
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for col in range(n)] for row in range(m)]

        if obstacleGrid[0][0] == 1: return 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    up = dp[i-1][j] if i > 0 else 0
                    left = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + left
        return dp[m-1][n-1]