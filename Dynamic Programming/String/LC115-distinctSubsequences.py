'''
Memoization
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[-1 for col in range(n)] for row in range(m)]

        def helper(i, j):
            if i < 0 and j >= 0: return 0
            if j < 0: return 1
            if dp[i][j] != -1: return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] = helper(i-1, j-1) + helper(i-1, j)
            else:
                dp[i][j] = helper(i-1, j)
            return dp[i][j]
        return helper(m-1, n-1)


'''
Tabulation
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[-1 for col in range(n + 1)] for row in range(m + 1)]

        for i in range(m + 1): dp[i][0] = 1
        for j in range(1, n + 1): dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]