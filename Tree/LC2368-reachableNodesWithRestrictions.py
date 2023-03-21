'''
DFS
'''
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = {i:[] for i in range(n)}
        r = set(restricted)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(cur, prev):
            nonlocal count
            count += 1
            for nei in adj[cur]:
                if nei not in r and nei != prev:
                    dfs(nei, cur)
        
        count = 0
        dfs(0, -1)
        return count


'''
BFS
'''
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        r = set(restricted)

        count = 0
        q = deque([(0, -1)])
        while q:
            cur, prev = q.popleft()
            count += 1
            for nei in adj[cur]:
                if nei not in r and nei != prev:
                    q.append((nei, cur))

        return count
        