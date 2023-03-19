'''
DFS
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()
        
        def dfs(r, c):
            vis.add((r, c))
            board[r][c] = 'T'
            
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(m) and 
                    nei_c in range(n) and 
                    (nei_r, nei_c) not in vis and
                    board[nei_r][nei_c] == 'O'
                ):
                    dfs(nei_r, nei_c)
        
        # 'O' -> 'T' for 'O' connected to edges
        for r in range(m):
            for c in range(n):
                if (
                    (r == 0 or r == m - 1 or c == 0 or c == n - 1) and
                    (r, c) not in vis and
                    board[r][c] == 'O'
                ):
                    dfs(r, c)
        
        # 'O' -> 'X' for 'O' NOT connected to edges
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        # 'T' -> 'O' for 'O' connected to edges
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'T':
                    board[r][c] = 'O'


'''
BFS
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()

        def bfs(sr, sc):
            vis.add((sr, sc))
            q = deque([(sr, sc)])
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    board[r][c] = 'T'
                    for dr, dc in directions:
                        nei_r, nei_c = dr + r, dc + c
                        if (
                            nei_r in range(m) and 
                            nei_c in range(n) and 
                            (nei_r, nei_c) not in vis and
                            board[nei_r][nei_c] == 'O'
                        ):
                            vis.add((nei_r, nei_c))
                            q.append((nei_r, nei_c))
                            

        # 'O' -> 'T' for 'O' connected to edges
        for r in range(m):
            for c in range(n):
                if (
                    (r == 0 or r == m - 1 or c == 0 or c == n - 1) and
                    (r, c) not in vis and
                    board[r][c] == 'O'
                ):
                    bfs(r, c)
        
        # 'O' -> 'X' for 'O' NOT connected to edges
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        # 'T' -> 'O' for 'O' connected to edges
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        