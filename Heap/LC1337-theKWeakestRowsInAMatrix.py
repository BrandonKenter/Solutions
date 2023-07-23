class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        freq = [[] for i in range(n + 1)]
        for i in range(m):
            soldiers = self.get_soldiers(n, mat[i])
            freq[soldiers].append(i)
        res = []
        for i in range(len(freq)):
            for row in freq[i]:
                res.append(row)
                k -= 1
                if k == 0:
                    return res
    
    def get_soldiers(self, n, row):
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if row[mid] == 0:
                right = mid
            else:
                left = mid + 1
        return left
        
