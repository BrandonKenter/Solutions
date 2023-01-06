class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        v = set()
        
        def dfs(r, c):
            if (
                r not in range(M) or 
                c not in range(N) or 
                (r, c) in v or
                board[r][c] != 'O'
            ):
                return
            
            v.add((r, c))
            board[r][c] = 'T'
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col)
        
        # 'O' -> 'T' for 'O' connected to edges
        for r in range(M):
            for c in range(N):
                if (r, c) not in v and board[r][c] == 'O' and (r == 0 or r == M - 1 or c == 0 or c == N - 1):
                    dfs(r, c)
        
        # 'O' -> 'X' for 'O' NOT connected to edges
        for r in range(M):
            for c in range(N):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        # 'T' -> 'O' for 'O' connected to edges
        for r in range(M):
            for c in range(N):
                if board[r][c] == 'T':
                    board[r][c] = 'O'