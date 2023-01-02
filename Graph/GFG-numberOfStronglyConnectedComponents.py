class Solution:
    def get_finish_times(self, i, finish_times, adj, v):
        v.add(i)
        for nei in adj[i]:
            if nei not in v:
                self.get_finish_times(nei, finish_times, adj, v)
        finish_times.append(i)
    
    def dfs(self, i, rev_adj, v):
        v.add(i)
        for nei in rev_adj[i]:
            if nei not in v:
                self.dfs(nei, rev_adj, v)
    
    def kosaraju(self, V, adj):
        finish_times = [] # last visited -> first visited
        v = set()
        
        # Step 1: Get ordering of nodes based on finish time
        for i in range(V):
            if i not in v:
                self.get_finish_times(i, finish_times, adj, v)
        
        # Step 2: Reverse adjacency list
        rev_adj = {i : [] for i in range(V + 1)}
        for a in range(V):
            for b in adj[a]:
                rev_adj[b].append(a)
        
        # Step 3: DFS in reversed adj list to get SCCs
        v.clear()
        scc = 0
        while finish_times:
            node = finish_times.pop()
            if node not in v:
                scc += 1
                self.dfs(node, rev_adj, v)
        return scc