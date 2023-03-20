'''
DFS
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vis = set()
        cur_vis = set()

        def dfs(cur):
            if cur in cur_vis:
                return False
            if cur in vis:
                return True

            cur_vis.add(cur)
            for nei in graph[cur]:
                if not dfs(nei):
                    return False
            vis.add(cur)
            cur_vis.remove(cur)
            return True
            
        safe = []
        for node in range(len(graph)):
            if dfs(node):
                safe.append(node)
        return safe


'''
BFS
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(len(graph))}
        indegree = [0] * len(graph)
        for u in range(len(graph)):
            for v in graph[u]:
                adj[v].append(u)
                indegree[u] += 1
        
        q = deque()
        for node in range(len(indegree)):
            if indegree[node] == 0:
                q.append(node)
        
        res = []
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                res.append(cur)

                for nei in adj[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        return sorted(res)
    