# Template 2
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right-left) // 2
            print(mid)
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


# Template 1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                return min(min_val, nums[left])
            
            mid = left + (right - left) // 2
            min_val = min(min_val, nums[mid])
            
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return min_val
