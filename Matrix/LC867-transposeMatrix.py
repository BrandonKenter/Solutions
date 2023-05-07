class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        new_matrix = [[0 for row in range(m)] for col in range(n)]
        print(new_matrix)
        for r in range(m):
            for c in range(n):
                new_matrix[c][r] = matrix[r][c]
        return new_matrix
        