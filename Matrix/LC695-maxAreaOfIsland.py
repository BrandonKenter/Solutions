'''
DFS
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        v = set()
        
        def dfs(r, c):
            a = 1
            v.add((r, c))
            
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c

                if (
                    nei_r in range(M) and 
                    nei_c in range(N) and 
                    (nei_r, nei_c) not in v and
                    grid[nei_r][nei_c] == 1
                ):
                    a += dfs(nei_r, nei_c)
            return a
        
        max_a = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1 and (r, c) not in v:
                    max_a = max(max_a, dfs(r, c))
        return max_a
        
        
'''
BFS
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        v = set()
        
        def bfs(r, c):
            a = 0
            q = deque([(r, c)])
            v.add((r, c))
            while q:
                for i in range(len(q)):
                    cur_r, cur_c = q.popleft()
                    a += 1

                    for dr, dc in directions:
                        nei_r, nei_c = dr + cur_r, dc + cur_c
                        if (
                            nei_r in range(M) and 
                            nei_c in range(N) and 
                            (nei_r, nei_c) not in v and 
                            grid[nei_r][nei_c] == 1
                        ):
                            q.append((nei_r, nei_c))
                            v.add((nei_r, nei_c))
            return a
        
        max_a = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1 and (r, c) not in v:
                    max_a = max(max_a, bfs(r, c))
        return max_a
        