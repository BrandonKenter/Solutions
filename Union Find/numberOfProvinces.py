'''
Union Find
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        sizes = [1] * n
        parents = [i for i in range(n)]

        def find(i):
            if i == parents[i]:
                return i
            parents[i] = find(parents[i])
            return parents[i]
        
        def union(x, y):
            px, py = find(x), find(y)

            if px == py: return False

            if sizes[px] < sizes[py]:
                sizes[py] += sizes[px]
                parents[px] = py
            else:
                sizes[px] += sizes[py]
                parents[py] = px
            return True
        
        count = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    if union(i, j):
                        count -= 1
        return count

'''
BFS
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    adj[i + 1].append(j + 1)
        
        vis = set()
        def bfs(i):
            q = deque([i])
            vis.add(i)
            while q:
                for i in range(len(q)):
                    cur = q.popleft()
                    for nei in adj[cur]:
                        if nei not in vis:
                            q.append(nei)
                            vis.add(nei)
                            
        count = 0
        for i in range(1, n + 1):
            if i not in vis:
                bfs(i)
                count += 1
        return count