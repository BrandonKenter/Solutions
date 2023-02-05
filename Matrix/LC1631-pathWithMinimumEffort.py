class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        min_h = [(0, 0, 0)] # (path_max, row, col)
        dist = [[float('inf') for col in range(n)] for r in range(m)] # min path distances to each every cell
        dist[0][0] = 0

        while min_h:
            path_max, r, c = heapq.heappop(min_h)
            if r == m - 1 and c == n - 1:
                return dist[r][c]

            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                
                if (
                    nei_r in range(m) and 
                    nei_c in range(n) 
                ):
                    nei_dif = abs(heights[r][c] - heights[nei_r][nei_c])
                    new_dif = max(path_max, nei_dif)
                    if new_dif < dist[nei_r][nei_c]:        
                        dist[nei_r][nei_c] = new_dif
                        heapq.heappush(min_h, (new_dif, nei_r, nei_c))