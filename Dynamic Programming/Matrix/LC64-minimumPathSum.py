'''
Memoization
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for col in range(n)] for row in range(m)]

        def helper(i, j):
            if i < 0 or j < 0: return float('inf')
            if i == 0 and j == 0: return grid[i][j]
            if dp[i][j] != -1: return dp[i][j]

            up = helper(i-1, j)
            left = helper(i, j-1)
            dp[i][j] = grid[i][j] + min(up, left)
            return dp[i][j]
        return helper(m-1, n-1)


'''
Tabulation - Seeding base cases before iterative procedure 
I prefer this method because it follows the base case translation that I
use for most problems.
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for col in range(n)] for row in range(m)]

        dp[0][0] = grid[0][0]
        for i in range(1, m): dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n): dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                up = dp[i-1][j]
                left = dp[i][j-1]
                dp[i][j] = grid[i][j] + min(up, left)
        return dp[m-1][n-1]


'''
Tabulation - Encoding base cases into for loop
This is kind of an ad hoc approach. We want the inside of the double for
loop to look like the memoization approach, which it does not here. This 
is why I prefer the above approach. 
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for col in range(n)] for row in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    up = grid[i][j] + dp[i-1][j] if i > 0 else float('inf')
                    left = grid[i][j] + dp[i][j-1] if j > 0 else float('inf')
                    dp[i][j] = min(up, left)
        return dp[m-1][n-1]