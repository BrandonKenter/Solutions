class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows, cols, diag, rev_diag = [0] * 3, [0] * 3, 0, 0
        player = 1
        m = 0

        for row, col in moves:
            rows[row] += player
            cols[col] += player
            if row == col: diag += player
            if row + col == 3 - 1: rev_diag += player
            m += 1

            if rows[row] == 3 or cols[col] == 3 or diag == 3 or rev_diag == 3:
                return 'A'
            elif rows[row] == -3 or cols[col] == -3 or diag == -3 or rev_diag == -3:
                return 'B'
            player *= -1
                
        if m != 9: return 'Pending'
        else: return 'Draw'