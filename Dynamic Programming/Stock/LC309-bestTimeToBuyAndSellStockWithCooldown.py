'''
Memoization
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for col in range(2)] for row in range(n)]

        def helper(i, buy):
            if i >= n: return 0
            if dp[i][buy] != -1: return dp[i][buy]

            profit = 0
            if buy:
                profit = max(-prices[i] + helper(i+1, 0), 0 + helper(i+1, 1))
            else:
                profit = max(prices[i] + helper(i+2, 1), 0 + helper(i+1, 0))
            dp[i][buy] = profit
            return dp[i][buy]
        return helper(0, 1)


'''
Tabulation
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for col in range(2)] for row in range(n + 2)]

        dp[n][0] = dp[n][1] = 0

        for i in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[i] + dp[i+1][0], 0 + dp[i+1][1])
                else:
                    profit = max(prices[i] + dp[i+2][1], 0 + dp[i+1][0])
                dp[i][buy] = profit
        return dp[0][1]