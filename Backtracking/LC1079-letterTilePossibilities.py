class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Initialize result collection
        res = set()
        # Initialize state collection
        used = [False] * len(tiles)
        perm = []

        # Create backtracking method
        # State parameters: 
        #   - none 
        def backtrack():
            # Check if we reached end of state space tree
            # Don't add to result collection here because we are 
            #   adding all non-empty sequences to the collection 
            #   when we make our choice to add to the sequence
            # Return to previous choice space
            if len(perm) == len(tiles):
                return
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for i in range(len(tiles)):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if used[i]:
                    continue
                
                # Choice meets constraints
                # Choice is to use tiles[j]
                # Reflect current choice in state collection
                perm.append(tiles[i])
                used[i] = True
                res.add(tuple(perm))
                # Recurse on next choice space of next state
                backtrack()
                # Clean up current choice (backtrack)
                perm.pop()
                used[i] = False

        backtrack()
        return len(res)