'''
DFS
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


'''
BFS (Kahn's)
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        indegree = [0 for i in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        completed = 0
        while q:
            cur = q.popleft()
            completed += 1

            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return completed == numCourses
        