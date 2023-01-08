'''
DFS
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []

        def dfs(cur, cur_path):
            nonlocal n
            
            cur_path.append(cur)
            if cur == n - 1:
                paths.append(cur_path[::])

            for nei in graph[cur]:
                dfs(nei, cur_path)
            cur_path.pop()
        dfs(0, [])
        return paths

'''
BFS
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []

        q = deque([(0, [0])])
        while q:
            for i in range(len(q)):
                cur, cur_path = q.popleft()

                if cur == n - 1:
                    paths.append(cur_path)
                
                for nei in graph[cur]:
                    nei_path = cur_path[::]
                    nei_path.append(nei)
                    q.append((nei, nei_path))
        return paths