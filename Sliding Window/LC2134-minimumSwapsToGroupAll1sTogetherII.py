class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        one_count = 0
        for num in nums:
            one_count += 1 if num == 1 else 0
        nums = nums * 2

        zero_count = 0
        min_count = float('inf')
        l = r = 0
        while r < len(nums):
            zero_count += 1 if nums[r] == 0 else 0
            if r - l + 1 == one_count:
                min_count = min(min_count, zero_count)
                zero_count -= 1 if nums[l] == 0 else 0
                l += 1
            r += 1
        return min_count if min_count != float('inf') else 0
    