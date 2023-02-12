class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        res = 0
        
        while l <= r:
            m = (l + r) // 2
            coins = (m*(m+1)) / 2
            if coins < n:
                res = m
                l = m + 1
            elif coins > n:
                r = m - 1
            else:
                return m
        return res