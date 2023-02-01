class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Use three sets to check the validity of each current state change 
        # in constant time. 
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        # Insert each non-empty cell's value to its corresponding sets
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].add(int(board[r][c]))
                    cols[c].add(int(board[r][c]))
                    squares[(r // 3, c // 3)].add(int(board[r][c]))
        
        def backtrack(r, c):
            # The "is valid state" base case is our first logic we add to 
            # our backtracking methods. If this check for being valid is
            # more than a couple lines, this is a good part of the method
            # that can be moved to a helper method such as "is_valid_state()".
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
            else:
                # Since this cell is empty, we attempt to make a choice on this cell
                # for every possible choice within the constraints. 
                # The constraints are: 
                #   1) Value must be 1 - 9
                #   2) Each value must be unique for its respective row/col/square
                for num in range(1, 10):
                    # If this choice does not satisfy the constraints, we do not
                    # explore this choice (so we do nothing and the algorithm 
                    # continues to the next num in the for loop).
                    if (
                        num not in rows[r] and
                        num not in cols[c] and 
                        num not in squares[(r // 3, c // 3)]
                    ):
                        # If this choice does satisfy the constraints and we are 
                        # in the if block, we explore this choice by adding the value
                        # to its respective sets and updating the board.
                        rows[r].add(num)
                        cols[c].add(num)
                        squares[(r // 3, c // 3)].add(num)
                        board[r][c] = str(num)
                        
                        # Once we make our choice, we recurse on the next cell.
                        # If this recursive call returns True (the base case returned
                        # True in that case), then we can return True. Note this will
                        # only return True if we are on the bottom-right cell as 
                        # this was the last cell we had to verify in our constraints, 
                        # so the row in the next call will be 9, which triggers the 
                        # base case.
                        if backtrack(new_r, new_c):
                            return True
                        
                        # This choice didn't lead to a valid state, so remove the
                        # decision so that we can make a different choice on the
                        # next iteration.
                        rows[r].remove(num)
                        cols[c].remove(num)
                        squares[(r // 3, c // 3)].remove(num)
                        board[r][c] = '.'
        backtrack(0, 0)