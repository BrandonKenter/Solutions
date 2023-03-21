class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 1
        for num in nums:
            cur = 1
            while num * num in nums_set:
                num *= num
                cur += 1
            longest = max(longest, cur)
        return longest if longest >= 2 else -1
                