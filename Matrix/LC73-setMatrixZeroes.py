class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        top_l = 1
        
        # Flag rows and cols
        for r in range(M):
            for c in range(N):
                if r == 0 and matrix[r][c] == 0:
                    top_l = 0
                elif matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # Set inner cells depending on flag
        for r in range(1, M):
            for c in range(1, N):
                if matrix[r][0] == 0:
                    matrix[r][c] = 0
                elif matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        # Set left col cells depending on flag
        if matrix[0][0] == 0:
            for i in range(M):
                matrix[i][0] = 0
        
        # Set top rrow cells depending on flag
        if top_l == 0:
            for i in range(N):
                matrix[0][i] = 0
