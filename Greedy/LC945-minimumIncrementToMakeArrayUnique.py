class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur <= prev:
                to_add = prev - cur + 1
                prev = cur + to_add
                count += to_add
            else:
                prev = cur
        return count
        