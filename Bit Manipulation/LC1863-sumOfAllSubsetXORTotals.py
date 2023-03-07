class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def backtrack(i, cur_xor):
            nonlocal s
            if i == len(nums):
                s += cur_xor
                return
            
            backtrack(i+1, cur_xor ^ nums[i])
            backtrack(i+1, cur_xor)

        s = 0
        backtrack(0, 0)
        return s
