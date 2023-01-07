'''
Memoization
'''
def canYouMake(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[-1 for col in range(n)] for row in range(m)]

    def helper(i, j):
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == t[j]:
            dp[i][j] = 1 + helper(i-1, j-1)
        else:
            dp[i][j] = max(helper(i-1, j), helper(i, j-1))
        return dp[i][j]
        
    LCS = helper(m-1, n-1)
    deletions = len(s) - LCS
    insertions = len(t) - LCS
    return deletions + insertions


'''
Tabulation
'''
def canYouMake(s: str, t: str) -> int:    
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
 
    LCS = dp[m][n]
    deletions = len(s) - LCS
    insertions = len(t) - LCS
    return deletions + insertions