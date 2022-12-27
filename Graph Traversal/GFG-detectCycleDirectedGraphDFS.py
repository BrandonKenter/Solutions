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