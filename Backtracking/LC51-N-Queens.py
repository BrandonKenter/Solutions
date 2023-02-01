class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, posDiag, negDiag = set(), set(), set()
        board = [["." for col in range(n)] for row in range(n)]
        res = []
        
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
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
                    board[r][c] = "Q"
                    
                    backtrack(r + 1)
                    
                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = "."
        backtrack(0)
        return res