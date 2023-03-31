class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        max_h = []
        for i in range(m):
            soldiers = self.get_soldiers(n, mat[i])
            heappush(max_h, (-soldiers, -i))
            if len(max_h) > k:
                heappop(max_h)
        res = []
        while max_h:
            res.append(-1 * heappop(max_h)[1])
        return res[::-1]
    
    def get_soldiers(self, n, row):
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if row[mid] == 0:
                right = mid
            else:
                left = mid + 1
        return left
        