class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_to_i = defaultdict(int)
        for i, num in enumerate(nums):
            num_to_i[num] = i
        
        for re, num in operations:
            i = num_to_i[re]
            nums[i] = num
            num_to_i[num] = i
        return nums
