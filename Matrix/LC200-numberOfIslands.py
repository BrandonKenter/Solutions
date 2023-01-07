class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        v = set()
        
        def dfs(r, c):
            if (
                r not in range(M) or 
                c not in range(N) or 
                (r, c) in v or
                grid[r][c] == '0'
            ):
                return
            
            v.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col)
        
        res = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == '1' and (r, c) not in v:
                    dfs(r, c)
                    res += 1
        return res