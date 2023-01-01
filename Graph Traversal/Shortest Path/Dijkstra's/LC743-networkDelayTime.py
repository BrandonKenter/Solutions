class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append((v, w))

        times = [float('inf')] * (n + 1)
        times[k] = 0
        min_h = [(0, k)]

        while min_h:
            cur_time, cur_node = heapq.heappop(min_h)
            if times[cur_node] < cur_time:
                continue
            
            for nei_node, nei_time in adj[cur_node]:
                new_time = cur_time + nei_time
                if new_time < times[nei_node]:
                    times[nei_node] = new_time
                    heapq.heappush(min_h, (new_time, nei_node))
        
        time = float('-inf')
        for i in range(1, n + 1):
            time = max(time, times[i])
        return time if time != float('inf') else -1