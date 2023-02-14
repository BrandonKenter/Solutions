class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        
        def backtrack(i):
            # State is a solution, so add it to solution collection
            if i == len(nums):
                res.append(subset[:])
                return
            
            # Make next choice from current state by calling backtrack
            # on i + 1
            subset.append(nums[i])
            backtrack(i+1)
            
            # Clean up decision
            subset.pop()
            
            # Make next choice from current state by calling backtrack
            # on i + 1 WITHOUT nums[i]
            backtrack(i+1)
        backtrack(0)
        return res
