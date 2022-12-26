class Solution:
    def dijkstra(self, V, adj, S):
        dist = [float('inf')] * V
        dist[S] = 0
        min_h = [(0, S)]
        
        while min_h:
            cur_dist, cur_node = heapq.heappop(min_h)
            
            for nei_node, nei_dist in adj[cur_node]:
                new_dist = cur_dist + nei_dist
                if new_dist < dist[nei_node]:
                    dist[nei_node] = new_dist
                    heapq.heappush(min_h, (new_dist, nei_node))
        return dist