class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        vis = set()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                    vis.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nei_r, nei_c = dr + r, dc + c
                    if (
                        nei_r in range(m) and 
                        nei_c in range(n) and 
                        (nei_r, nei_c) not in vis and 
                        grid[nei_r][nei_c] == 1
                    ):
                        vis.add((nei_r, nei_c))
                        fresh -= 1
                        q.append((nei_r, nei_c))
            time += 1
        return time if fresh == 0 else -1
    