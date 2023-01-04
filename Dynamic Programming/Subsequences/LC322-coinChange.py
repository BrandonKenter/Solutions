'''
Memoization
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for col in range(amount + 1)] for row in range(n)]

        def helper(i, w):
            if w < 0:
                return float('inf')
            if i == 0:
                if w % coins[i] == 0:
                    return w // coins[i]
                else:
                    return float('inf')
            if dp[i][w] != -1:
                return dp[i][w]
            
            take = 1 + helper(i, w-coins[i])
            not_take = 0 + helper(i-1, w)
            dp[i][w] = min(take, not_take)
            return dp[i][w]
        
        res = helper(n-1, amount)
        return res if res != float('inf') else -1


'''
Tabulation
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for col in range(amount + 1)] for row in range(n)]

        for w in range(amount + 1):
            if w % coins[0] == 0:
                dp[0][w] = w // coins[0]
            else:
                dp[0][w] = float('inf')
        
        for i in range(1, n):
            for w in range(amount + 1):
                take = float('inf')
                take = 1 + dp[i][w-coins[i]] if coins[i] <= w else float('inf')
                not_take = 0 + dp[i-1][w]
                dp[i][w] = min(take, not_take)
                
        res = dp[n-1][amount]
        return res if res != float('inf') else -1