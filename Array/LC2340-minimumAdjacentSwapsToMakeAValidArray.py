class Solution:
    def minimumSwaps(self, nums: List[int]) -> int: 
        min_val, min_i, max_val, max_i = float('inf'), -1, float('-inf'), -1
        for i, num in enumerate(nums):
            if num < min_val:
                min_val, min_i = num, i
            if num >= max_val:
                max_val, max_i = num, i
        
        swaps = (min_i - 0) + (len(nums) - 1 - max_i)
        if min_i > max_i: swaps -= 1
        return swaps