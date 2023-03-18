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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for a, b in pairs:
            if uf.is_connected(a, b) == False:
                uf.union(a, b)
        
        component_chars = defaultdict(list)
        for i in range(len(s)): 
            component_chars[uf.find(i)].append(s[i]) 
        
        for r in component_chars.keys():
            component_chars[r].sort(reverse=True)

        res = []
        for i in range(len(s)):
            res.append(component_chars[uf.find(i)].pop()) 
        return "".join(res)
