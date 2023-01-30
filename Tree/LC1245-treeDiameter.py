'''
DFS
O(N) time / O(H) space
'''
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(src):
            max_depth, peripheral = 0, None
            vis = set()

            def helper(cur, cur_depth):
                nonlocal max_depth, peripheral
                if cur is None:
                    return
                
                cur_depth += 1
                vis.add(cur)
                if cur_depth > max_depth:
                    max_depth = cur_depth
                    peripheral = cur
                for nei in adj[cur]:
                    if nei not in vis: helper(nei, cur_depth)
            helper(src, 0)
            return [max_depth, peripheral]

        _, peripheral = dfs(0)
        diam, _ = dfs(peripheral)
        return diam - 1
        

'''
BFS
O(N) time / O(N) space
'''
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def bfs(src):
            vis = set()
            vis.add(src)
            level = 0
            q = deque([src])
            peripheral = None
            while q:
                for i in range(len(q)):
                    cur = q.popleft()
                    peripheral = cur
                    for nei in adj[cur]:
                        if nei not in vis:
                            q.append(nei)
                            vis.add(nei)
                level += 1
            return [level, peripheral]
        
        _, peripheral = bfs(0)
        diam, _ = bfs(peripheral)
        return diam - 1
