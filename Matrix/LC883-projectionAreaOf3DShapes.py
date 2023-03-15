class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        yz = sum([max(r) for r in grid])

        zx = xy = 0
        for c in range(n):
            maxi = 0
            for r in range(n):
                maxi = max(maxi, grid[r][c])
                if grid[r][c] > 0:
                    xy += 1
            zx += maxi
        return xy + yz + zx
