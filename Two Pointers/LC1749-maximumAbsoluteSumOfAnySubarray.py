class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        neg_maxi = pos_maxi = 0
        
        # Check maximum negative sum
        i = j = s = 0
        while j < len(nums):
            s += nums[j]
            if s > 0:
                i = j + 1
                s = 0
            neg_maxi = max(neg_maxi, -1 * s)
            j += 1
        
        # Check maximum positive sum
        i = j = s = 0
        while j < len(nums):
            s += nums[j]
            if s < 0:
                i = j + 1
                s = 0
            pos_maxi = max(pos_maxi, s)
            j += 1
        
        return max(neg_maxi, pos_maxi)
