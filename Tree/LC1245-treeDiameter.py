'''
DFS
'''
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        vis = set()
        max_depth = 0
        perimeter_node = -1

        def dfs(cur, cur_depth):
            nonlocal max_depth, perimeter_node
            if cur is None:
                return

            cur_depth += 1
            vis.add(cur)
            if cur_depth > max_depth:
                max_depth = cur_depth
                perimeter_node = cur

            for nei in adj[cur]:
                if nei not in vis:
                    dfs(nei, cur_depth)
        
        dfs(0, 0)
        vis.clear()
        dfs(perimeter_node, 0)
        return max_depth - 1


'''
BFS
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
        
        level, peripheral = bfs(0)
        diam, peripheral_2 = bfs(peripheral)
        return diam - 1