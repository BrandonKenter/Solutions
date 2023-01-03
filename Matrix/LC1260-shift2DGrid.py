class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        tmp = [[0 for c in range(n)] for r in range(m)]
        
        for r in range(m):
            for c in range(n):
                new_i = (r * n + c + k) % (m * n)
                new_r = new_i // n
                new_c = new_i % n
                tmp[new_r][new_c] = grid[r][c]
        return tmp