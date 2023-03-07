class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row_ones, col_ones = defaultdict(int), defaultdict(int)
        row_zeros, col_zeros = defaultdict(int), defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1
                else:
                    row_zeros[i] += 1
                    col_zeros[j] += 1
        
        dif = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                dif[i][j] = row_ones[i] + col_ones[j] - row_zeros[i] - col_zeros[j]
        return dif
        