class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        v = set()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                    v.add((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nei_r, nei_c = dr + r, dc + c
                    if (
                        nei_r in range(m) and 
                        nei_c in range(n) and 
                        (nei_r, nei_c) not in v
                    ):
                        q.append((nei_r, nei_c))
                        v.add((nei_r, nei_c))
                        mat[nei_r][nei_c] = dist
            dist += 1
        return mat