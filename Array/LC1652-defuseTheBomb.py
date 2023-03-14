class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * len(code)
        for i in range(n):
            if k > 0:
                s = 0
                for j in range(k):
                    s += code[(i + j + 1) % n]
                res[i] = s
            elif k < 0:
                s = 0 
                for j in range(abs(k)):
                    s += code[(i - j - 1 + n) % n]
                res[i] = s
            else:
                res[i] = 0
        return res
        