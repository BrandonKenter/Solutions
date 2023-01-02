class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)
        
        def find(i):
            if i == par[i]:
                return i
            par[i] = find(par[i])
            return par[i]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return True

            if size[px] > size[py]:
                par[py] = px
                size[px] += size[py]
            else:
                par[px] = py
                size[py] += size[px]
            return False
        
        for a, b in edges:
            if union(a, b): return [a, b]
        return []