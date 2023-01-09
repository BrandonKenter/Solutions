'''
Memoization
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for z in range(3)] for y in range(2)] for x in range(n)]

        def helper(i, buy, cap):
            if i == n or cap == 0: return 0

            if dp[i][buy][cap] != -1: return dp[i][buy][cap]

            profit = 0
            if buy:
                profit = max(-prices[i] + helper(i+1, 0, cap), 0 + helper(i+1, 1, cap))
            else:
                profit = max(prices[i] + helper(i+1, 1, cap - 1), 0 + helper(i+1, 0, cap))
            dp[i][buy][cap] = profit
            return dp[i][buy][cap]
        return helper(0, 1, 2)


'''
Tabulation
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for z in range(3)] for y in range(2)] for x in range(n + 1)]

        # We don't need these to translate the base cases to seed the dp table
        # because the dp table is initialzied to 0 already, but I wrote them 
        # anyway for clarity of understanding how the tabulation works.
        for buy in range(2):
            for cap in range(3):
                dp[n][buy][cap] = 0
        for i in range(n):
            for buy in range(2):
                dp[i][buy][0] = 0
        

        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    profit = 0
                    if buy:
                        profit = max(-prices[i] + dp[i+1][0][cap], 0 + dp[i+1][1][cap])
                    else:
                        profit = max(prices[i] + dp[i+1][1][cap-1], 0 + dp[i+1][0][cap])
                    dp[i][buy][cap] = profit
        return dp[0][1][2]


'''
Tabulation - O(1) space
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        after = [[0 for col in range(3)] for row in range(2)]
        cur = [[0 for col in range(3)] for row in range(2)]

        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    profit = 0
                    if buy:
                        profit = max(-prices[i] + after[0][cap], 0 + after[1][cap])
                    else:
                        profit = max(prices[i] + after[1][cap-1], 0 + after[0][cap])
                    cur[buy][cap] = profit
            after = cur
        return after[1][2]