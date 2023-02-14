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
