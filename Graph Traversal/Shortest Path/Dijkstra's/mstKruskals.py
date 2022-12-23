class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        size = [1] * V
        par = [i for i in range(V)]
        
        def find(n):
            if n == par[n]:
                return n
            par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return
            
            if size[p1] < size[p2]:
                size[p2] += size[p1]
                par[p1] = p2
            else:
                size[p1] += size[p2]
                par[p2] = p1
        
        edges = []
        for u in range(V):
            for v, w in adj[u]:
                edges.append([w, u, v])
        edges.sort()
  
        s = 0
        for edge in edges:
            weight, n1, n2 = edge
            if find(n1) != find(n2):
                s += weight
                union(n1, n2)
        return s