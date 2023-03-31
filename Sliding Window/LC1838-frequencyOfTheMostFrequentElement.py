class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxi = s = left = 0
        for right in range(len(nums)):
            s += nums[right]
            ops_needed = (nums[right] * (right - left + 1)) - s 
            if ops_needed <= k:
                maxi = max(maxi, right - left + 1)
            else:
                s -= nums[left]
                left += 1
        return maxi    
