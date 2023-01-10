'''
Memoization
'''
class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)

        def helper(i):
            if i == 0: return 0
            if i == 1: return 1
            if dp[i] != -1: return dp[i]

            dp[i] = helper(i-1) + helper(i-2)
            return dp[i]
        return helper(n)


'''
Tabulation
'''
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n

        dp = [0] * (n+1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]