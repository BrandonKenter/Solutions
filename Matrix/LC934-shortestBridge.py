class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        vis = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            vis.add((r, c))
            q.append((r, c))

            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(n) and 
                    nei_c in range(n) and 
                    grid[nei_r][nei_c] == 1 and
                    (nei_r, nei_c) not in vis
                ):
                    dfs(nei_r, nei_c)
        
        
        def bfs():
            shortest = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    
                    for dr, dc in directions:
                        nei_r, nei_c = dr + r, dc + c
                        if (
                            nei_r in range(n) and 
                            nei_c in range(n) and 
                            (nei_r, nei_c) not in vis
                        ):
                            if grid[nei_r][nei_c] == 1 and (nei_r, nei_c) not in vis:
                                return shortest
                            q.append((nei_r, nei_c))
                            vis.add((nei_r, nei_c))
                shortest += 1
            return shortest
        

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()
                    