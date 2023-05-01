class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        pos = {}
        m, n = len(mat), len(mat[0])
        
        for r in range(m):
            for c in range(n):
                pos[mat[r][c]] = [r, c]
        
        for i in range(len(arr)):
            val = arr[i]
            row, col = pos[val]
            rows[row] += 1
            cols[col] += 1
            if rows[row] == n or cols[col] == m:
                return i
            