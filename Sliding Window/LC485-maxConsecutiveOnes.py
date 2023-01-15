class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_conseq = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 1: 
                max_conseq = max(max_conseq, right - left + 1)
            else:
                left = right + 1
        return max_conseq