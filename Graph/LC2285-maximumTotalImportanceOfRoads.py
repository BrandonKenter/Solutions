class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
        
        edge_counts = sorted([len(l) for l in adj.values()])
        total_i = 0
        for i in range(n, 0, -1):
            total_i += i * edge_counts[i-1]
        return total_i
        