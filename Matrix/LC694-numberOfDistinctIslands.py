'''
DFS
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()
        islands = set()

        def dfs(r, c, coord_list, sr, sc):
            vis.add((r, c))
            coord_list.append((r-sr, c-sc))

            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(m) and 
                    nei_c in range(n) and 
                    (nei_r, nei_c) not in vis and
                    grid[nei_r][nei_c] == 1
                ):
                    dfs(nei_r, nei_c, coord_list, sr, sc)
            return tuple(coord_list)
        
        for r in range(m):
            for c in range(n):
                if (r, c) not in vis and grid[r][c] == 1:
                    island = dfs(r, c, [], r, c)
                    islands.add(island)
        return len(islands)


'''
BFS
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis = set()
        islands = set()

        def bfs(sr, sc, coord_list):
            q = deque([(sr, sc)])
            vis.add((sr, sc))
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    coord_list.append((r - sr, c - sc))
                    for dr, dc in directions:
                        nei_r, nei_c = dr + r, dc + c
                        if (
                            nei_r in range(m) and 
                            nei_c in range(n) and 
                            (nei_r, nei_c) not in vis and
                            grid[nei_r][nei_c] == 1
                        ):
                            vis.add((nei_r, nei_c))
                            q.append((nei_r, nei_c))
            return tuple(coord_list)
        
        for r in range(m):
            for c in range(n):
                if (r, c) not in vis and grid[r][c] == 1:
                    island = bfs(r, c, [])
                    islands.add(island)
        return len(islands)
