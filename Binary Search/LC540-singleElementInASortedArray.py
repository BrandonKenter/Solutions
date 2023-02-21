class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if mid % 2 == 0:
                if nums[mid + 1] != nums[mid]:
                    right = mid 
                else:
                    left = mid + 1
            else:
                if nums[mid - 1] != nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        return nums[left]