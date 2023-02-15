class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Initialize result collection
        res = []
        # Initialize state collection
        perm = []
        used = [False] * len(nums)
        
        # Create backtracking method
        # No state parameters because we iterate starting from 0 
        # for each choice
        def backtrack():
            # Check if current state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for i in range(len(nums)):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if used[i]:
                    continue
                # Choice meets constraints
                # Reflect current choice in state collection
                used[i] = True
                perm.append(nums[i])
                # Recurse on next choice space of next state
                backtrack()
                # Clean up current choice (backtrack)
                used[i] = False
                perm.pop()

        backtrack()
        return res