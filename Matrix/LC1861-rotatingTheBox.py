class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for r in range(m):
            for c in range(n - 2, -1, -1):
                i = c
                while i < n - 1 and box[r][i] == '#' and box[r][i+1] == '.':
                    box[r][i] = '.'
                    box[r][i+1] = '#'
                    i += 1
        res = []
        for c in range(n):
            row = []
            for r in range(m - 1, -1, -1):
                row.append(box[r][c])
            res.append(row)
        return res
