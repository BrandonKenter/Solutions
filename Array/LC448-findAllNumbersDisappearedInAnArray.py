class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = abs(nums[idx]) * -1
        
        disappeared = []
        for i, num in enumerate(nums):
            if num > 0:
                disappeared.append(i + 1)
        return disappeared