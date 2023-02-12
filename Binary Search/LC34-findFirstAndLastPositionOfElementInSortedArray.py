class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(is_right):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                val = nums[mid]
                if val == target:
                    if not is_right:
                        pos[0] = mid
                        right = mid - 1
                    else:
                        pos[1] = mid
                        left = mid + 1
                elif val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
        pos = [-1, -1]
        search(False)
        search(True)
        return pos
