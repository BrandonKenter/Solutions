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
            
            for nei in adj[cur]:
                dfs(nei)
            
            vis.add(cur)
            res.append(cur)
        
        for i in range(V):
            if i not in vis:
                dfs(i)
        return res[::-1]

'''
BFS (Kahn's)
'''
class Solution:
    def topoSort(self, V, adj):
        indegree = [0] * V
        for a in range(V):
            for b in adj[a]:
                indegree[b] += 1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return ans