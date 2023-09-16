class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zeroCount = maxi = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi
        
