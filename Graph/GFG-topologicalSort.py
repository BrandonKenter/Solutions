'''
DFS
'''
class Solution:
    def topoSort(self, V, adj):
        vis = set()
        res = []
        
        def dfs(cur):
            if cur in vis:
                return
            
            vis.add(cur)
            for nei in adj[cur]:
                dfs(nei)
            res.append(cur)
        
        for node in range(V):
            if node not in vis:
                dfs(node)
        return res[::-1]


'''
BFS (Kahn's)
'''
class Solution:
    def topoSort(self, V, adj):
        indegree = [0 for i in range(V)]
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        
        q = deque()
        for node in range(V):
            if indegree[node] == 0:
                q.append(node)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res
    