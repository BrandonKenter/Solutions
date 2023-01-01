class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        times = [float('inf')] * (n * n)
        times[0] = grid[0][0]
        min_h = [(grid[0][0], 0, 0)] # (time, row, col)

        while min_h:
            time, row, col = heapq.heappop(min_h)

            for dr, dc in directions:
                nei_row, nei_col = dr + row, dc + col
                if (
                    nei_row in range(n) and 
                    nei_col in range(n)
                ):
                    nei_time = max(time, grid[nei_row][nei_col])
                    nei_idx = nei_row * n + nei_col
                    if nei_time < times[nei_idx]:
                        times[nei_idx] = nei_time
                        heapq.heappush(min_h, (nei_time, nei_row, nei_col))
        return times[-1]