class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ns = defaultdict(int) # {col : max_height}
        ew = defaultdict(int) # {row : max_height}

        for r in range(m):
            for c in range(n):
                ns[c] = max(ns[c], grid[r][c])
                ew[r] = max(ew[r], grid[r][c])
        
        res = 0
        for r in range(m):
            for c in range(n):
                mini = min(ns[c], ew[r])
                res += mini - grid[r][c]
        return res
        