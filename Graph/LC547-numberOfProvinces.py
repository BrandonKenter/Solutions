'''
DFS
O(N^2) time / O(N) space
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        vis = set()
        
        def dfs(cur):
            for nei, adj in enumerate(isConnected[cur]):
                if adj and nei not in vis:
                    vis.add(nei)
                    dfs(nei)
        
        provinces = 0
        for node in range(N):
            if node not in vis:
                dfs(node)
                provinces += 1
        return provinces


'''
BFS
O(N^2) time / O(N) space
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        vis = set()

        def bfs(src):
            q = deque([src])
            vis.add(src)
            
            while q:
                for i in range(len(q)):
                    cur = q.popleft()

                    for nei, adj in enumerate(isConnected[cur]):
                        if adj and nei not in vis:
                            vis.add(nei)
                            q.append(nei)
        
        provinces = 0
        for node in range(N):
            if node not in vis:
                bfs(node)
                provinces += 1
        return provinces


'''
Union-Find
O(N^2 * α(N)) time / O(N) space
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:     
        provinces = len(isConnected)
        uf = UnionFind(provinces)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    if uf.is_connected(i, j) == False:
                        uf.union(i, j)
                        provinces -= 1
        return provinces
