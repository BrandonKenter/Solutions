class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Helper method to check if the current cell in dfs is valid
        def is_valid(r, c):
            if (
                r not in range(m) or 
                c not in range(n) or 
                (r, c) in vis or 
                grid[r][c] == 1
            ):
                return False
            return True
        
        # DFS to visit all 0 cells that are connected together
        def dfs(r, c):
            vis.add((r, c))
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if is_valid(nei_r, nei_c):
                    dfs(nei_r, nei_c)
        
        # Mark all edge cells as visited since they can't be a part of closed islands
        for r in range(m):
            for c in range(n):
                if (r, c) not in vis and grid[r][c] == 0:
                    if (
                        r == 0 or r == m - 1 or 
                        c == 0 or c == n - 1
                    ):
                        dfs(r, c)
        
        # The remaining 0 cells have to be surrounded by 1's
        # So DFS from each unvisited 0, the DFS will spread and mark each
        # connected 0 cell as visited and after every connected 0 cell is 
        # visited, we add 1 to the count.
        count = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in vis and grid[r][c] == 0:
                    dfs(r, c)
                    count += 1
        return count