'''
Memoization
'''
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[-1 for col in range(n)] for row in range(m)]

        def helper(i, j):
            if i < 0: return j + 1
            if j < 0: return i + 1
            if dp[i][j] != -1: return dp[i][j]

            if s[i] == t[j]: 
                dp[i][j] = 0 + helper(i-1, j-1)
                return dp[i][j]
            else:
                insert = 1 + helper(i, j-1)
                delete = 1 + helper(i-1, j)
                replace = 1 + helper(i-1, j-1)
                dp[i][j] = min(insert, delete, replace)
                return dp[i][j]
        return helper(m-1, n-1)


'''
Tabulation
'''
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[-1 for col in range(n + 1)] for row in range(m + 1)]

        for i in range(m + 1): dp[i][0] = i 
        for j in range(n + 1): dp[0][j] = j 

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 0 + dp[i-1][j-1]
                else:
                    insert = 1 + dp[i][j-1]
                    delete = 1 + dp[i-1][j]
                    replace = 1 + dp[i-1][j-1]
                    dp[i][j] = min(insert, delete, replace)
        return dp[m][n]