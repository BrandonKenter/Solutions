class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque([(0, 0, 0, 0)]) # (r, c, cur_k, cur_d)
        vis = set([(0, 0, 0)]) # (r, c, cur_k)
        while q:
            r, c, cur_k, cur_d = q.popleft()
            if r == m-1 and c == n-1:
                return cur_d
            
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(m) and 
                    nei_c in range(n) and 
                    (nei_r, nei_c, cur_k) not in vis and 
                    (grid[nei_r][nei_c] == 0 or 
                    (grid[nei_r][nei_c] == 1 and cur_k + 1 <= k))
                ):
                    if grid[nei_r][nei_c] == 0:
                        q.append((nei_r, nei_c, cur_k, cur_d + 1))
                    else:
                        q.append((nei_r, nei_c, cur_k + 1, cur_d + 1))
                    vis.add((nei_r, nei_c, cur_k))
        return -1
