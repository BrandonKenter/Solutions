'''
DFS
'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {i : [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        vis = set()
        def dfs(cur):
            vis.add(cur)
            if cur == destination:
                return True
            
            for nei in adj[cur]:
                if nei not in vis and dfs(nei):
                    return True
            return False
        return dfs(source)


'''
BFS
'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {i : [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        vis = set()
        vis.add(source)
        q = deque([source])
        while q:
            cur = q.popleft()

            if cur == destination:
                return True

            for nei in adj[cur]:
                if nei not in vis:
                    q.append(nei)
                    vis.add(nei)
        return False