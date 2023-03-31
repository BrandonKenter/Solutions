class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(1, len(nums)):
            diff = nums[i-1] - nums[i]
            if diff >= 0:
                ops += diff + 1
                nums[i] = nums[i-1] + 1
        return ops
        