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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        connected = n
        extra = 0
        for a, b in connections:
            if uf.is_connected(a, b):
                extra += 1
            else:
                uf.union(a, b)
                connected -= 1
        return connected - 1 if extra >= connected - 1 else -1
        