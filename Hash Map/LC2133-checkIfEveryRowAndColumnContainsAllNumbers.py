class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows, cols = defaultdict(set), defaultdict(set)
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                val = matrix[row][col]
                if val in rows[row] or val in cols[col]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
        return True