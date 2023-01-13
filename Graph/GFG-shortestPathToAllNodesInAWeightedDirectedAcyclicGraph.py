'''
DFS
'''
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(n)}
        for u, v, w in edges:
            adj[u].append((v, w))
        
        def dfs(node):
            for nei_node, nei_weight in adj[node]:
                dfs(nei_node)
            topo.append(node)
            
        topo = []
        for i in range(n):
            dfs(i)
        
        dist = [float('inf')] * n
        dist[0] = 0
        while topo:
            node = topo.pop()
            node_dist = dist[node]
            for nei in adj[node]:
                nei_dist = node_dist + nei[1]
                dist[nei[0]] = min(dist[nei[0]], nei_dist)
        for i, d in enumerate(dist):
            if d == float('inf'):
                dist[i] = -1
        return dist
        
        
'''
BFS (Kahn's)
'''
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(n)}
        indegree = [0] * n
        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1

        
        vis = set()
        def bfs(node):
            q = deque()
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)
            
            ans = []
            while q:
                for i in range(len(q)):
                    cur = q.popleft()
                    vis.add(cur)
                    ans.append(cur)
    
                    for nei in adj[cur]:
                        indegree[nei[0]] -= 1
                        if indegree[nei[0]] == 0:
                            q.append(nei[0])
            return ans
        
        topo = []
        for i in range(n):
            if i not in vis:
                topo.extend(bfs(i))
        
        dist = [float('inf')] * n
        dist[0] = 0
        for node in topo:
            node_dist = dist[node]
            for nei in adj[node]:
                nei_dist = node_dist + nei[1]
                dist[nei[0]] = min(dist[nei[0]], nei_dist)
        for i, d in enumerate(dist):
            if d == float('inf'):
                dist[i] = -1
        return dist