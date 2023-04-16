class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []
        for c in range(n):
            mini = maxi = grid[0][c]
            for r in range(m):
                mini = min(mini, grid[r][c])
                maxi = max(maxi, grid[r][c])
            max_len = max(len(str(mini)), len(str(maxi)))
            res.append(max_len)
        return res
        