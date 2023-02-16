class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        # Initialize result variable
        max_gold = 0
        # Initialize state collections
        vis = set()
        
        # Create backtracking method
        # State parameters:
        #   - r where r is the current row
        #   - c where c is the current column
        #   - cur_gold where cur_gold is the sum of gold along the current path
        def backtrack(r, c, cur_gold):
            # Update the max_gold every time we extend our path with a 
            # valid choice
            nonlocal max_gold
            max_gold = max(max_gold, cur_gold)

            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if (
                    nei_r not in range(m) or
                    nei_c not in range(n) or
                    (nei_r, nei_c) in vis or 
                    grid[nei_r][nei_c] == 0
                ):
                    continue

                # Choice meets constraints
                # Reflect current choice in state collection
                vis.add((nei_r, nei_c))
                # Recurse on next choice space of next state
                backtrack(nei_r, nei_c, cur_gold + grid[nei_r][nei_c])
                # Clean up current choice (backtrack)
                vis.remove((nei_r, nei_c))
        
        # Call backtrack on every cell that is not 0 to try all possible paths
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    vis.add((r, c))
                    backtrack(r, c, grid[r][c])
                    vis.remove((r, c))
        return max_gold