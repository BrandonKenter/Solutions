def shortestPath(self, n, m, edges):
    adj = {i : [] for i in range(n + 1)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    min_h = [(0, 1)]
    par = [i for i in range(n + 1)]
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    
    while min_h:
        path_weight, u = heapq.heappop(min_h)
        
        for v, v_weight in adj[u]:
            new_path_weight = path_weight + v_weight
            if new_path_weight < dist[v]:
                heapq.heappush(min_h, (new_path_weight, v))
                dist[v] = new_path_weight
                par[v] = u
    
    if dist[n] == float('inf'):
        return [-1]
    path = []
    cur = n
    while par[cur] != cur:
        path.append(cur)
        cur = par[cur]
    path.append(cur)
    return path[::-1]