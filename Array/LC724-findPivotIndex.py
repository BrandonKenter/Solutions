class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r_sum = sum(nums)
        l_sum = 0
        
        for i in range(len(nums)):
            r_sum -= nums[i]
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1
    