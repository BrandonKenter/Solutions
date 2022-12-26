'''
Shortest path from a source to every other node in an undirected graph of weights = 1.
'''

'''
BFS
- Distance array 'dist' to store distances to each node and also acts as a visited set
- Queue 'q' to store (node, distance to node) pairs
'''
class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = {i : [] for i in range(n + 1)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque([(src, 0)])
        
        while q:
            for i in range(len(q)):
                node, node_dist = q.popleft()
                for nei in adj[node]:
                    nei_dist = node_dist + 1
                    if dist[nei] == float('inf'):
                        q.append((nei, nei_dist))
                        dist[nei] = nei_dist
                        
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist

'''
Dijkstra's
- Distance array 'dist' to store distances to each node
- Queue 'q' to store (node, distance to node) pairs
- Doesn't need visited set because "if nei < dist[nei]" acts as a visited check
'''
class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = {i : [] for i in range(n + 1)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque([(src, 0)])
        
        while q:
            for i in range(len(q)):
                node, node_dist = q.popleft()
                for nei in adj[node]:
                    nei_dist = node_dist + 1
                    if nei_dist < dist[nei]:
                        q.append((nei, nei_dist))
                        dist[nei] = nei_dist
                        
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist
