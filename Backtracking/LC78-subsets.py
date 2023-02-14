class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize result collecction
        res = []
        # Initialize state collection
        subset = []
        
        # Create backtracking method
        # State parameters: 
        #   - i where i is the index of the nums array
        def backtrack(i):
            # Check if state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if i == len(nums):
                res.append(subset[:])
                return

            # State is valid, so can proceed to make choice on this state
            # Reflect current choice in state collection
            subset.append(nums[i])
            # Recurse on next choice space of next state
            backtrack(i+1)
            # Clean up current choice (backtrack)
            subset.pop()
            
            # Recurse on choice space of next state
            # Current choice to NOT include nums[i]
            backtrack(i+1)
            
        backtrack(0)
        return res
