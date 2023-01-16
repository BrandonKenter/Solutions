class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = zero_count = left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count == 2:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            longest = max(longest, right - left)
        return longest