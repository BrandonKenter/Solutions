class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        left_maxi = [float('-inf')] * len(nums)
        right_mini = [float('inf')] * len(nums)
        for i in range(1, len(nums) - 1): 
            left_maxi[i] = max(left_maxi[i-1], nums[i-1])
        for i in range(len(nums) - 2, 0, -1):
            right_mini[i] = min(right_mini[i+1], nums[i+1])
            
        count = 0
        for i in range(1, len(nums) - 1):
            if left_maxi[i] < nums[i] and right_mini[i] > nums[i]:
                count += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                count += 1
        return count
        