class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = -1
        least_dif = float('inf')

        for left in range(len(nums) - 2):
            mid, right = left + 1, len(nums) - 1
            while mid < right:
                cur_sum = nums[left] + nums[mid] + nums[right]
                dif = abs(target - cur_sum)
                if dif < least_dif:
                    least_dif = dif
                    closest = cur_sum
                if cur_sum < target:    
                    mid += 1
                else:
                    right -= 1
        return closest