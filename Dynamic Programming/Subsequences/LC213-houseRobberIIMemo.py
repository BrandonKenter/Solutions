class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
    
    def rob_helper(self, nums):
        dp = {}
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        def helper(i):
            if i in dp: 
                return dp[i]
            
            left = helper(i - 1)
            right = helper(i - 2) + nums[i]
            dp[i] = max(left, right)
            return dp[i]
        return helper(len(nums) - 1)