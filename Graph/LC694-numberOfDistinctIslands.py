'''
DFS
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        v = set()
        coords = set() # tuples of coordinates for each island

        def dfs(orig, r, c, cur_coords):
            v.add((r, c))
            cur_coords.append((r - orig[0], c - orig[1]))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(m) and
                    nei_c in range(n) and 
                    (nei_r, nei_c) not in v and
                    grid[nei_r][nei_c] == 1
                ):
                    dfs(orig, nei_r, nei_c, cur_coords)
            return cur_coords

        for r in range(m):
            for c in range(n):
                if (r, c) not in v and grid[r][c] == 1:
                    coords.add(tuple(dfs((r, c), r, c, [])))
        print(coords)
        return len(coords)


'''
BFS
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        v = set()
        coords = set() # tuples of coordinates for each island

        def bfs(orig_r, orig_c):
            v.add((orig_r, orig_c))
            q = deque([(orig_r, orig_c)])
            cur_coords = []
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    cur_coords.append((r - orig_r, c - orig_c))

                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in directions:
                        nei_r, nei_c = dr + r, dc + c
                        if (
                            nei_r in range(m) and 
                            nei_c in range(n) and 
                            (nei_r, nei_c) not in v and
                            grid[nei_r][nei_c] == 1
                        ):
                            q.append((nei_r, nei_c))
                            v.add((nei_r, nei_c))
            coords.add(tuple(cur_coords))

        for r in range(m):
            for c in range(n):
                if (r, c) not in v and grid[r][c] == 1:
                    bfs(r, c)
        return len(coords)