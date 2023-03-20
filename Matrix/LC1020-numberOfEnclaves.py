'''
DFS
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def dfs(r, c):
            for dr, dc in directions:
                nei_r, nei_c = r + dr, c + dc
                if (
                    nei_r in range(m) and
                    nei_c in range(n) and 
                    (nei_r, nei_c) not in vis and
                    grid[nei_r][nei_c] == 1
                ):
                    vis.add((nei_r, nei_c))
                    dfs(nei_r, nei_c)

        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()

        for r in range(m):
            for c in range(n):
                if (
                    (r == 0 or r == m - 1 or c == 0 or c == n - 1) and
                    grid[r][c] == 1 and
                    (r, c) not in vis
                ):
                    vis.add((r, c))
                    dfs(r, c)
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in vis:
                    count += 1
        return count


'''
BFS
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()
        q = deque()
        for r in range(m):
            for c in range(n):
                if (
                    (r == 0 or r == m - 1 or c == 0 or c == n - 1) and
                    grid[r][c] == 1 
                ):
                    vis.add((r, c))
                    q.append((r, c))
                    
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nei_r, nei_c = r + dr, c + dc
                    if (
                        nei_r in range(m) and 
                        nei_c in range(n) and 
                        (nei_r, nei_c) not in vis and
                        grid[nei_r][nei_c] == 1
                    ):
                        vis.add((nei_r, nei_c))
                        q.append((nei_r, nei_c))
                        

        count = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in vis and grid[r][c] == 1:
                    count += 1
        return count
        