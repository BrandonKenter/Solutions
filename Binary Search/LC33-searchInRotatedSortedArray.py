# Template 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            
            # In left sorted portion
            if nums[left] <= nums[mid]:
                # Search right
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                # Search left
                else:
                    right = mid - 1
            # In right sorted portion
            else:
                # Search left
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                # Search right
                else:
                    left = mid + 1
        return -1
