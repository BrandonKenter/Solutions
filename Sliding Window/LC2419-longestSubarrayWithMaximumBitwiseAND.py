class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi = max(nums)
        longest = left = 0
        for right in range(len(nums)):
            if nums[right] == maxi:
                longest = max(longest, right - left + 1)
            else:
                left = right + 1
        return longest
        