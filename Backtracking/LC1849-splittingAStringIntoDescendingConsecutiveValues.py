class Solution:
    def splitString(self, s: str) -> bool:
        # Create backtracking method
        def backtrack(i, prev, count):
            # Check if current state is a solution
            # If so, return True because asked if ONE solution exists
            if i == len(s) and count >= 2:
                return True
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for j in range(i, len(s)):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                nxt = int(s[i:j+1])
                if prev is not None and nxt != prev - 1:
                    continue
                # Choice meets constraints
                # Reflect current choice in state collections
                # In this case, there are no state collections to update
                #   since the state is just int variables as arguments. If
                #   we had a need for a set or array that tracked the 
                #   state, we would update it here.
                # Recurse on next choice space of next state
                # Add if condition and return value
                if backtrack(j + 1, nxt, count + 1):
                    return True
                # Clean up choice (backtrack)
                # There is nothing to clean up because the arguments
                #   are the only way we track the state. So when we
                #   backtrack, the execution context uses the arguments
                #   in that call. If we use state collections outside of
                #   the parameter list, this is where we would undo 
                #   the change to that collection for this choice.
            return False
        return backtrack(0, None, 0)