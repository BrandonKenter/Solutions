
'''
DFS
'''
class Solution:
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        cur_vis = set()
        vis = set()

        def dfs(cur, parent):
            if cur in vis:
                return False
            if cur in cur_vis:
                return True
            
            cur_vis.add(cur)
            for nei in adj[cur]:
                if nei != parent and dfs(nei, cur):
                    return True
            cur_vis.remove(cur)
            vis.add(cur)
            return False

        for i in range(V):
            if i not in vis and dfs(i, -1): return True
        return False

'''
BFS
'''
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = set()
        
        def bfs(i):
            q = deque([(i, -1)])
            while q:
                for i in range(len(q)):
                    cur_node, cur_parent = q.popleft()
                    
                    for nei in adj[cur_node]:
                        if nei != cur_parent:
                            if nei in vis: 
                                return True
                            else:  
                                vis.add(nei)
                                q.append((nei, cur_node))
            return False
        
        for i in range(V):
            if i not in vis and bfs(i):
                return True
        return False