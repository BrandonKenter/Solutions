'''
Memoization
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n

        def helper(i):
            if i == 0: return cost[0]
            if i == 1: return cost[1]
            if dp[i] != -1: return dp[i]

            dp[i] = cost[i] + min(helper(i-1), helper(i-2))
            return dp[i]
        return min(helper(n-1), helper(n-2))


'''
Tabulation
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])