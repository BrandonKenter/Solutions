class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize state collections
        col, posDiag, negDiag = set(), set(), set()
        board = [["." for col in range(n)] for row in range(n)]
        # Initialize result collecction
        res = []
        
        # Create backtracking method
        # State parameters: 
        #   - r where r is the row in the board
        def backtrack(r):
            # Check if current state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for c in range(n):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                # Need to do this for this problem because adding to sets
                # that already have this element would not be reflected in 
                # the set, so we can't backtrack properly
                if (
                    c in col or
                    (r + c) in posDiag or 
                    (r - c) in negDiag
                ):
                    continue

                # Choice meets constraints
                # Reflect current choice in state collections
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                # Recurse on next choice space of next state
                backtrack(r + 1)
                
                # Clean up current choice (backtrack)
                # r is automatically cleaned up because we are returning
                # to the previous execution context with previous arg
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
