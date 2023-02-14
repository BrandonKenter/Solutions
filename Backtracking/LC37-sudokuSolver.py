class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize state collections
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        # Seed state collections with current state
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].add(int(board[r][c]))
                    cols[c].add(int(board[r][c]))
                    squares[(r // 3, c // 3)].add(int(board[r][c]))
        
        # Create backtracking method
        # State parameters: 
        #   - r where r is the row in the board
        #   - c where c is the col in the board
        def backtrack(r, c):
            # Check if current state is a solution
            # If so, return True because asked if ONE solution exists
            if r == 9:
                return True
            
            # Since we are traversing the grid column-wise and then row-wise, 
            # we do not increment the row number every time we move to check
            # the next cell. We increment the row when the column number 
            # reaches 9. Note that this is 0-based indexing, so this logic
            # increments r by 1 and stores it in new_r if the column c 
            # becomes out of bounds/reaches column index 9 in the current row.
            new_r = r + ((c + 1) // 9)
            new_c = (c + 1) % 9
            
            # If the cell value is already chosen, skip it by recursing on 
            # the next cell. Since we're skipping, there is no need to 
            # have the logic of "if backtrack == True, return True, otherwise
            # remove traces of this choice" as we see in the else block.
            if board[r][c] != '.':
                return backtrack(new_r, new_c)
            
            # State is valid (empty cell), so can proceed to make choice on this state
            # Iterate through choices for current state
            for num in range(1, 10):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                # Need to do this for this problem because adding to sets
                # that already have this element would not be reflected in 
                # the set, so we can't backtrack properly
                if (
                    num in rows[r] or
                    num in cols[c] or 
                    num in squares[(r // 3, c // 3)]
                ):
                    continue

                # Choice meets constraints
                # Reflect current choice in state collections
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)
                board[r][c] = str(num)
                
                # Recurse on next choice space of next state
                # Add if condition and return value
                if backtrack(new_r, new_c):
                    return True
                
                # Clean up current choice (backtrack)
                # r is automatically cleaned up because we are returning
                # to the previous execution context with previous arg
                rows[r].remove(num)
                cols[c].remove(num)
                squares[(r // 3, c // 3)].remove(num)
                board[r][c] = '.'
                
        backtrack(0, 0)
