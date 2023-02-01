class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        
        def backtrack(i):
            # Current state is a solution, so append to res
            if i == len(nums):
                res.append(subset[:])
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            
            # Decision to NOT include nums[i]
            backtrack(i+1)
        backtrack(0)
        return res