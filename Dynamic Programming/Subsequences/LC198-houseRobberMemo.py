class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        return self.rob_helper(len(nums) - 1, memo, nums)
        
    def rob_helper(self, i, memo, nums):
        if i in memo:
            return memo[i]
        
        memo[i] = max(nums[i] + self.rob_helper(i - 2, memo, nums), self.rob_helper(i - 1, memo, nums))
        return memo[i]