'''
DFS
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = {i : [] for i in range(n)}
        for u in range(n):
            for v in graph[u]:
                adj[u].append(v)
        
        cur_vis = set()
        vis = set()

        def dfs(cur):
            if cur in vis:
                return True
            if cur in cur_vis:
                return False
            
            cur_vis.add(cur)
            for nei in adj[cur]:
                if not dfs(nei): return False
            cur_vis.remove(cur)
            vis.add(cur)
            return True
        
        ans = []
        for i in range(n):
            if dfs(i): ans.append(i)
        return ans

'''
BFS (Kahn's)
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = {i : [] for i in range(n)}
        indegree = [0] * n
        for u in range(n):
            for v in graph[u]:
                adj[v].append(u)
                indegree[u] += 1
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        ans = []
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                ans.append(cur)

                for nei in adj[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

        return sorted(ans)