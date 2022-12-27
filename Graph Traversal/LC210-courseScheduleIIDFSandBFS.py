'''
DFS
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            premap[crs].append(pre)
         
        v = set()
        v_cur = set()
        def dfs(crs):
            if crs in v:
                return True
            if crs in v_cur:
                return False
            
            v_cur.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            v_cur.remove(crs)
            v.add(crs)
            res.append(crs)
            return True
        
        res = []
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res

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