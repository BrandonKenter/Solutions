class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()
        p = 0

        def is_water(r, c):
            if (
                r not in range(m) or
                c not in range(n) or 
                grid[r][c] == 0
            ):
                return True
            return False

        def dfs(r, c):
            nonlocal p
            vis.add((r, c))
            for dr, dc in directions:
                nei_r, nei_c = r + dr, c + dc
                if is_water(nei_r, nei_c):
                    p += 1
                elif (nei_r, nei_c) not in vis:
                    dfs(nei_r, nei_c)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return p
                    