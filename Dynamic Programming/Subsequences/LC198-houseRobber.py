'''
Memoization
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def helper(i):
            if i == 0: return nums[0]
            if i == 1: return max(nums[0], nums[1])
            if dp[i] != -1: return dp[i]

            take = nums[i] + helper(i-2)
            skip = 0 + helper(i-1)
            dp[i] = max(take, skip)
            return dp[i]
        return helper(n-1)


'''
Tabulation
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if n == 1: return nums[0]

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            take = nums[i] + dp[i-2]
            skip = 0 + dp[i-1]
            dp[i] = max(take, skip)
        return dp[n-1]