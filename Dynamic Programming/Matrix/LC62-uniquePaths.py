'''
Memoization
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for col in range(n)] for row in range(m)]

        def helper(i, j):
            if i < 0 or j < 0: return 0
            if i == 0 and j == 0: return 1
            if dp[i][j] != -1: return dp[i][j]

            up = helper(i-1, j)
            left = helper(i, j-1)
            dp[i][j] = up + left
            return dp[i][j]
        return helper(m-1, n-1)


'''
Tabulation
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for col in range(n)] for row in range(m)]
        for i in range(m): dp[i][0] = 1
        for j in range(n): dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                up = dp[i-1][j]
                left = dp[i][j-1]
                dp[i][j] = up + left
        return dp[m-1][n-1]