'''
DFS
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        adj = {i : [] for i in range(V)}
        for i in range(V):
            for j in range(V):
                if isConnected[i][j]:
                    adj[i].append(j)

        vis = set()
        
        def dfs(cur):
            if cur is None:
                return 
            
            vis.add(cur)
            for nei in adj[cur]:
                if nei not in vis:
                    dfs(nei)
        
        provinces = 0
        for node in range(V):
            if node not in vis:
                provinces += 1
                dfs(node)
        return provinces

'''
BFS
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        adj = {i : [] for i in range(V)}
        for i in range(V):
            for j in range(V):
                if isConnected[i][j]:
                    adj[i].append(j)

        vis = set()

        def bfs(src):
            q = deque([src])
            vis.add(src)
            
            while q:
                for i in range(len(q)):
                    cur = q.popleft()

                    for nei in adj[cur]:
                        if nei not in vis:
                            q.append(nei)
                            vis.add(nei)
        
        provinces = 0
        for node in range(V):
            if node not in vis:
                provinces += 1
                bfs(node)
        return provinces