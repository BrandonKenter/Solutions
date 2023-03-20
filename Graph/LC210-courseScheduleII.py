'''
DFS
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        vis = set()
        path_vis = set()
        def dfs(cur):
            if cur in path_vis:
                return False
            if cur in vis:
                return True

            path_vis.add(cur)
            for nei in adj[cur]:
                if not dfs(nei):
                    return False
            path_vis.remove(cur)
            vis.add(cur)
            res.append(cur)
            return True

        res = []
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


'''
DFS (Kahn's)
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        indegree = [0 for i in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)

            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res[::-1] if len(res) == numCourses else []
