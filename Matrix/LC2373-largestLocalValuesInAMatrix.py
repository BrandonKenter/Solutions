class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        for r in range(n-2):
            row = []
            for c in range(n-2):
                cur_max = 0
                for r_i in range(r, r + 3):
                    for c_i in range(c, c + 3):
                        cur_max = max(cur_max, grid[r_i][c_i])
                row.append(cur_max)
            res.append(row)
        return res