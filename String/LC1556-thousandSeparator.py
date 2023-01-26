class Solution:
    def thousandSeparator(self, n: int) -> str:
        n, res = str(n), []
        digits = 0
        for i in range(len(n) - 1, -1, -1):
            res.append(n[i])
            digits += 1
            if digits % 3 == 0 and i != 0:
                res.append(".") 
        return "".join(res[::-1])