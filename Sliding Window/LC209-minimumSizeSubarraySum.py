class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        win_sum = 0

        left = 0
        for right in range(len(nums)):
            win_sum += nums[right]
            while win_sum >= target:
                min_len = min(min_len, right - left + 1)
                win_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0