class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for a, b in edges:
            indegree[b] += 1
        
        res = []
        for node in range(n):
            if indegree[node] == 0:
                res.append(node)
        return res
        