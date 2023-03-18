'''
DFS
O(N) time / O(N) space
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i : [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        vis = set()
        def dfs(cur, prev):
            vis.add(cur)
            for nei in adj[cur]:
                if nei != prev:
                    if nei in vis: return False
                    if not dfs(nei, cur): return False
            return True
        return dfs(0, -1) and len(vis) == n


'''
BFS
O(N) time / O(N) space
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i : [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        q = deque([(0, -1)])
        vis = set([0])
        while q:
            for i in range(len(q)):
                cur, prev = q.popleft()
                
                for nei in adj[cur]:
                    if nei != prev:
                        if nei in vis:
                            return False
                        q.append((nei, cur))
                        vis.add(nei)
        return True if len(vis) == n else False


'''
Union-Find
O(N * α(N)) time / O(N) space
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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        components = n
        for a, b in edges:
            if uf.is_connected(a, b):
                return False
            uf.union(a, b)
            components -= 1
        return components == 1
