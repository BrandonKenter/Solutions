'''
DFS
'''
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = {i : [] for i in range(1, n + 1)}
        color = [-1] * (n + 1)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(cur):
            for nei in adj[cur]:
                # Adjacent is not colored, then color it
                if color[nei] == -1:
                    color[nei] = 1 - color[cur]
                    if not dfs(nei): return False
                # Adjacent color == cur color
                if color[nei] == color[cur]:
                    return False
            return True

        for i in range(1, n + 1):
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False
        return True


'''
BFS
'''
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = {i : [] for i in range(1, n + 1)}
        color = [-1] * (n + 1)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        def bfs(source):
            q = deque([source])
            
            while q:
                for i in range(len(q)):
                    cur = q.popleft()
                    
                    for nei in adj[cur]:
                        # Adjacent is not colored, then color it
                        if color[nei] == -1:
                            color[nei] = 1 - color[cur]
                            q.append(nei)
                        # Adjacent color == cur color
                        if color[nei] == color[cur]:
                            return False
            return True
        
        for i in range(1, n + 1):
            if color[i] == -1:
                color[i] = 0
                if not bfs(i):
                    return False
        return True
    