class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = {}
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        return self.rob_helper(len(nums) - 1, dp, nums)
        
    def rob_helper(self, i, dp, nums):
        if i in dp:
            return dp[i]
        
        dp[i] = max(nums[i] + self.rob_helper(i - 2, dp, nums), self.rob_helper(i - 1, dp, nums))
        return dp[i]