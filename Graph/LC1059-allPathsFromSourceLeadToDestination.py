class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
        
        vis = set()
        path_vis = set()
        
        def dfs(cur):
            if cur in path_vis:
                return False
            if cur in vis:
                return True

            path_vis.add(cur)
            for nei in adj[cur]:
                if not dfs(nei):
                    return False
            path_vis.remove(cur)
            vis.add(cur)
            if not adj[cur] and cur != destination:
                return False
            return True
        
        return dfs(source)
        