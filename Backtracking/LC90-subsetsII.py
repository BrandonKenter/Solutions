class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return res