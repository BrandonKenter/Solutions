'''
DFS
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        vis = set()
        cur_vis = set()

        def dfs(crs):
            if crs in vis:
                return True
            if crs in cur_vis:
                return False
            
            cur_vis.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            cur_vis.remove(crs)
            vis.add(crs)
            ans.append(crs)
            return True
        
        ans = []
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return ans

'''
BFS (Kahn's)
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1
        
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        ans = []
        while q:
            crs = q.popleft()
            ans.append(crs)

            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)

        if len(ans) == numCourses:
            return ans[::-1]
        else:
            return []
