class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        memo[0] = cost[0]
        memo[1] = cost[1]
        n = len(cost)
        return min(self.helper(n - 1, cost, memo), self.helper(n - 2, cost, memo))

    def helper(self, i, cost, memo):
        if i in memo: return memo[i]

        left = self.helper(i - 1, cost, memo)
        right = self.helper(i - 2, cost, memo)
        memo[i] = cost[i] + min(left, right)
        return memo[i]
