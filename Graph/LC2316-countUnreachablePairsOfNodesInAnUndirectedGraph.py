class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        vis = set()

        def dfs(cur, prev):
            vis.add(cur)
            size = 1
            for nei in adj[cur]:
                if nei is not prev and nei not in vis:
                    size += dfs(nei, cur)
            return size

        pairs = 0
        cur_total = dfs(0, -1)
        for node in range(1, n):
            if node not in vis:
                s = dfs(node, -1)
                pairs += s * cur_total
                cur_total += s
        return pairs
            