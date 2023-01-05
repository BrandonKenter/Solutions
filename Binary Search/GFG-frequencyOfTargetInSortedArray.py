class Solution:
    def count(self,arr, n, x):
        left = self.find_index(arr, x, True)
        right = self.find_index(arr, x, False)
        return right - left + 1 if left != -1 else 0
	
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