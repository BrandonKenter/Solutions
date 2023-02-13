# Template 2
# Find minimal k where isCondition(k) is True
# isCondition is "if value at this index >= target"
# F F T T T T T <- find first index that is TRUE
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
