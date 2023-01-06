'''
Memoization
'''
class Solution:
    def knapsack(self, weights: List[int], profits: List[int], n: int, maxWeight: int):   
        dp = [[-1 for col in range(maxWeight + 1)] for row in range(n)]
        
        def helper(i, w):
            if w < 0:
                return float('-inf')
            if i == 0:
                if weights[0] <= w:
                    return profits[0]
                else:
                    return 0
            if dp[i][w] != -1:
                return dp[i][w]
            
            take = profits[i] + helper(i, w-weights[i])
            not_take = 0 + helper(i-1, w)
            dp[i][w] = max(take, not_take)
            return dp[i][w]
        return helper(n-1, maxWeight)


'''
Tabulation
'''
class Solution:
    def knapsack(self, weights: List[int], profits: List[int], n: int, maxWeight: int):    
        dp = [[-1 for col in range(maxWeight + 1)] for row in range(n)]
        
        for w in range(maxWeight + 1):
            if weights[0] <= w:
                dp[0][w] = profits[0] * (w // weights[0])
            else:
                dp[0][w] = 0
            
        for i in range(1, n):
            for w in range(maxWeight + 1):
                take = profits[i] + dp[i][w-weights[i]] if weights[i] <= w else float('-inf')
                not_take = 0 + dp[i-1][w]
                dp[i][w] = max(take, not_take)
        return dp[n-1][maxWeight]