'''
Memoization
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        dp = {}

        def helper(i, j):
            if i < 0 and j < 0:
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            
            take_s1 = helper(i-1, j) if (i >= 0) and  s1[i] == s3[i + j + 1] else False
            take_s2 = helper(i, j-1) if (j >= 0) and s2[j] == s3[i + j + 1] else False
            dp[(i, j)] = take_s1 or take_s2
            return dp[(i, j)]
        
        return helper(len(s1) - 1, len(s2) - 1)

'''
Tabulation
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s1) + len(s2) != len(s3): return False
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1): dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n + 1): dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                take_s1 = dp[i-1][j] if s1[i-1] == s3[i + j - 1] else False
                take_s2 = dp[i][j-1] if s2[j-1] == s3[i + j - 1] else False
                dp[i][j] = take_s1 or take_s2
        return dp[m][n]
        