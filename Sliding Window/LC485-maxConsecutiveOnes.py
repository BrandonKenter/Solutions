class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            max_consec = max(max_consec, right - left + 1)
        return max_consec
    
