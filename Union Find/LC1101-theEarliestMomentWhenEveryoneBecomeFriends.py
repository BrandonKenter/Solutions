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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)
        connected = n
        for t, x, y in logs:
            if uf.is_connected(x, y) == False:
                uf.union(x, y)
                connected -= 1
                if connected == 1:
                    return t
        return -1
            