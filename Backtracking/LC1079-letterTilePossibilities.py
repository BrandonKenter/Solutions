class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Initialize result collection
        count = 0
        # Initialize state collection
        perm = []
        used = [False for i in range(len(tiles))]
        tiles = sorted(tiles)

        # Create backtracking method
        # State parameters: 
        #   - none 
        def backtrack():
            # Check if we reached end of state space tree
            # Don't add to result collection here because we are 
            #   adding to non-empty sequence count when we make
            #    our choice to add to the sequence
            # Return to previous choice space
            nonlocal count
            if len(perm) == len(tiles):
                return
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for i in range(len(used)):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if used[i] == False:
                    if i > 0 and used[i - 1] == False and tiles[i] == tiles[i-1]:
                        continue
                
                # Choice meets constraints
                # Choice is to use tiles[i]
                # Reflect current choice in state collection
                perm.append(tiles[i])
                used[i] = True
                count += 1
                # Recurse on next choice space of next state
                backtrack()
                # Clean up current choice (backtrack)
                perm.pop()
                used[i] = False

        backtrack()
        return count
