class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()
        
        def dfs(r, c):
            if (
                r not in range(m) or
                c not in range(n) or 
                (r, c) in vis or
                grid[r][c] == 0
            ):
                return 0
            
            vis.add((r, c))
            num_fish = grid[r][c]
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                num_fish += dfs(nei_r, nei_c)
            return num_fish
        
        maxi = 0
        for r in range(m):
            for c in range(n):
                maxi = max(maxi, dfs(r, c))
        return maxi
