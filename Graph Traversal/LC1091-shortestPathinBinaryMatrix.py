class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        directions = [[1, 1,], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
        q = deque([[0, 0]])
        vis = set((0, 0))

        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if [r, c] == [n - 1, n - 1]: return dist
                
                for dr, dc in directions:
                    nei_r, nei_c = r + dr, c + dc
                    if (
                        nei_r in range(n) and 
                        nei_c in range(n) and 
                        (nei_r, nei_c) not in vis and 
                        grid[nei_r][nei_c] == 0
                    ):
                        q.append([nei_r, nei_c])
                        vis.add((nei_r, nei_c))
            dist += 1
        return -1