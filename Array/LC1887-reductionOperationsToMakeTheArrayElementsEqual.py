class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res, less_count, prev = 0, 0, nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                less_count += 1
            res += less_count
        return res
