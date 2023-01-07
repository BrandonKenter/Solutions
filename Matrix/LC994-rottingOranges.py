class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        v = set()
        q = deque() 
        fresh = 0
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    v.add((r, c))
        
        t = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (
                        row not in range(M) or 
                        col not in range(N) or 
                        (row, col) in v or
                        grid[row][col] != 1
                    ):
                        continue
                    
                    q.append((row, col))
                    v.add((row, col))
                    fresh -= 1
            t += 1
        return t if fresh == 0 else -1