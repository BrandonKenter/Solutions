class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        length = sum(matchsticks) // 4
        if sum(matchsticks) / 4 != length:
            return False
        
        # Initialize state collection
        sides = [0] * 4
        
        # Create backtracking method
        # State parameters: 
        #   - i where i is the index of the matchsticks array
        def backtrack(i):
            # Check if current state is a solution
            # If so, return True because asked if ONE solution exists
            if i == len(matchsticks):
                return True
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for j in range(4):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if matchsticks[i] + sides[j] <= length:
                    # Choice meets constraints
                    # Reflect current choice in state collections
                    sides[j] += matchsticks[i]
                    # Recurse on next choice space of next state
                    # Add if condition and return value
                    if backtrack(i + 1):
                        return True
                    # Clean up choice (backtrack)
                    # i is automatically cleaned up because we are returning
                    # to the previous execution context with previous arg
                    sides[j] -= matchsticks[i]

        return backtrack(0)
