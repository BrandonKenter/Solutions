class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        arr = [[0 for col in range(n)] for row in range(m)]
        for idcs in indices:
            r, c = idcs
            
            for col in range(n):
                arr[r][col] += 1
            for row in range(m):
                arr[row][c] += 1
        
        odd = 0
        for r in range(m):
            for c in range(n):
                if arr[r][c] % 2:
                    odd += 1
        return odd
        