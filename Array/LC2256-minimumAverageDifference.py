class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float('inf')
        mini_i = 0
        right_s = sum(nums)
        left_s = 0
        for i in range(len(nums)):
            right_s -= nums[i]
            left_s += nums[i]
            left_avg = left_s // (i + 1)
            right_avg = right_s // (n - i - 1) if i != len(nums) - 1 else 0
            dif = abs(left_avg - right_avg)
            if dif < mini:
                mini = dif
                mini_i = i
        return mini_i
