class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Initialize result collecction
        res = []
        # Initialize state collection
        combo = []

        # Create backtracking method
        # State parameters: 
        #   - i where i is the number in the range [1, 9]
        def backtrack(i, cur_sum):
            # Check if current state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if len(combo) == k and cur_sum == n:
                res.append(combo[:])
                return
            # Base case to check if current state is valid
            if len(combo) > k or cur_sum > n:
                return
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for j in range(i, 10):
                # Reflect current choice in state collection
                combo.append(j)
                # Recurse on next choice space of next state
                backtrack(j + 1, cur_sum + j)
                # Clean up current choice (backtrack)
                combo.pop()
                
        backtrack(1, 0)
        return res
