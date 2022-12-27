'''
DFS
'''
class Solution:    
    def isCyclic(self, V, adj):
        vis = set()
        cur_vis = set()
        
        def dfs(i):
            if i in vis:
                return False
            if i in cur_vis:
                return True
            
            cur_vis.add(i)
            for nei in adj[i]:
                if dfs(nei): return True
            cur_vis.remove(i)
            vis.add(i)
            return False
        
        for i in range(V):
            if dfs(i): return True
        return False

'''
BFS (Kahn's)
'''
class Solution:
    def isCyclic(self, V, adj):
        indegree = [0] * V
        for a in range(V):
            for b in adj[a]:
                indegree[b] += 1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        cnt = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                cnt += 1
                
                # Added cur to topo sort, so can decrement indegree of neighbors
                for nei in adj[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0: q.append(nei)
                    
        if cnt == V: return False
        return True