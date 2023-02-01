class Solution:
    def totalNQueens(self, n: int) -> int:
        col, posDiag, negDiag = set(), set(), set()
        res = 0
        
        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if (
                    c not in col and
                    (r + c) not in posDiag and
                    (r - c) not in negDiag
                ):
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)

                    backtrack(r + 1)

                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
        backtrack(0)
        return res