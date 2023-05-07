class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cur_vis = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (
                r not in range(m) or
                c not in range(n) or 
                (r, c) in cur_vis or
                grid[r][c] == -1
            ):
                return 0
            if grid[r][c] == 2 and len(cur_vis) == traversable:
                return 1
            
            paths = 0
            cur_vis.add((r, c))
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                paths += dfs(nei_r, nei_c)
            cur_vis.remove((r, c))
            return paths
        
        traversable = 0
        src_r, src_c = -1, -1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    src_r, src_c = r, c
                    traversable += 1
                if grid[r][c] == 0:
                    traversable += 1
        return dfs(src_r, src_c)
