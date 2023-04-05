'''
DFS
'''
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            nonlocal mini, maxi
            mini, maxi = min(mini, (r, c)), max(maxi, (r, c))
            vis.add((r, c))

            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(m) and 
                    nei_c in range(n) and 
                    (nei_r, nei_c) not in vis and 
                    land[nei_r][nei_c] == 1
                ):
                    dfs(nei_r, nei_c)
        
        vis, res = set(), []
        mini, maxi = (m, n), (-1, -1)
        for r in range(m):
            for c in range(n):
                if (r, c) not in vis and land[r][c] == 1:
                    dfs(r, c)
                    r1, c1 = mini
                    r2, c2 = maxi
                    mini, maxi = (m, n), (-1, -1)
                    res.append([r1, c1, r2, c2])
        return res


'''
BFS
'''
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(sr, sc):
            nonlocal mini, maxi
            q = deque([(sr, sc)])
            
            while q:
                r, c = q.popleft()
                mini, maxi = min(mini, (r, c)), max(maxi, (r, c))
                
                for dr, dc in directions:
                    nei_r, nei_c = dr + r, dc + c
                    if (
                        nei_r in range(m) and 
                        nei_c in range(n) and 
                        (nei_r, nei_c) not in vis and 
                        land[nei_r][nei_c] == 1
                    ):
                        vis.add((nei_r, nei_c))
                        q.append((nei_r, nei_c))
                        
        vis, res = set(), []
        mini, maxi = (m, n), (-1, -1)
        for r in range(m):
            for c in range(n):
                if (r, c) not in vis and land[r][c] == 1:
                    vis.add((r, c))
                    bfs(r, c)
                    r1, c1 = mini
                    r2, c2 = maxi
                    mini, maxi = (m, n), (-1, -1)
                    res.append([r1, c1, r2, c2])
        return res
