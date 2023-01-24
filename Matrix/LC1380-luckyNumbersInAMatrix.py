class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_mins = [float('inf')] * m
        col_maxs = [float('-inf')] * n
        for r in range(m):
            for c in range(n):
                row_mins[r] = min(row_mins[r], matrix[r][c])
                col_maxs[c] = max(col_maxs[c], matrix[r][c])
        res = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == row_mins[r] and matrix[r][c] == col_maxs[c]:
                    res.append(matrix[r][c])
        return res