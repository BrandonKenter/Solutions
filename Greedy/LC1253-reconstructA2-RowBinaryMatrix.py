class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        mat = [[0 for col in range(n)] for row in range(2)]
        for c in range(n):
            if colsum[c] == 2:
                mat[0][c] = 1
                mat[1][c] = 1
                upper -= 1
                lower -= 1
            elif colsum[c] == 1:
                if upper > lower:
                    mat[0][c] = 1
                    upper -= 1
                else:
                    mat[1][c] = 1
                    lower -= 1
        return mat if upper == lower == 0 else []
