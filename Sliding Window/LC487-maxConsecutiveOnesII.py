class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec = zero_count = left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count == 2:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_consec = max(max_consec, right - left + 1)
        return max_consec