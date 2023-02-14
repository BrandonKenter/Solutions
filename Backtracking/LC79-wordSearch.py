# Valid state checking before backtrack call
# Fits my pattern better of just having solution state check at beginning of backtrack method
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Initialize state collection
        vis = set()

        # Create backtracking method
        # State parameters: 
        #   - r where r is the row in the board
        #   - c where c is the col in the board
        #   - i where i is the index of a character in the word
        def backtrack(r, c, i):
            # Check if state is a solution and return True if so
            if i == len(word) - 1:
                return True

            # Make next choices from current state by calling backtrack
            # for every adjacent cell
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if (
                    nei_r not in range(m) or 
                    nei_c not in range(n) or
                    (nei_r, nei_c) in vis or 
                    i == len(word) - 1 or
                    board[nei_r][nei_c] != word[i+1]
                ):
                    continue

                # Choice meets constraints
                # Reflect current choice in state collections
                vis.add((nei_r, nei_c))

                # Recurse on next choice space of next state
                # Add if condition and return value
                if backtrack(nei_r, nei_c, i+1):
                    return True

                # Clean up current choice (backtrack)
                # r and c are automatically cleaned up because we are returning
                # to the previous execution context with previous args
                vis.remove((nei_r, nei_c))
        
        # Call backtrack on every cell whose char is the first char in word
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    vis.add((r, c))
                    if backtrack(r, c, 0): 
                        return True
                    vis.remove((r, c))
        return False


# # Valid state checking at start of backtrack method
# Does not have the optimization, so all test cases won't pass
# This is a interview-friendly solution (optimizations won't be expected in an interview)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(board), len(board[0])
        vis = set()

        def backtrack(r, c, i):
            # Base case to check if state is valid
            if (
                r not in range(m) or 
                c not in range(n) or
                (r, c) in vis or 
                board[r][c] != word[i]
            ):
                return
            
            # State is valid, so update state
            i += 1
            vis.add((r, c))

            # Check if state is a solution and return True if so
            if i == len(word):
                return True

            # Make next choices from current state by calling backtrack
            # for every adjacent cell
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                # Add the if condition to return early since we only care
                # about finding ONE solution
                if backtrack(nei_r, nei_c, i):
                    return True

            # Clean up choice 
            vis.remove((r, c))
        
        # Call backtrack on every cell whose char is the first char in word
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and backtrack(r, c, 0): 
                    return True
        return False
