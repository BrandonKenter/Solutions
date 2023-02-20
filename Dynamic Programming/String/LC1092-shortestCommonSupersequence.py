'''
Tabulation
'''
class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        dp = [[-1 for col in range(n + 1)] for row in range(m + 1)]

        for i in range(m + 1): dp[i][0] = 0
        for j in range(n + 1): dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        i, j = m, n
        ans = []
        while i > 0 and j > 0:
            if s[i-1] == t[j-1]:
                ans.append(s[i-1])
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    ans.append(s[i-1])
                    i = i - 1
                else:
                    ans.append(t[j-1])
                    j = j - 1
        while i > 0: 
            ans.append(s[i-1])
            i -= 1
        while j > 0:
            ans.append(t[j-1])
            j -= 1
        return "".join(ans)[::-1]
