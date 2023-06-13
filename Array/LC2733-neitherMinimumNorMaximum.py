class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mini, maxi = min(nums), max(nums)
        for num in nums:
            if num != mini and num != maxi:
                return num
        return -1
        