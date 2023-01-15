'''
We have to find the indices of the leftmost instance of 
the minimum element and the rightmost instance of the maximum
element. The difference between leftmost and rightmost is 
why we use < and >= for the min/max val comparisons (we don't 
want to update min if it is equal to previous min, but we want 
to update max if it is equal to previous max). The number of 
swaps is just the distance to the ends of the array. And when 
the min/max values have to cross each other to get to their 
respective sides, it takes 1 swap instead of 2 so we decrement 
swaps by 1 in that case.

Time: O(N)
Space: O(1)
'''
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
