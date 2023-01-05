class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.find_index(nums, target, True), self.find_index(nums, target, False)]

    def find_index(self, nums, target, is_left):
        left, right = 0, len(nums) - 1
        idx = -1

        while left <= right:
            mid = left + (right - left) // 2
            val = nums[mid]
            if val == target:
                idx = mid
                if is_left: right = mid - 1
                else: left = mid + 1
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return idx