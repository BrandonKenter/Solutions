'''
DFS
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {crs : [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        vis = set()
        cur_vis = set()

        def dfs(cur):
            if cur in vis:
                return True
            if cur in cur_vis:
                return False
            
            cur_vis.add(cur)
            for pre in adj[cur]:
                if not dfs(pre): return False
            cur_vis.remove(cur)
            vis.add(cur)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

'''
BFS (Kahn's)
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {crs : [] for crs in range(numCourses)}
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1
        
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        count = numCourses
        while q:
            cur = q.popleft()
            count -= 1
            
            for pre in adj[cur]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        return count == 0