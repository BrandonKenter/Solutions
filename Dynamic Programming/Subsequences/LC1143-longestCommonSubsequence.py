'''
Memoization
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1 for col in range(n)] for row in range(m)]

        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + helper(i-1, j-1)
            else:
                dp[i][j] = max(helper(i-1, j), helper(i, j-1))
            return dp[i][j]
        return helper(m-1, n-1)


'''
Tabulation
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1 for col in range(n + 1)] for row in range(m + 1)]

        for i in range(m + 1): dp[i][0] = 0
        for j in range(n + 1): dp[0][j] = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]