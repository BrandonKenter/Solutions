class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Initialize result collecction
        res = []
        # Initialize state collection
        combo = []
        
        # Create backtracking method
        # State parameters: 
        #   - i where i is the number in the range [1, n]
        def backtrack(i):
            # Check if current state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if len(combo) == k:
                res.append(combo[:])
                return
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for j in range(i, n + 1):
                # Reflect current choice in state collection
                combo.append(j)
                # Recurse on next choice space of next state
                backtrack(j + 1)
                # Clean up current choice (backtrack)
                combo.pop()

        backtrack(1)
        return res
