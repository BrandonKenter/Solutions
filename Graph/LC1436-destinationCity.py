class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adj = {}
        for a, b in paths:
            adj[a] = b

        def dfs(cur):
            if cur not in adj:
                return cur
            
            return dfs(adj[cur])
        
        return dfs(paths[0][0])