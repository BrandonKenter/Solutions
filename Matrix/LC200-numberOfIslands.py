'''
DFS
O(M*N) time / O(M*N) space
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()

        def dfs(r, c):
            vis.add((r, c))
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(m) and 
                    nei_c in range(n) and 
                    (nei_r, nei_c) not in vis and 
                    grid[nei_r][nei_c] == "1"
                ):
                    dfs(nei_r, nei_c)

        count = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in vis and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count


'''
BFS
O(M*N) time / O(M*N) space
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()

        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                cur_r, cur_c = q.popleft()
                for dr, dc in directions:
                    nei_r, nei_c = dr + cur_r, dc + cur_c
                    if (
                        nei_r in range(m) and 
                        nei_c in range(n) and 
                        (nei_r, nei_c) not in vis and 
                        grid[nei_r][nei_c] == "1"
                    ):
                        vis.add((nei_r, nei_c))
                        q.append((nei_r, nei_c))
        
        count = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in vis and grid[r][c] == "1":
                    vis.add((r, c))
                    bfs(r, c)
                    count += 1
        return count
