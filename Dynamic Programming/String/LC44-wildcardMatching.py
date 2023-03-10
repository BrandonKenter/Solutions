'''
Memoization
'''
class Solution:
    def isMatch(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[False for col in range(n)] for row in range(m)]

        def helper(i, j):
            if i < 0 and j < 0: return True 
            if i >= 0 and j < 0: return False
            if i < 0 and j >= 0: return all(char == '*' for char in t[:j+1])
            if dp[i][j] != -1: return dp[i][j]

            if s[i] == t[j] or t[j] == '?':
                dp[i][j] = helper(i-1, j-1)
                return dp[i][j]
            elif t[j] == '*':
                take = helper(i-1, j)  # match * with i but don't decrement j (discard i and don't discard */j)
                skip = helper(i, j-1)  # don't match * with i and decrement j (discard */j)
                dp[i][j] = take or skip
                return dp[i][j]
            else:
                return False
        return helper(m-1, n-1)


'''
Tabulation
'''
class Solution:
    def isMatch(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[False for col in range(n + 1)] for row in range(m + 1)]

        dp[0][0] = True
        for i in range(1, m + 1): dp[i][0] = False
        for j in range(1, n + 1): dp[0][j] = all(char == '*' for char in t[:j])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1] or t[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif t[j-1] == '*':
                    take = dp[i-1][j] # match * with i but don't decrement j (discard i and don't discard */j)
                    skip = dp[i][j-1] # don't match * with i and decrement j (discard */j)
                    dp[i][j] = take or skip
                else:
                    dp[i][j] = False
        return dp[m][n]
