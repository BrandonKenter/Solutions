'''
Memoization
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        n, dp = len(s), {}

        def helper(i):
            if i <= 0:
                return 1
            if i in dp:
                return dp[i]
            
            take_1 = helper(i-1) if s[i] != '0' else 0
            take_2 = helper(i-2) if i >= 1 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26 else 0
            dp[i] = take_1 + take_2
            return dp[i]
        
        return helper(n-1)

'''
Tabulation
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        n, dp = len(s), [-1 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            take_1 = dp[i-1] if s[i-1] != '0' else 0
            take_2 = dp[i-2] if s[i-2] != '0' and int(s[i-2:i]) <= 26 else 0
            dp[i] = take_1 + take_2
        return dp[n]