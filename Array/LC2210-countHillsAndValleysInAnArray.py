class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i-1]: continue
            left, right = i - 1, i + 1
            while left >= 0:
                if nums[left] != nums[i]: break
                left -= 1
            while right < len(nums) - 1:
                if nums[right] != nums[i]: break
                right += 1
            
            if left < 0 or right > len(nums) - 1:
                continue
            if nums[left] < nums[i] > nums[right]:
                cnt += 1
            elif nums[left] > nums[i] < nums[right]:
                cnt += 1
        return cnt
        