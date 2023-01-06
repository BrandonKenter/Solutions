'''
DFS
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            for dr, dc in directions:
                nei_r, nei_c = r + dr, c + dc
                if (
                    nei_r in range(m) and
                    nei_c in range(n) and 
                    (nei_r, nei_c) not in v and
                    grid[nei_r][nei_c] == 1
                ):
                    v.add((nei_r, nei_c))
                    dfs(nei_r, nei_c)

        m, n = len(grid), len(grid[0])
        v = set()
        for r in range(m):
            for c in range(n):
                if (
                    (r == 0 or r == m - 1 or c == 0 or c == n - 1) and
                    grid[r][c] == 1 and
                    (r, c) not in v
                ):
                    v.add((r, c))
                    dfs(r, c)
        
        e = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in v:
                    e += 1
        return e


'''
BFS
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        v = set()
        q = deque()
        for r in range(m):
            for c in range(n):
                if (
                    (r == 0 or r == m - 1 or c == 0 or c == n - 1) and
                    grid[r][c] == 1 and
                    grid[r][c] not in v
                ):
                    q.append((r, c))
                    v.add((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nei_r, nei_c = r + dr, c + dc
                    if (
                        nei_r in range(m) and 
                        nei_c in range(n) and 
                        (nei_r, nei_c) not in v and
                        grid[nei_r][nei_c] == 1
                    ):
                        q.append((nei_r, nei_c))
                        v.add((nei_r, nei_c))

        e = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in v and grid[r][c] == 1:
                    e += 1
        return e