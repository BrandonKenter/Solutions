'''
Memoization
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for col in range(amount + 1)] for row in range(n)]
        
        def helper(i, w):
            if w < 0:
                return 0
            if i == 0:
                if w % coins[i] == 0:
                    return 1
                else:
                    return 0
            if dp[i][w] != -1:
                return dp[i][w]
            
            take = helper(i, w-coins[i])
            not_take = helper(i-1, w)
            dp[i][w] = take + not_take
            return dp[i][w]
        return helper(n-1, amount)


'''
Tabulation
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for col in range(amount + 1)] for i in range(n)]
        
        for w in range(amount + 1):
            if w % coins[0] == 0:
                dp[0][w] = 1
            else:
                dp[0][w] = 0
        
        for i in range(1, n):
            for w in range(amount + 1):
                take = dp[i][w-coins[i]] if coins[i] <= w else 0
                not_take = dp[i-1][w]
                dp[i][w] = take + not_take
        return dp[n-1][amount]