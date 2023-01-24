class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        for r in range(1, n-1):
            row = []
            for c in range(1, n-1):
                maxi = max(grid[r][c], grid[r+1][c], grid[r+1][c+1], grid[r][c+1], grid[r-1][c+1], grid[r-1][c], grid[r-1][c-1], grid[r][c-1], grid[r+1][c-1])
                row.append(maxi)
            res.append(row)
        return res
