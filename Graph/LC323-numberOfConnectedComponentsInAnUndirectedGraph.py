'''
DFS
O(V + E) time / O(V) space
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        vis = set()
        def dfs(cur):
            vis.add(cur)
            for nei in adj[cur]:
                if nei not in vis:
                    dfs(nei)

        connected = 0
        for node in range(n):
            if node not in vis:
                dfs(node)
                connected += 1
        return connected


'''
BFS
O(V + E) time / O(V) space
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        vis = set()

        def bfs(src):
            q = deque([src])
            
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append(nei)
        
        connected = 0
        for node in range(n):
            if node not in vis:
                vis.add(node)
                bfs(node)
                connected += 1
        return connected


'''
Union-Find
O(V + E * α(N)) time / O(V) space
'''
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        connected = n
        for a, b in edges:
            if uf.is_connected(a, b) == False:
                uf.union(a, b)
                connected -= 1
        return connected
