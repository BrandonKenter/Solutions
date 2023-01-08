'''
DFS
'''
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = {i : [] for i in range(1, n + 1)}
        for a, b, w in roads:
            adj[a].append((b, w))
            adj[b].append((a, w))
        
        vis = set()
        min_found = float('inf')
        def dfs(cur):
            nonlocal min_found
            vis.add(cur)
            
            for nei, nei_weight in adj[cur]:
                min_found = min(min_found, nei_weight)
                if nei not in vis:
                    dfs(nei)
        dfs(1)
        return min_found

'''
BFS
'''
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = {i : [] for i in range(1, n + 1)}
        for a, b, w in roads:
            adj[a].append((b, w))
            adj[b].append((a, w))

        vis = set()
        min_found = float('inf')
        q = deque([(1)])
        vis.add(1)
        while q:
            cur_node = q.popleft()
            
            for nei_node, nei_weight in adj[cur_node]:
                min_found = min(min_found, nei_weight)
                if nei_node not in vis:
                    q.append(nei_node)
                    vis.add(nei_node)
        return min_found